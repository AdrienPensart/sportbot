import copy
from dataclasses import dataclass, field
from functools import cached_property

import click
from beartype import beartype
from beartype.typing import Self
from progressbar import ProgressBar, Variable

from sportbot.exercise import (
    Exercise,
    Maintain,
    Prepare,
    TheEnd,
    Waiting,
    rhythmic_push_up,
)
from sportbot.helpers import flatten, intersperse, seconds_to_human
from sportbot.rest import Rest, _5_minutes_rest
from sportbot.sound import Bell
from sportbot.tag import Tag


@beartype
@dataclass
class Sequence:
    name: str
    exercices: list[Exercise]
    description: str | None = None
    tags: frozenset[Tag] = frozenset()
    register: bool = True

    def __post_init__(self) -> None:
        if self.register:
            known_sequences[self.name] = self

    @classmethod
    def rounds(cls, n: int, exercice: Exercise, waiting: Waiting, register: bool = False) -> Self:
        name = f"{n}_{exercice.name}"
        description = f"{n} {exercice.name} ({waiting})"
        interspersed = intersperse([copy.deepcopy(exercice) for _ in range(n)], waiting)
        exercices: list[Exercise] = flatten(interspersed)
        sequence = cls(name=name, description=description, exercices=exercices, register=register)
        return sequence

    @cached_property
    def bell(self) -> Bell:
        return Bell()

    @staticmethod
    def known_tags() -> set[str]:
        return set().union(*[sequence.tags for sequence in known_sequences.values()])

    def run(self, dry: bool = False, silence: bool = False) -> None:
        number = 0
        widgets = [Variable("progression", format="{formatted_value}")]
        print(f"{self}")
        with ProgressBar(max_value=self.length, widgets=widgets) as pbar:
            for exercice in self.exercices:
                if not isinstance(exercice, Waiting):
                    number += 1
                prefix = f"{number}/{self.length}, ({self.human_left_stopwatch} remaining)"
                exercice.run(prefix=prefix, dry=dry, pbar=pbar, silence=silence)
                pbar.update(number)

        if not silence:
            self.bell.say(dry)

    def __repr__(self) -> str:
        if self.description:
            representation = self.description
        else:
            representation = self.name
        joined_tags = " ".join(tag for tag in self.tags)
        if joined_tags:
            representation += f" ({joined_tags}),"
        representation += f" {self.length} exercices, duration: {self.human_exercices_duration}, rest: {self.human_rest_duration}, total duration: {self.human_total_duration}"
        return click.style(representation, fg="magenta")

    @property
    def only_rest(self) -> list[Exercise]:
        return list(filter(lambda exercice: isinstance(exercice, Rest), self.exercices))

    @property
    def only_exercices(self) -> list[Exercise]:
        return list(filter(lambda exercice: not isinstance(exercice, Waiting), self.exercices))

    @property
    def length(self) -> int:
        return len(self.only_exercices)

    @property
    def total_duration(self) -> int:
        return self.exercices_duration + self.rest_duration

    @property
    def human_total_duration(self) -> str:
        return seconds_to_human(self.total_duration)

    @property
    def rest_duration(self) -> int:
        return sum(rest.duration for rest in self.only_rest)

    @property
    def human_rest_duration(self) -> str:
        return seconds_to_human(self.rest_duration)

    @property
    def exercices_duration(self) -> int:
        return sum(exercice.duration for exercice in self.only_exercices)

    @property
    def human_exercices_duration(self) -> str:
        return seconds_to_human(self.exercices_duration)

    @property
    def left_stopwatch(self) -> int:
        return sum(exercice.stopwatch for exercice in self.exercices if not isinstance(exercice, Waiting))

    @property
    def human_left_stopwatch(self) -> str:
        return seconds_to_human(self.left_stopwatch)


@beartype
@dataclass(repr=False)
class PrepareSequence(Sequence):
    name: str = "prepare-sequence"
    description: str = "Prepare Sequence"
    exercices: list[Exercise] = field(default_factory=lambda: [Prepare()])
    register: bool = False


@beartype
@dataclass(repr=False)
class RestSequence(Sequence):
    name: str = "rest-sequence"
    description: str = "Rest Sequence"
    exercices: list[Exercise] = field(default_factory=lambda: [_5_minutes_rest])
    register: bool = False


@beartype
@dataclass(repr=False)
class EndSequence(Sequence):
    name: str = "end-sequence"
    description: str = "End Sequence"
    exercices: list[Exercise] = field(default_factory=lambda: [TheEnd()])
    register: bool = False


known_sequences: dict[str, Sequence] = {}

_10_rhythmic_push_up = Sequence.rounds(n=10, exercice=rhythmic_push_up, waiting=Maintain(), register=True)


@beartype
def create_sequence(
    name: str,
    description: str,
    exercices: list[Exercise],
    tags: set[Tag] | None = None,
) -> Sequence:
    real_tags = frozenset(tags) if tags is not None else frozenset()
    return Sequence(name=name, description=description, exercices=exercices, tags=real_tags)

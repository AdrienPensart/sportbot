import copy
from dataclasses import dataclass, field
from functools import cached_property

import click
from beartype import beartype
from beartype.typing import Self
from progressbar import ProgressBar, Variable

from sportbot.exercise import Exercise, rhythmic_push_up
from sportbot.helpers import flatten, intersperse, seconds_to_human
from sportbot.sound import Bell
from sportbot.tag import Tag
from sportbot.waiting import Maintain, Prepare, Rest, TheEnd, Waiting, _5_minutes_rest


@beartype
@dataclass
class Sequence:
    name: str
    exercises: list[Exercise]
    description: str | None = None
    register: bool = True

    def __post_init__(self) -> None:
        if self.register:
            KnownSequences[self.name] = self

    @classmethod
    def rounds(cls, n: int, exercise: Exercise, waiting: Waiting, register: bool = False) -> Self:
        name = f"{n}_{exercise.name}"
        description = f"{n} {exercise.name} ({waiting})"
        interspersed = intersperse([copy.deepcopy(exercise) for _ in range(n)], waiting)
        exercises: list[Exercise] = flatten(interspersed)
        sequence = cls(name=name, description=description, exercises=exercises, register=register)
        return sequence

    @cached_property
    def bell(self) -> Bell:
        return Bell()

    @property
    def tags(self) -> set[Tag]:
        return set().union(*[exercise.tags for exercise in self.exercises])

    @staticmethod
    def known_tags() -> set[str]:
        return set().union(*[sequence.tags for sequence in KnownSequences.values()])

    def run(self, dry: bool, silence: bool) -> None:
        number = 0
        widgets = [Variable("progression", format="{formatted_value}")]
        print(f"{self}")
        with ProgressBar(max_value=self.length, widgets=widgets) as pbar:
            for exercise in self.exercises:
                if not isinstance(exercise, Waiting):
                    number += 1
                prefix = f"{number}/{self.length}, ({self.human_left_stopwatch} remaining)"
                exercise.run(prefix=prefix, dry=dry, pbar=pbar, silence=silence)
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
        representation += f" {self.length} exercises, duration: {self.human_exercises_duration}, rest: {self.human_rest_duration}, total duration: {self.human_total_duration}"
        return click.style(representation, fg="magenta")

    @property
    def only_rest(self) -> list[Exercise]:
        return list(filter(lambda exercise: isinstance(exercise, Rest), self.exercises))

    @property
    def only_exercises(self) -> list[Exercise]:
        return list(filter(lambda exercise: not isinstance(exercise, Waiting), self.exercises))

    @property
    def length(self) -> int:
        return len(self.only_exercises)

    @property
    def total_duration(self) -> int:
        return self.exercises_duration + self.rest_duration

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
    def exercises_duration(self) -> int:
        return sum(exercise.duration for exercise in self.only_exercises)

    @property
    def human_exercises_duration(self) -> str:
        return seconds_to_human(self.exercises_duration)

    @property
    def left_stopwatch(self) -> int:
        return sum(exercise.stopwatch for exercise in self.exercises if not isinstance(exercise, Waiting))

    @property
    def human_left_stopwatch(self) -> str:
        return seconds_to_human(self.left_stopwatch)


@beartype
@dataclass(repr=False)
class PrepareSequence(Sequence):
    name: str = "prepare-sequence"
    description: str = "Prepare Sequence"
    exercises: list[Exercise] = field(default_factory=lambda: [Prepare()])
    register: bool = False


@beartype
@dataclass(repr=False)
class RestSequence(Sequence):
    name: str = "rest-sequence"
    description: str = "Rest Sequence"
    exercises: list[Exercise] = field(default_factory=lambda: [_5_minutes_rest])
    register: bool = False


@beartype
@dataclass(repr=False)
class EndSequence(Sequence):
    name: str = "end-sequence"
    description: str = "End Sequence"
    exercises: list[Exercise] = field(default_factory=lambda: [TheEnd()])
    register: bool = False


KnownSequences: dict[str, Sequence] = {}

_10_rhythmic_push_up = Sequence.rounds(n=10, exercise=rhythmic_push_up, waiting=Maintain())

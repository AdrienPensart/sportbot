from typing import Tuple, Dict, Set, FrozenSet, Optional
import copy
import functools
import click
import attr
from progressbar import ProgressBar, Variable  # type: ignore
from sportbot.helpers import flatten, intersperse, seconds_to_human, classproperty
from sportbot.sound import Bell
from sportbot.exercice import BaseExercice, Exercice, Prepare, TheEnd, Maintain, Waiting, rhythmic_push_up
from sportbot.rest import Rest, _5_minutes_rest


@attr.s(auto_attribs=True, repr=False, hash=True)
class Sequence:
    name: str
    exercices: Tuple[BaseExercice, ...]
    description: Optional[str] = None
    tags: FrozenSet[str] = frozenset()
    register: bool = True

    def __attrs_post_init__(self) -> None:
        if self.register:
            known_sequences[self.name] = self

    @staticmethod
    def rounds(n: int, exercice: Exercice, waiting: Waiting, register=False):
        name = f"{n}_{exercice.name}"
        description = f"{n} {exercice.name} ({waiting})"
        exercices = flatten(intersperse([copy.deepcopy(exercice) for _ in range(n)], waiting))
        sequence = Sequence(name=name, description=description, exercices=exercices, register=register)
        return sequence

    @functools.cached_property
    def bell(self):
        return Bell()

    @classproperty
    def known_tags(cls, obj) -> Set[str]:  # pylint: disable=no-self-argument,no-self-use,unused-argument
        return set().union(*[sequence.tags for sequence in known_sequences.values()])  # type: ignore

    def run(self, dry=False):
        number = 0
        widgets = [Variable("progression", format='{formatted_value}')]
        print(self)
        with ProgressBar(max_value=self.length, widgets=widgets) as pbar:
            for exercice in self.exercices:
                if not isinstance(exercice, Waiting):
                    number += 1
                prefix = f"{number}/{self.length}, ({self.human_left_stopwatch} remaining)"
                exercice.run(prefix=prefix, dry=dry, pbar=pbar)
                pbar.update(number)

        self.bell.say(dry)

    def __repr__(self):
        if self.description:
            representation = self.description
        else:
            representation = self.name
        joined_tags = ' '.join(self.tags)
        if joined_tags:
            representation += f" ({joined_tags}),"
        representation += f" {self.length} exercices, duration: {self.human_exercices_duration}, rest: {self.human_rest_duration}, total duration: {self.human_total_duration}"
        return click.style(representation, fg="magenta")

    @property
    def only_rest(self):
        return list(filter(lambda exercice: isinstance(exercice, Rest), self.exercices))

    @property
    def only_exercices(self):
        return list(filter(lambda exercice: isinstance(exercice, Exercice), self.exercices))

    @property
    def length(self):
        return len(self.only_exercices)

    @property
    def total_duration(self) -> int:
        return self.exercices_duration + self.rest_duration

    @property
    def human_total_duration(self) -> str:
        return seconds_to_human(self.total_duration)

    @property
    def rest_duration(self) -> int:
        return sum([rest.duration for rest in self.only_rest])

    @property
    def human_rest_duration(self) -> str:
        return seconds_to_human(self.rest_duration)

    @property
    def exercices_duration(self) -> int:
        return sum([exercice.duration for exercice in self.only_exercices])

    @property
    def human_exercices_duration(self) -> str:
        return seconds_to_human(self.exercices_duration)

    @property
    def left_stopwatch(self) -> int:
        return sum([exercice.stopwatch for exercice in self.exercices if not isinstance(exercice, Waiting)])

    @property
    def human_left_stopwatch(self) -> str:
        return seconds_to_human(self.left_stopwatch)


@attr.s(auto_attribs=True, repr=False, hash=True)
class PrepareSequence(Sequence):
    name: str = "prepare-sequence"
    description: str = "Prepare Sequence"
    exercices: Tuple[BaseExercice, ...] = tuple([Prepare()])
    register: bool = False


@attr.s(auto_attribs=True, repr=False, hash=True)
class RestSequence(Sequence):
    name: str = "rest-sequence"
    description: str = "Rest Sequence"
    exercices: Tuple[BaseExercice, ...] = tuple([_5_minutes_rest])
    register: bool = False


@attr.s(auto_attribs=True, repr=False, hash=True)
class TheEndSequence(Sequence):
    name: str = "the-end-sequence"
    description: str = "The End Sequence"
    exercices: Tuple[BaseExercice, ...] = tuple([TheEnd()])
    register: bool = False


known_sequences: Dict[str, Sequence] = {}

_10_rhythmic_push_up = Sequence.rounds(n=10, exercice=rhythmic_push_up, waiting=Maintain(), register=True)


def create_sequence(name: str, description: str, exercices: Tuple[BaseExercice, ...], tags: Optional[Set[str]] = None) -> Sequence:
    real_tags: FrozenSet[str] = frozenset(tags) if tags is not None else frozenset()
    return Sequence(name=name, description=description, exercices=exercices, tags=real_tags)  # type: ignore

from typing import FrozenSet, Optional, List
import click
import attr
import progressbar  # type: ignore
from sportbot.helpers import seconds_to_human
from sportbot.sound import bell
from sportbot.exercice import Exercice, Waiting
from sportbot.rest import Rest


@attr.s(auto_attribs=True, repr=False)
class Sequence:
    name: str
    exercices: List[Exercice]
    description: Optional[str] = None
    tags: FrozenSet[str] = attr.ib(default=frozenset(), converter=frozenset)

    def run(self, dry=False):
        number = 0
        widgets = [progressbar.Variable("progression", format='{formatted_value}')]
        print(self)
        with progressbar.ProgressBar(max_value=self.length, widgets=widgets) as pbar:
            for exercice in self.exercices:
                if not isinstance(exercice, Waiting):
                    number += 1
                prefix = f"{number}/{self.length}, ({self.human_left_stopwatch} remaining)"
                exercice.run(prefix=prefix, dry=dry, pbar=pbar)
                pbar.update(number)

        if not dry:
            bell()

    def __repr__(self):
        joined_tags = ' '.join(self.tags)
        if self.description:
            representation = self.description
        else:
            representation = self.name
        representation += f" ({joined_tags}), {self.length} exercices, duration: {self.human_exercices_duration}, rest: {self.human_rest_duration}, total duration: {self.human_total_duration}"
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
        return sum([exercice.stopwatch for exercice in self.exercices if type(exercice) != Waiting])  # pylint: disable=unidiomatic-typecheck

    @property
    def human_left_stopwatch(self) -> str:
        return seconds_to_human(self.left_stopwatch)

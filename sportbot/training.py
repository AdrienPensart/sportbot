from typing import Dict, Tuple
import click
import attr
from sportbot.sequence import Sequence
from sportbot.helpers import seconds_to_human


@attr.s(auto_attribs=True, repr=False, hash=True)
class Training:
    name: str
    sequences: Tuple[Sequence, ...]
    register: bool = True

    def __attrs_post_init__(self) -> None:
        if self.register:
            known_trainings[self.name] = self

    @property
    def tags(self):
        return set().union(*[sequence.tags for sequence in self.sequences])

    def __repr__(self):
        return click.style(f"{self.name} ({len(self.sequences)} sequences), duration: {self.human_total_duration}", fg="blue")

    @property
    def total_duration(self) -> int:
        return sum([sequence.total_duration for sequence in self.sequences])

    @property
    def human_total_duration(self) -> str:
        return seconds_to_human(self.total_duration)

    def run(self, dry=False):
        for sequence in self.sequences:
            sequence.run(dry=dry)


known_trainings: Dict[str, Training] = {}

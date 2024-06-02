from dataclasses import dataclass

import click
from beartype import beartype

from sportbot.helpers import seconds_to_human
from sportbot.sequence import Sequence
from sportbot.tag import Tag


@beartype
@dataclass
class Training:
    sequences: tuple[Sequence, ...]
    name: str = "Training"
    register: bool = True

    def __post_init__(self) -> None:
        if self.register:
            KnownTrainings[self.name] = self

    @property
    def tags(self) -> set[Tag]:
        return set().union(*[sequence.tags for sequence in self.sequences])

    def __repr__(self) -> str:
        return click.style(
            f"{self.name} ({len(self.sequences)} sequences), duration: {self.human_total_duration}",
            fg="blue",
        )

    @property
    def total_duration(self) -> int:
        return sum(sequence.total_duration for sequence in self.sequences)

    @property
    def human_total_duration(self) -> str:
        return seconds_to_human(self.total_duration)

    def run(self, dry: bool, silence: bool) -> None:
        for sequence in self.sequences:
            sequence.run(dry=dry, silence=silence)


KnownTrainings: dict[str, Training] = {}

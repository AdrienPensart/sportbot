from dataclasses import dataclass

import click
from beartype import beartype

from sportbot.exercises.helpers import seconds_to_human
from sportbot.exercises.sequence import Sequence
from sportbot.exercises.tag import Tag
from sportbot.exercises.waiting import Waiting


@beartype
@dataclass
class Training:
    sequences: tuple[Waiting | Sequence, ...]
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
            f"{self.name} ({len(self.sequences)} sequences), duration: {self.human_duration}",
            fg="blue",
        )

    @property
    def duration(self) -> int:
        return sum(sequence.duration for sequence in self.sequences)

    @property
    def human_duration(self) -> str:
        return seconds_to_human(self.duration)

    def run(self, dry: bool, silence: bool) -> None:
        for sequence in self.sequences:
            sequence.run(dry=dry, silence=silence)


KnownTrainings: dict[str, Training] = {}

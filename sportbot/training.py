from typing import Dict, Tuple
import attr
from sportbot.sequence import Sequence


@attr.s(auto_attribs=True, repr=False, hash=True)
class Training:
    name: str
    sequences: Tuple[Sequence]

    def __attrs_post_init__(self) -> None:
        known_trainings[self.name] = self

    @property
    def tags(self):
        return set().union(*[sequence.tags for sequence in self.sequences])

    def __repr__(self):
        return self.name

    def run(self, dry=False):
        for sequence in self.sequences:
            sequence.run(dry=dry)


known_trainings: Dict[str, Training] = {}

from typing import List
import attr
from sportbot.sequence import Sequence


@attr.s(auto_attribs=True)
class Sequences:
    sequences: List[Sequence]

    @property
    def tags(self):
        return set().union(*[sequence.tags for sequence in self.sequences])

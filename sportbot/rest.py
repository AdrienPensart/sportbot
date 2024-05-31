from dataclasses import dataclass
from typing import FrozenSet

from sportbot.exercise import Waiting


@dataclass
class Rest(Waiting):
    name: str = "Rest"
    color: str = "green"
    tags: FrozenSet[str] = frozenset({"rest"})


# RESTS
_15_seconds_rest = Rest(duration=15)
_30_seconds_rest = Rest(duration=30)
_45_seconds_rest = Rest(duration=45)
_60_seconds_rest = _1_minute_rest = Rest(duration=60)
_120_seconds_rest = _2_minutes_rest = Rest(duration=120)
_5_minutes_rest = Rest(duration=5 * 60)

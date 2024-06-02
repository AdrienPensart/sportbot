from enum import StrEnum, auto

from beartype import beartype


@beartype
class Tag(StrEnum):
    WAITING = auto()
    WARMING_UP = auto()
    STRENGTHENING = auto()
    ABS = auto()
    STATIONARY = auto()
    DYNAMIC = auto()
    FULL_BODY = auto()
    BOXING = auto()

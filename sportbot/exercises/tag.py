from enum import StrEnum, auto

from beartype import beartype


@beartype
class Tag(StrEnum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()
    WAITING = auto()
    WARM_UP = auto()
    STRENGTHENING = auto()
    ABS = auto()
    STATIONARY = auto()
    DYNAMIC = auto()
    FULL_BODY = auto()
    BOXING = auto()

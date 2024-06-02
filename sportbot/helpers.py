import collections
import copy
import datetime
import sys

from beartype import beartype
from beartype.typing import Any, Generator, Iterable

from sportbot.exercise import Exercise


class Py2Key:
    __slots__ = ("value", "typestr")

    def __init__(self, value: Any):
        self.value = value
        self.typestr = sys.intern(type(value).__name__)

    def __lt__(self, other: Any) -> bool:
        try:
            return self.value < other.value
        except TypeError:
            return self.typestr < other.typestr


@beartype
def seconds_to_human(seconds: int) -> str:
    """Human readable duration from seconds"""
    return str(datetime.timedelta(seconds=seconds))


@beartype
def deep_flatten(iterables: Iterable) -> Generator[Any, None, None]:
    """Recursively flatten argument"""
    for element in iterables:
        if isinstance(element, collections.abc.Iterable) and not isinstance(element, (str, bytes)):
            yield from deep_flatten(element)
        else:
            yield element


@beartype
def flatten(*iterables: Any) -> list:
    return list(deep_flatten(iterables))


@beartype
def join_exercices(iterable: Iterable, rest: Any) -> Generator[Exercise, None, None]:
    it = iter(iterable)
    n_round = 1
    total_round = sum(1 for i in iterable)

    try:
        first_exercice = next(it)
        first_exercice.name = f"{first_exercice.name}, round {n_round} on {total_round}"
        yield first_exercice
    except StopIteration:
        pass

    for next_exercice in it:
        yield copy.deepcopy(rest)
        n_round += 1
        next_exercice.name = f"{next_exercice.name}, round {n_round} on {total_round}"
        yield next_exercice


@beartype
def intersperse(exercices: Iterable, rest: Any) -> list:
    return list(join_exercices(exercices, rest))

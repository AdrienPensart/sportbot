import sys
import datetime
import copy
import collections


class classproperty:
    __slots__ = ('getter', )

    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj, cls):
        return self.getter(cls, obj)


class Py2Key:
    __slots__ = ("value", "typestr")

    def __init__(self, value):
        self.value = value
        self.typestr = sys.intern(type(value).__name__)

    def __lt__(self, other):
        try:
            return self.value < other.value
        except TypeError:
            return self.typestr < other.typestr


def seconds_to_human(seconds: int) -> str:
    '''Human readable duration from seconds'''
    return str(datetime.timedelta(seconds=seconds))


def deep_flatten(iterables):
    '''Recursively flatten argument'''
    for element in iterables:
        if isinstance(element, collections.abc.Iterable) and not isinstance(element, (str, bytes)):
            yield from deep_flatten(element)
        else:
            yield element


def flatten(*iterables):
    return list(deep_flatten(iterables))


def join_exercices(iterable, rest):
    it = iter(iterable)
    n_round = 1
    total_round = len(iterable)

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


def intersperse(exercices, rest):
    return list(join_exercices(exercices, rest))


def create_rounds(n, exercice, rest):
    return flatten(intersperse([copy.deepcopy(exercice) for _ in range(n)], rest))

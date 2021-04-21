import datetime
import copy
import collections


def seconds_to_human(seconds: int) -> str:
    '''Human readable duration from seconds'''
    return str(datetime.timedelta(seconds=seconds))


def deep_flatten(iterables):
    '''Recursively flatten argument'''
    for element in iterables:
        if isinstance(element, collections.Iterable) and not isinstance(element, (str, bytes)):
            yield from deep_flatten(element)
        else:
            yield element


def flatten(*iterables):
    return deep_flatten(iterables)


def join_exercices(iterable, rest):
    it = iter(iterable)
    n_round = 1
    total_round = len(iterable)

    first_exercice = next(it)
    first_exercice.label = f"{first_exercice.label} (round {n_round}/{total_round})"

    yield first_exercice
    for next_exercice in it:
        yield copy.deepcopy(rest)
        n_round += 1
        next_exercice.label = f"{next_exercice.label} (round {n_round}/{total_round})"
        yield next_exercice


def intersperse(exercices, rest):
    return list(join_exercices(exercices, rest))


def rounds(n, exercice, rest):
    return flatten(intersperse([copy.deepcopy(exercice) for _ in range(n)], rest))

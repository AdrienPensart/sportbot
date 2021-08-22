from typing import Dict, FrozenSet, Set
import functools
import time
import click
import attr
from sportbot.sound import player, Sound, Bell
from sportbot.helpers import classproperty


@attr.s(auto_attribs=True, hash=True, repr=False)
class BaseExercice:
    name: str
    duration: int
    color: str
    silence: bool = False
    stopwatch: int = 0
    tags: FrozenSet[str] = attr.ib(default=frozenset(), converter=frozenset)

    def __attrs_post_init__(self) -> None:
        self.stopwatch = self.duration
        if not isinstance(self, Waiting):
            known_exercices[self.name] = self

    def __repr__(self):
        if self.stopwatch != self.duration:
            return click.style(f"{self.name} : {self.stopwatch} / {self.duration} seconds", fg=self.color)
        return click.style(f"{self.name} : {self.stopwatch} seconds ", fg=self.color)

    @functools.cached_property
    def bell(self):
        return Bell()

    @functools.cached_property
    def sound(self):
        return Sound(self.name)

    @classproperty
    def known_tags(cls, obj) -> Set[str]:  # pylint: disable=no-self-argument,no-self-use,unused-argument
        return set().union(*[exercice.tags for exercice in known_exercices.values()])  # type: ignore

    def run(self, prefix, dry=False, pbar=None):
        if not self.silence:
            self.sound.say(dry)
            self.bell.say(dry)
        while self.stopwatch > 0:
            progression = f"{prefix} : {self}"
            if pbar:
                pbar.update(progression=progression)

            if not pbar or dry:
                print(progression)
            self.stopwatch -= 1

            if not dry:
                time.sleep(1)
                player().stop()


@attr.s(auto_attribs=True, hash=True, repr=False)
class Exercice(BaseExercice):
    color: str = "yellow"


@attr.s(auto_attribs=True, hash=True, repr=False)
class Waiting(BaseExercice):
    color: str = "bright_blue"


@attr.s(auto_attribs=True, hash=True, repr=False)
class Prepare(Waiting):
    name: str = 'Prepare'
    duration: int = 20


@attr.s(auto_attribs=True, hash=True, repr=False)
class TheEnd(Waiting):
    name: str = 'THE END'
    duration: int = 5


known_exercices: Dict[str, BaseExercice] = {}

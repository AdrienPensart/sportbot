from typing import FrozenSet
import time
import os
import click
import attr
from slugify import slugify
from gtts import gTTS  # type: ignore
from sportbot.sound import player, bell, say


def default_tts_path(name):
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    return f'{dir_path}/tts/{name}.mp3'


known_exercices = set()


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
            known_exercices.add(self)

    def __repr__(self):
        if self.stopwatch != self.duration:
            return click.style(f"{self.name} : {self.stopwatch} / {self.duration} seconds", fg=self.color)
        return click.style(f"{self.name} : {self.stopwatch} seconds ", fg=self.color)

    @property
    def tts_path(self) -> str:
        slug = slugify(self.name)
        _tts_path = default_tts_path(slug)
        if not os.path.isfile(_tts_path):
            tts = gTTS(self.name)
            _tts_path = f'/tmp/{slug}.mp3'
            tts.save(_tts_path)
        return _tts_path

    def run(self, prefix, dry=False, pbar=None):
        if not self.silence and not dry:
            wait_for = say(self.tts_path)
            time.sleep(wait_for)
            bell()
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
class Rest(Waiting):
    name: str = attr.ib(default="Rest")
    color: str = "green"
    tags: FrozenSet[str] = frozenset({"rest"})


@attr.s(auto_attribs=True, hash=True, repr=False)
class Boxing(Exercice):
    color: str = "red"
    tags: FrozenSet[str] = frozenset({"boxing"})

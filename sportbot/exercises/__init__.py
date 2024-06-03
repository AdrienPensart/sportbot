import time
from dataclasses import dataclass
from functools import cached_property

import click
from beartype import beartype
from progressbar import ProgressBar

from sportbot.exercises.tag import Tag
from sportbot.sound import BaseSound, Bell


@beartype
@dataclass
class Exercise:
    name: str = "Exercise"
    duration: int = 0
    stopwatch: int = 0
    color: str = "yellow"
    tags: frozenset[Tag] = frozenset()
    register: bool = True

    def __post_init__(self) -> None:
        self.stopwatch = self.duration
        if self.register and not isinstance(self, BaseWaiting):
            KnownExercises[self.name] = self

    def __repr__(self) -> str:
        if self.stopwatch != self.duration:
            return click.style(
                f"{self.name} : {self.stopwatch} / {self.duration} seconds",
                fg=self.color,
            )
        return click.style(f"{self.name} : {self.stopwatch} seconds", fg=self.color)

    @cached_property
    def bell(self) -> Bell:
        return Bell()

    @cached_property
    def sound(self) -> BaseSound:
        return BaseSound(self.name)

    @staticmethod
    def known_tags() -> set[Tag]:
        return set().union(*[exercise.tags for exercise in KnownExercises.values()])

    def run(
        self,
        dry: bool,
        silence: bool,
        prefix: str | None = None,
        pbar: ProgressBar | None = None,
    ) -> None:
        prefix = prefix if prefix is not None else ""
        if not silence:
            self.sound.say(dry=dry)
            self.bell.say(dry=dry)
        while self.stopwatch > 0:
            progression = f"{prefix} : {self}"
            if pbar is not None:
                pbar.update(progression=progression)

            if not pbar or dry:
                print(progression)
            self.stopwatch -= 1

            if not dry:
                time.sleep(1)


@beartype
@dataclass(repr=False, init=False)
class BaseWaiting(Exercise):
    name: str = "Waiting"
    color: str = "bright_blue"
    tags: frozenset[Tag] = frozenset({Tag.WAITING})


KnownExercises: dict[str, Exercise] = {}


@beartype
def create_exercise(name: str, duration: int, tags: set[Tag] | None = None, color: str | None = None) -> Exercise:
    real_tags: frozenset[Tag] = frozenset(tags) if tags is not None else frozenset()
    real_color: str = color if color is not None else "yellow"
    return Exercise(name=name, duration=duration, tags=real_tags, color=real_color)

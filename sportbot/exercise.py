import time
from dataclasses import dataclass
from functools import cached_property

import click
from beartype import beartype
from progressbar import ProgressBar

from sportbot.sound import BaseSound, Bell
from sportbot.tag import Tag


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
        if self.register and not isinstance(self, Waiting):
            known_exercises[self.name] = self

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
        return set().union(*[exercice.tags for exercice in known_exercises.values()])

    def run(
        self,
        prefix: str | None = None,
        dry: bool = False,
        silence: bool = False,
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
@dataclass(repr=False)
class Waiting(Exercise):
    name: str = "Waiting"
    color: str = "bright_blue"
    tags: frozenset[Tag] = frozenset({Tag.WAITING})


@beartype
@dataclass(repr=False)
class Prepare(Waiting):
    name: str = "Prepare"
    duration: int = 10

    def run(
        self,
        prefix: str | None = None,
        dry: bool = False,
        silence: bool = False,
        pbar: ProgressBar | None = None,
    ) -> None:
        prefix = prefix if prefix is not None else ""
        if not silence:
            self.sound.say(dry=dry)

        while self.stopwatch > 0:
            progression = f"{prefix} : {self}"
            if not silence:
                sound_countdown = BaseSound(name=str(self.stopwatch))
                sound_countdown.say(dry=dry)
            if pbar is not None:
                pbar.update(progression=progression)

            if not pbar or dry:
                print(progression)
            self.stopwatch -= 1

            if not dry:
                time.sleep(1)


@beartype
@dataclass(repr=False)
class Maintain(Waiting):
    name: str = "Maintain"
    duration: int = 2


@beartype
@dataclass(repr=False)
class TheEnd(Waiting):
    name: str = "The End"
    duration: int = 5


known_exercises: dict[str, Exercise] = {}


@beartype
def create_exercise(name: str, duration: int, tags: set[Tag] | None = None) -> Exercise:
    real_tags: frozenset[Tag] = frozenset(tags) if tags is not None else frozenset()
    return Exercise(name=name, duration=duration, tags=real_tags)


# SIMPLE

# Warm-Up
_30_seconds_heels_rise = create_exercise("Heels rise", duration=30, tags={Tag.WARMING_UP})
_30_seconds_knees_rise = create_exercise("Knees rise", duration=30, tags={Tag.WARMING_UP})
_30_seconds_heels_to_buttocks = create_exercise("Heels to buttocks", duration=30, tags={Tag.WARMING_UP})

# Jumping jacks
_30_seconds_jumping_jacks = create_exercise("Jumping jacks", duration=30, tags={Tag.FULL_BODY, Tag.DYNAMIC, Tag.WARMING_UP, Tag.STRENGTHENING})
_60_seconds_jumping_jacks = create_exercise("Jumping jacks", duration=60, tags={Tag.FULL_BODY, Tag.DYNAMIC, Tag.WARMING_UP, Tag.STRENGTHENING})

# Lunges
_30_seconds_forward_lunges = create_exercise("Forward lunges", duration=30, tags={Tag.DYNAMIC, Tag.WARMING_UP, Tag.STRENGTHENING})
_60_seconds_backward_lunges = create_exercise("Backward lunges", duration=60, tags={Tag.DYNAMIC, Tag.WARMING_UP, Tag.STRENGTHENING})

# Alternate lunges
_30_seconds_alternate_lunges = create_exercise("Alternate lunges", duration=30, tags={Tag.DYNAMIC, Tag.STRENGTHENING})
_60_seconds_alternate_lunges = create_exercise("Alternate lunges", duration=60, tags={Tag.DYNAMIC, Tag.STRENGTHENING})

# Crunchs
_30_seconds_crunchs = create_exercise("Crunchs", duration=30, tags={Tag.DYNAMIC, Tag.ABS, Tag.STRENGTHENING})
_60_seconds_crunchs = create_exercise("Crunchs", duration=60, tags={Tag.DYNAMIC, Tag.ABS, Tag.STRENGTHENING})

# Twists
_30_seconds_twists = create_exercise("Russian Twists", duration=30, tags={Tag.DYNAMIC, Tag.ABS, Tag.STRENGTHENING})
_60_seconds_twists = create_exercise("Russian Twists", duration=60, tags={Tag.DYNAMIC, Tag.ABS, Tag.STRENGTHENING})

# Mountain climbers
_30_seconds_mountain_climber = create_exercise("Mountain climber", duration=30, tags={Tag.DYNAMIC, Tag.WARMING_UP, Tag.STRENGTHENING})
_60_seconds_mountain_climber = create_exercise("Mountain climber", duration=60, tags={Tag.DYNAMIC, Tag.WARMING_UP, Tag.STRENGTHENING})

# Plank
_30_seconds_plank = create_exercise("Plank", duration=30, tags={Tag.STATIONARY, Tag.ABS, Tag.STRENGTHENING})
_60_seconds_plank = create_exercise("Plank", duration=60, tags={Tag.STATIONARY, Tag.ABS, Tag.STRENGTHENING})

# Chair
_30_seconds_chair = create_exercise("Chair", duration=30, tags={Tag.STATIONARY, Tag.STRENGTHENING})
_60_seconds_chair = create_exercise("Chair", duration=60, tags={Tag.STATIONARY, Tag.STRENGTHENING})

# Squats
_30_seconds_squats = create_exercise("Squats", duration=30, tags={Tag.DYNAMIC, Tag.STRENGTHENING})
_60_seconds_squats = create_exercise("Squats", duration=60, tags={Tag.DYNAMIC, Tag.STRENGTHENING})

# Squats
_30_seconds_jump_squats = create_exercise("Jump squats", duration=30, tags={Tag.DYNAMIC, Tag.STRENGTHENING})
_60_seconds_jump_squats = create_exercise("Jump squats", duration=60, tags={Tag.DYNAMIC, Tag.STRENGTHENING})

# Burpees
_10_burpees = create_exercise("10 Burpees", duration=60, tags={Tag.FULL_BODY, Tag.DYNAMIC, Tag.STRENGTHENING})
_30_seconds_burpees = create_exercise("Burpees", duration=30, tags={Tag.FULL_BODY, Tag.DYNAMIC, Tag.STRENGTHENING})
_60_seconds_burpees = create_exercise("Burpees", duration=60, tags={Tag.FULL_BODY, Tag.DYNAMIC, Tag.STRENGTHENING})

# Push-ups
_5_push_up = create_exercise("5 push-ups", duration=30, tags={Tag.DYNAMIC, Tag.WARMING_UP})
_10_push_up = create_exercise("10 push-ups", duration=60, tags={Tag.DYNAMIC, Tag.WARMING_UP})
_15_push_up = create_exercise("15 push-ups", duration=90, tags={Tag.DYNAMIC, Tag.WARMING_UP, Tag.STRENGTHENING})
_20_push_up = create_exercise("20 push-ups", duration=120, tags={Tag.DYNAMIC, Tag.WARMING_UP, Tag.STRENGTHENING})
_25_push_up = create_exercise("25 push-ups", duration=150, tags={Tag.DYNAMIC, Tag.WARMING_UP, Tag.STRENGTHENING})
rhythmic_push_up = create_exercise("Push-up", duration=2, tags={Tag.STRENGTHENING})

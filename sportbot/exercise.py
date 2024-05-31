import time
from dataclasses import dataclass
from functools import cached_property
from typing import Dict, FrozenSet, Optional, Set

import click
from progressbar import ProgressBar  # type: ignore

from sportbot.sound import BaseSound, Bell


@dataclass
class Exercise:
    name: str = "Exercise"
    duration: int = 0
    silence: bool = False
    stopwatch: int = 0
    color: str = "yellow"
    tags: FrozenSet[str] = frozenset()
    register: bool = True

    def __post_init__(self) -> None:
        self.stopwatch = self.duration
        if self.register and not isinstance(self, Waiting):
            known_exercises[self.name] = self

    def __repr__(self):
        if self.stopwatch != self.duration:
            return click.style(
                f"{self.name} : {self.stopwatch} / {self.duration} seconds",
                fg=self.color,
            )
        return click.style(f"{self.name} : {self.stopwatch} seconds", fg=self.color)

    @cached_property
    def bell(self):
        return Bell()

    @cached_property
    def sound(self):
        return BaseSound(self.name)

    @staticmethod
    def known_tags() -> Set[str]:
        return set().union(*[exercice.tags for exercice in known_exercises.values()])

    def run(
        self,
        prefix: Optional[str] = None,
        dry=False,
        pbar: Optional[ProgressBar] = None,
    ):
        prefix = prefix if prefix is not None else ""
        if not self.silence:
            self.sound.say(dry=dry)
            self.bell.say(dry=dry)
        while self.stopwatch > 0:
            progression = f"{prefix} : {self}"
            if pbar:
                pbar.update(progression=progression)

            if not pbar or dry:
                print(progression)
            self.stopwatch -= 1

            if not dry:
                time.sleep(1)


@dataclass
class Waiting(Exercise):
    name: str = "Waiting"
    color: str = "bright_blue"


@dataclass
class Prepare(Waiting):
    name: str = "Prepare"
    duration: int = 10

    def run(
        self,
        prefix: Optional[str] = None,
        dry=False,
        pbar: Optional[ProgressBar] = None,
    ):
        prefix = prefix if prefix is not None else ""
        if not self.silence:
            self.sound.say(dry=dry)

        while True:
            progression = f"{prefix} : {self}"
            sound_countdown = BaseSound(name=str(self.stopwatch))
            if not self.silence:
                sound_countdown.say(dry=dry)
            if pbar:
                pbar.update(progression=progression)

            if not pbar or dry:
                print(progression)
            self.stopwatch -= 1
            if self.stopwatch == 0:
                break


@dataclass
class Maintain(Waiting):
    name: str = "Maintain"
    duration: int = 2
    silence: bool = True


@dataclass
class TheEnd(Waiting):
    name: str = "The End"
    duration: int = 5


known_exercises: Dict[str, Exercise] = {}


def create_exercise(name: str, duration: int, tags: Optional[Set[str]] = None, silence: bool = False) -> Exercise:
    real_tags: FrozenSet[str] = frozenset(tags) if tags is not None else frozenset()
    return Exercise(name=name, duration=duration, silence=silence, tags=real_tags)  # type: ignore


# SIMPLE

# Warm-Up
_30_seconds_heels_rise = create_exercise("Heels rise", duration=30, tags={"warming-up"})
_30_seconds_knees_rise = create_exercise("Knees rise", duration=30, tags={"warming-up"})
_30_seconds_heels_to_buttocks = create_exercise("Heels to buttocks", duration=30, tags={"warming-up"})

# Jumping jacks
_30_seconds_jumping_jacks = create_exercise("Jumping jacks", duration=30, tags={"warming-up", "strengthening"})
_60_seconds_jumping_jacks = create_exercise("Jumping jacks", duration=60, tags={"warming-up", "strengthening"})

# Lunges
_30_seconds_forward_lunges = create_exercise("Forward lunges", duration=30, tags={"warming-up", "strengthening"})
_60_seconds_backward_lunges = create_exercise("Backward lunges", duration=60, tags={"warming-up", "strengthening"})

# Alternate lunges
_30_seconds_alternate_lunges = create_exercise("Alternate lunges", duration=30, tags={"strengthening"})
_60_seconds_alternate_lunges = create_exercise("Alternate lunges", duration=60, tags={"strengthening"})

# Crunchs
_30_seconds_crunchs = create_exercise("Crunchs", duration=30, tags={"strengthening"})
_60_seconds_crunchs = create_exercise("Crunchs", duration=60, tags={"strengthening"})

# Twists
_30_seconds_twists = create_exercise("Twists", duration=30, tags={"strengthening"})
_60_seconds_twists = create_exercise("Twists", duration=60, tags={"strengthening"})

# Mountain climbers
_30_seconds_mountain_climber = create_exercise("Mountain climber", duration=30, tags={"warming-up", "strengthening"})
_60_seconds_mountain_climber = create_exercise("Mountain climber", duration=60, tags={"warming-up", "strengthening"})

# Plank
_30_seconds_plank = create_exercise("Plank", duration=30, tags={"strengthening"})
_60_seconds_plank = create_exercise("Plank", duration=60, tags={"strengthening"})

# Chair
_30_seconds_chair = create_exercise("Chair", duration=30, tags={"strengthening"})
_60_seconds_chair = create_exercise("Chair", duration=60, tags={"strengthening"})

# Squats
_30_seconds_squats = create_exercise("Squats", duration=30, tags={"strengthening"})
_60_seconds_squats = create_exercise("Squats", duration=60, tags={"strengthening"})

# Squats
_30_seconds_jump_squats = create_exercise("Jump squats", duration=30, tags={"strengthening"})
_60_seconds_jump_squats = create_exercise("Jump squats", duration=60, tags={"strengthening"})

# Burpees
_30_seconds_burpees = create_exercise("Burpees", duration=30, tags={"strengthening"})
_60_seconds_burpees = create_exercise("Burpees", duration=60, tags={"strengthening"})

# Push-ups
_10_push_up = create_exercise("10 push-ups", duration=60, tags={"warming-up", "strengthening"})
rhythmic_push_up = create_exercise("Push-up", duration=2, tags={"strengthening"})

from typing import Dict, FrozenSet, Set, Optional
import functools
import time
import click
import attr
from progressbar import ProgressBar  # type: ignore
from sportbot.sound import BaseSound, Bell
from sportbot.helpers import classproperty


@attr.s(auto_attribs=True, hash=True, repr=False)
class BaseExercice:
    name: str
    duration: int
    color: str
    silence: bool = False
    stopwatch: int = 0
    tags: FrozenSet[str] = frozenset()
    register: bool = True

    def __attrs_post_init__(self) -> None:
        self.stopwatch = self.duration
        if self.register and not isinstance(self, Waiting):
            known_exercices[self.name] = self

    def __repr__(self):
        if self.stopwatch != self.duration:
            return click.style(f"{self.name} : {self.stopwatch} / {self.duration} seconds", fg=self.color)
        return click.style(f"{self.name} : {self.stopwatch} seconds", fg=self.color)

    @functools.cached_property
    def bell(self):
        return Bell()

    @functools.cached_property
    def sound(self):
        return BaseSound(self.name)

    @classproperty
    def known_tags(cls, obj) -> Set[str]:  # pylint: disable=no-self-argument,no-self-use,unused-argument
        return set().union(*[exercice.tags for exercice in known_exercices.values()])  # type: ignore

    def run(self, prefix: Optional[str] = None, dry=False, pbar: Optional[ProgressBar] = None):
        prefix = prefix if prefix is not None else ''
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


@attr.s(auto_attribs=True, hash=True, repr=False)
class Exercice(BaseExercice):
    color: str = "yellow"


@attr.s(auto_attribs=True, hash=True, repr=False)
class Waiting(BaseExercice):
    color: str = "bright_blue"


@attr.s(auto_attribs=True, hash=True, repr=False)
class Prepare(Waiting):
    name: str = 'Prepare'
    duration: int = 10

    def run(self, prefix: Optional[str] = None, dry=False, pbar: Optional[ProgressBar] = None):
        prefix = prefix if prefix is not None else ''
        if not self.silence:
            self.sound.say(dry=dry)

        while self.stopwatch > 0:
            progression = f"{prefix} : {self}"
            sound_countdown = BaseSound(name=str(self.stopwatch))
            if not self.silence:
                sound_countdown.say(dry=dry)
            if pbar:
                pbar.update(progression=progression)

            if not pbar or dry:
                print(progression)
            self.stopwatch -= 1


@attr.s(auto_attribs=True, hash=True, repr=False)
class Maintain(Waiting):
    name: str = "Maintain"
    duration: int = 2
    silence: bool = True


@attr.s(auto_attribs=True, hash=True, repr=False)
class TheEnd(Waiting):
    name: str = 'THE END'
    duration: int = 5


known_exercices: Dict[str, BaseExercice] = {}


def create_exercice(name: str, duration: int, tags: Optional[Set[str]] = None, silence: bool = False) -> Exercice:
    real_tags: FrozenSet[str] = frozenset(tags) if tags is not None else frozenset()
    return Exercice(name, duration, silence=silence, tags=real_tags)  # type: ignore


# SIMPLE

# Warm-Up
_30_seconds_heels_rise = create_exercice("Heels rise", duration=30, tags={'warming-up'})
_30_seconds_knees_rise = create_exercice("Knees rise", duration=30, tags={'warming-up'})
_30_seconds_heels_to_buttocks = create_exercice("Heels to buttocks", duration=30, tags={'warming-up'})

# Jumping jacks
_30_seconds_jumping_jacks = create_exercice("Jumping jacks", duration=30, tags={'warming-up', 'strengthening'})
_60_seconds_jumping_jacks = create_exercice("Jumping jacks", duration=60, tags={'warming-up', 'strengthening'})

# Lunges
_30_seconds_forward_lunges = create_exercice("Forward lunges", duration=30, tags={'warming-up', 'strengthening'})
_60_seconds_backward_lunges = create_exercice("Backward lunges", duration=60, tags={'warming-up', 'strengthening'})

# Alternate lunges
_30_seconds_alternate_lunges = create_exercice("Alternate lunges", duration=30, tags={'strengthening'})
_60_seconds_alternate_lunges = create_exercice("Alternate lunges", duration=60, tags={'strengthening'})

# Crunchs
_30_seconds_crunchs = create_exercice("Crunchs", duration=30, tags={'strengthening'})
_60_seconds_crunchs = create_exercice("Crunchs", duration=60, tags={'strengthening'})

# Twists
_30_seconds_twists = create_exercice("Twists", duration=30, tags={'strengthening'})
_60_seconds_twists = create_exercice("Twists", duration=60, tags={'strengthening'})

# Mountain climbers
_30_seconds_mountain_climber = create_exercice("Mountain climber", duration=30, tags={'warming-up', 'strengthening'})
_60_seconds_mountain_climber = create_exercice("Mountain climber", duration=60, tags={'warming-up', 'strengthening'})

# Plank
_30_seconds_plank = create_exercice("Plank", duration=30, tags={'strengthening'})
_60_seconds_plank = create_exercice("Plank", duration=60, tags={'strengthening'})

# Chair
_30_seconds_chair = create_exercice("Chair", duration=30, tags={'strengthening'})
_60_seconds_chair = create_exercice("Chair", duration=60, tags={'strengthening'})

# Squats
_30_seconds_squats = create_exercice("Squats", duration=30, tags={'strengthening'})
_60_seconds_squats = create_exercice("Squats", duration=60, tags={'strengthening'})

# Squats
_30_seconds_jump_squats = create_exercice("Jump squats", duration=30, tags={'strengthening'})
_60_seconds_jump_squats = create_exercice("Jump squats", duration=60, tags={'strengthening'})

# Burpees
_30_seconds_burpees = create_exercice("Burpees", duration=30, tags={'strengthening'})
_60_seconds_burpees = create_exercice("Burpees", duration=60, tags={'strengthening'})

# Push-ups
_10_push_up = create_exercice("10 push-ups", duration=60, tags={'warming-up', 'strengthening'})
rhythmic_push_up = create_exercice("Push-up", duration=2, tags={'strengthening'})

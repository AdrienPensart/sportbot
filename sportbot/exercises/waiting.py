import time
from dataclasses import dataclass, field

from beartype import beartype
from progressbar import ProgressBar

from sportbot.exercises import BaseWaiting, Exercise
from sportbot.exercises.tag import Tag
from sportbot.sound import BaseSound


@beartype
@dataclass(repr=False)
class Waiting(BaseWaiting):
    name: str = "Waiting"
    color: str = "bright_blue"
    tags: frozenset[Tag] = frozenset({Tag.WAITING})
    exercises: list[Exercise] = field(default_factory=lambda: [])


@beartype
@dataclass(repr=False)
class Prepare(Waiting):
    name: str = "Prepare"
    duration: int = 10

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


@beartype
@dataclass(repr=False)
class Rest(Waiting):
    name: str = "Rest"
    color: str = "green"


# RESTS
_15s_rest = Rest(duration=15)
_30s_rest = Rest(duration=30)
_45s_rest = Rest(duration=45)
_60s_rest = _1mn_rest = Rest(duration=60)
_120s_rest = _2mn_rest = Rest(duration=120)
_5mn_rest = Rest(duration=5 * 60)

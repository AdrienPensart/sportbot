import time
from dataclasses import dataclass

from beartype import beartype
from progressbar import ProgressBar

from sportbot.exercise import BaseWaiting
from sportbot.sound import BaseSound
from sportbot.tag import Tag


@beartype
@dataclass(repr=False)
class Waiting(BaseWaiting):
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
_15_seconds_rest = Rest(duration=15)
_30_seconds_rest = Rest(duration=30)
_45_seconds_rest = Rest(duration=45)
_60_seconds_rest = _1_minute_rest = Rest(duration=60)
_120_seconds_rest = _2_minutes_rest = Rest(duration=120)
_5_minutes_rest = Rest(duration=5 * 60)

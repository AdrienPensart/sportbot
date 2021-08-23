# type: ignore
# bug: https://github.com/python/mypy/issues/8625
from typing import FrozenSet
import functools
import attr
from sportbot.helpers import flatten
from sportbot.sound import TempSound
from sportbot.sequence import Sequence, RestSequence, TheEndSequence
from sportbot.training import Training
from sportbot.exercice import Exercice, Prepare
from sportbot.rest import _1_minute_rest


@attr.s(auto_attribs=True, repr=False)
class Boxing(Exercice):
    color: str = "red"
    tags: FrozenSet[str] = frozenset({"boxing"})

    @functools.cached_property
    def sound(self):
        return TempSound(self.name)


@attr.s(auto_attribs=True, repr=False)
class BoxingSequence(Sequence):
    tags: FrozenSet[str] = frozenset({"boxing"})


@attr.s(auto_attribs=True, repr=False)
class BoxingTraining(Training):
    name: str = "boxing-training"
    description: str = "Boxing Training"


# Kicks
_30_seconds_jab_cross = Boxing("Jab/Cross", duration=30)
_60_seconds_jab_cross = _1_minute_jab_cross = Boxing("Jab/Cross", duration=60)

_30_seconds_uppercuts = Boxing("Left/right uppercuts", duration=30)
_60_seconds_uppercuts = _1_minute_uppercuts = Boxing("Left/right uppercuts", duration=60)

_30_seconds_hooks = Boxing("Left/right hooks", duration=30)
_60_seconds_hooks = _1_minute_hooks = Boxing("Left/right hooks", duration=60)

_30_seconds_knee_kicks = Boxing("Knee kicks", duration=30)
_60_seconds_knee_kicks = _1_minute_knee_kicks = Boxing("Knee kicks", duration=60)

# Boxing
_2_minutes_shadow_boxing = Boxing("Shadow boxing", duration=120)
_3_minutes_shadow_boxing = Boxing("Shadow boxing", duration=180)

_2_minutes_double_ended_bag_boxing = Boxing("Double-ended bag boxing", duration=120)
_3_minutes_double_ended_bag_boxing = Boxing("Double-ended bag boxing", duration=180)

boxing_training = BoxingTraining(
    sequences=tuple([
        BoxingSequence(
            name="12-rounds-2-minutes-shadow-boxing",
            description="12 rounds of 2 minutes shadow boxing with 1 minute rest in between",
            exercices=flatten(
                Prepare(),
                Sequence.rounds(12, _2_minutes_shadow_boxing, _1_minute_rest).exercices,
            ),
        ),
        RestSequence(),
        BoxingSequence(
            name="12-double-ended-bag-boxing-rounds-2-minutes",
            description="12 rounds of 2 minutes double ended bag with 1 minute rest in between",
            exercices=flatten(
                Prepare(),
                Sequence.rounds(12, _2_minutes_double_ended_bag_boxing, _1_minute_rest).exercices,
            ),
        ),
        TheEndSequence(),
    ]),
)

# type: ignore
# bug: https://github.com/python/mypy/issues/8625
from typing import FrozenSet
import attr
from sportbot.helpers import create_rounds, flatten
from sportbot.sequence import Sequence
from sportbot.sequences import Sequences
from sportbot.exercice import Exercice, prepare, the_end
from sportbot.rest import _1_minute_rest


@attr.s(auto_attribs=True, hash=True, repr=False)
class Boxing(Exercice):
    color: str = "red"
    tags: FrozenSet[str] = frozenset({"boxing"})


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

boxing_training = Sequences([
    Sequence(
        name="12_rounds_2_minutes_shadow_boxing",
        description="12 rounds of 2 minutes shadow boxing with 1 minute rest in between",
        exercices=flatten(
            prepare,
            create_rounds(12, _2_minutes_shadow_boxing, _1_minute_rest),
            the_end,
        ),
        tags={"boxing"},
    ),
    Sequence(
        name="12_double_ended_bag_boxing_rounds_2_minutes",
        description="12 rounds of 2 minutes double ended bag with 1 minute rest in between",
        exercices=flatten(
            prepare,
            create_rounds(12, _2_minutes_double_ended_bag_boxing, _1_minute_rest),
            the_end,
        ),
        tags={"boxing"},
    ),
])

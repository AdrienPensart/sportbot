from dataclasses import dataclass
from enum import auto, IntEnum, StrEnum
from functools import cached_property

from beartype import beartype

from sportbot.exercises import Exercise
from sportbot.exercises.helpers import flatten
from sportbot.exercises.sequence import Sequence
from sportbot.exercises.tag import Tag
from sportbot.exercises.training import Training
from sportbot.exercises.waiting import Prepare, TheEnd, _1mn_rest, _5mn_rest
from sportbot.sound import TempSound


@beartype
@dataclass(repr=False)
class Boxing(Exercise):
    name: str = "Boxing"
    color: str = "red"
    tags: frozenset[Tag] = frozenset({Tag.BOXING})

    @cached_property
    def sound(self) -> TempSound:
        return TempSound(self.name)


@beartype
@dataclass(repr=False)
class JumpRope(Exercise):
    name: str = "Jump Rope"
    color: str = "yellow"
    tags: frozenset[Tag] = frozenset({Tag.BOXING, Tag.WARM_UP})


@beartype
@dataclass(repr=False)
class BoxingTraining(Training):
    name: str
    description: str = "Boxing Training"


@beartype
class Bag(StrEnum):
    HEAVY = auto()
    DOUBLE_ENDED = auto()
    SPEED = auto()


@beartype
class Blow(IntEnum):
    JAB = 1
    CROSS = 2
    LEAD_HOOK = 3
    REAR_UPPERCUT = 4
    LEAD_UPPERCUT = 5
    REAR_HOOK = 6


@beartype
class Dodge(IntEnum):
    SLIP_LEFT = 1
    SLIP_RIGHT = 2
    ROLL_LEFT = 3
    ROLL_RIGHT = 4
    STEP_BACK = 5
    BLOCK = 6
    PARRY = 7
    PULL = 8


Combination = list[Blow | Dodge]

# jab / cross
_1_1 = double_jab = Combination([Blow.JAB, Blow.JAB])
_1_1_2 = double_jab_cross = Combination([Blow.JAB, Blow.JAB, Blow.CROSS])
_1_1_1 = triple_jab = Combination([Blow.JAB, Blow.JAB, Blow.JAB])
_1_2 = jab_cross = Combination([Blow.JAB, Blow.CROSS])
_1_2_1 = jab_cross_jab = Combination([Blow.JAB, Blow.CROSS, Blow.JAB])
_1_2_1_2 = jab_cross_jab_cross = Combination([Blow.JAB, Blow.CROSS, Blow.JAB, Blow.CROSS])
_2_1 = cross_jab = Combination([Blow.CROSS, Blow.JAB])

# hooks
_3_6 = lead_hook_rear_hook = Combination([Blow.LEAD_HOOK, Blow.REAR_HOOK])
_1_2_3 = one_two_three = jab_cross_lead_hook = Combination([Blow.JAB, Blow.CROSS, Blow.LEAD_HOOK])
_1_2_3_4 = one_two_three_two = jab_cross_lead_hook_cross = Combination([Blow.JAB, Blow.CROSS, Blow.LEAD_HOOK, Blow.CROSS])
_1_6 = jab_right_hook = Combination([Blow.JAB, Blow.REAR_HOOK])
_2_3 = cross_lead_hook = Combination([Blow.CROSS, Blow.LEAD_HOOK])
_2_3_2 = cross_lead_hook_cross = Combination([Blow.CROSS, Blow.LEAD_HOOK, Blow.CROSS])

# uppercuts
_5_2 = lead_uppercut_cross = Combination([Blow.LEAD_UPPERCUT, Blow.CROSS])
_5_2_3 = lead_uppercut_cross_lead_hook = Combination([Blow.LEAD_UPPERCUT, Blow.CROSS])
_4_3 = right_uppercut_lead_hook = Combination([Blow.REAR_UPPERCUT, Blow.LEAD_HOOK])
_1_2_5 = jab_cross_lead_uppercut = Combination([Blow.JAB, Blow.CROSS, Blow.LEAD_UPPERCUT])
_1_2_5_2 = jab_cross_lead_uppercut_cross = Combination([Blow.JAB, Blow.CROSS, Blow.LEAD_UPPERCUT, Blow.CROSS])
_5_4_3 = lead_uppercut_rear_uppercut_lead_hook = Combination([Blow.LEAD_UPPERCUT, Blow.REAR_UPPERCUT, Blow.LEAD_HOOK])
_1_4_3 = jab_rear_uppercut_lead_hook = Combination([Blow.JAB, Blow.REAR_UPPERCUT, Blow.LEAD_HOOK])
_2_3_4 = cross_lead_hook_rear_uppercut = Combination([Blow.CROSS, Blow.LEAD_HOOK, Blow.REAR_UPPERCUT])

# Jump rope
_30s_jump_rope = JumpRope(duration=30)
_60s_jump_rope = _1mn_jump_rope = JumpRope(duration=60)
_2mn_jump_rope = JumpRope(duration=120)
_5mn_jump_rope = JumpRope(duration=300)
_10mn_jump_rope = JumpRope(duration=600)

# Kicks
_15s_jab_cross = Boxing("Jab/Cross", duration=15)
_30s_jab_cross = Boxing("Jab/Cross", duration=30)
_60s_jab_cross = _1mn_jab_cross = Boxing("Jab/Cross", duration=60)

_15s_uppercuts = Boxing("Left/right uppercuts", duration=15)
_30s_uppercuts = Boxing("Left/right uppercuts", duration=30)
_60s_uppercuts = _1mn_uppercuts = Boxing("Left/right uppercuts", duration=60)

_15s_hooks = Boxing("Left/right hooks", duration=15)
_30s_hooks = Boxing("Left/right hooks", duration=30)
_60s_hooks = _1mn_hooks = Boxing("Left/right hooks", duration=60)

_15s_knee_kicks = Boxing("Knee kicks", duration=15)
_30s_knee_kicks = Boxing("Knee kicks", duration=30)
_60s_knee_kicks = _1mn_knee_kicks = Boxing("Knee kicks", duration=60)

# Boxing
_60s_boxing = _1mn_boxing = Boxing("Boxing", duration=60)
_2mn_boxing = Boxing("Boxing", duration=120)
_3mn_boxing = Boxing("Boxing", duration=180)

_60s_shadow_boxing = _1mn_shadow_boxing = Boxing("Shadow boxing", duration=60)
_2mn_shadow_boxing = Boxing("Shadow boxing", duration=120)
_3mu_shadow_boxing = Boxing("Shadow boxing", duration=180)

_60s_heavy_bag = _1mn_heavy_bag = Boxing("Heavy bag", duration=60)
_2mn_heavy_bag = Boxing("Heavy bag", duration=120)
_3mn_heavy_bag = Boxing("Heavy bag", duration=180)

_60s_speed_bag = _1mn_heavy_bag = Boxing("Speed bag", duration=60)
_2mn_speed_bag = Boxing("Speed bag", duration=120)
_3mn_speed_bag = Boxing("Speed bag", duration=180)

_60s_double_ended_bag = _1mn_double_ended_bag = Boxing("Double-ended bag", duration=60)
_2mn_double_ended_bag = Boxing("Double-ended bag", duration=120)
_3mn_double_ended_bag = Boxing("Double-ended bag", duration=180)

BoxingTraining(
    name="Shadow & double-ended bag",
    sequences=tuple(
        [
            Prepare(),
            Sequence(
                name="6-rounds-2-minutes-shadow-boxing",
                description="6 rounds of 2 minutes shadow boxing with 1 minute rest in between",
                exercises=Sequence.rounds(6, _2mn_shadow_boxing, _1mn_rest).exercises,
            ),
            _5mn_rest,
            Sequence(
                name="6-double-ended-bag-boxing-rounds-2-minutes",
                description="6 rounds of 2 minutes double ended bag with 1 minute rest in between",
                exercises=Sequence.rounds(6, _2mn_double_ended_bag, _1mn_rest).exercises,
            ),
            TheEnd(),
        ],
    ),
)

BoxingTraining(
    name="Shadow & heavy bag",
    sequences=tuple(
        [
            Prepare(),
            Sequence(
                name="6-rounds-2-minutes-shadow-boxing",
                description="6 rounds of 2 minutes shadow boxing with 1 minute rest in between",
                exercises=Sequence.rounds(6, _2mn_shadow_boxing, _1mn_rest).exercises,
            ),
            _5mn_rest,
            Sequence(
                name="6-heavy-bag-boxing-rounds-2-minutes",
                description="6 rounds of 2 minutes heavy bag with 1 minute rest in between",
                exercises=Sequence.rounds(6, _2mn_heavy_bag, _1mn_rest).exercises,
            ),
            TheEnd(),
        ],
    ),
)

BoxingTraining(
    name="Shadow, double ended bag and heavy bag",
    sequences=tuple(
        [
            Prepare(),
            Sequence(
                name="4-rounds-2-minutes-shadow-boxing",
                description="4 rounds of 2 minutes shadow boxing with 1 minute rest in between",
                exercises=Sequence.rounds(4, _2mn_shadow_boxing, _1mn_rest).exercises,
            ),
            _5mn_rest,
            Sequence(
                name="4-double-ended-bag-boxing-rounds-2-minutes",
                description="4 rounds of 2 minutes double ended bag with 1 minute rest in between",
                exercises=Sequence.rounds(4, _2mn_double_ended_bag, _1mn_rest).exercises,
            ),
            _5mn_rest,
            Sequence(
                name="4-heavy-bag-boxing-rounds-2-minutes",
                description="4 rounds of 2 minutes double ended bag with 1 minute rest in between",
                exercises=Sequence.rounds(4, _2mn_heavy_bag, _1mn_rest).exercises,
            ),
            TheEnd(),
        ],
    ),
)

BoxingTraining(
    name="Olympic Boxing Fight",
    sequences=tuple(
        [
            Prepare(duration=60),
            Sequence(
                name="12-rounds-2-minutes",
                description="12 rounds of 2 minutes boxing with 1 minute rest in between",
                exercises=flatten(
                    Sequence.rounds(12, _2mn_boxing, _1mn_rest).exercises,
                ),
            ),
            TheEnd(),
        ],
    ),
)

BoxingTraining(
    name="Professional Boxing Fight",
    sequences=tuple(
        [
            Prepare(duration=60),
            Sequence(
                name="12-rounds-3-minutes",
                description="12 rounds of 3 minutes boxing with 1 minute rest in between",
                exercises=flatten(
                    Sequence.rounds(12, _3mn_boxing, _1mn_rest).exercises,
                ),
            ),
            TheEnd(),
        ],
    ),
)

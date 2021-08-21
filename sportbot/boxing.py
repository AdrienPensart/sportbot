# type: ignore
# bug: https://github.com/python/mypy/issues/8625
from sportbot.helpers import rounds, flatten
from sportbot.sequence import Sequence
from sportbot.sequences import Sequences
from sportbot.exercices import (
    prepare,
    the_end,
    _1_minute_rest,
    _2_minutes_shadow_boxing,
    _2_minutes_double_ended_bag_boxing,
)


boxing_training = Sequences([
    Sequence(
        name="12_rounds_2_minutes_shadow_boxing",
        description="12 rounds of 2 minutes shadow boxing with 1 minute rest in between",
        exercices=flatten(
            prepare,
            rounds(12, _2_minutes_shadow_boxing, _1_minute_rest),
            the_end,
        ),
        tags={"boxing"},
    ),
    Sequence(
        name="12_double_ended_bag_boxing_rounds_2_minutes",
        description="12 rounds of 2 minutes double ended bag with 1 minute rest in between",
        exercices=flatten(
            prepare,
            rounds(12, _2_minutes_double_ended_bag_boxing, _1_minute_rest),
            the_end,
        ),
        tags={"boxing"},
    ),
])

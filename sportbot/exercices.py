# type: ignore
# bug: https://github.com/python/mypy/issues/8625
from sportbot.helpers import rounds
from sportbot.exercice import Exercice, Rest, Waiting, Boxing

prepare = Waiting("Prepare", duration=20)
the_end = Waiting("THE END", duration=5)
maintain = Exercice("Maintain", duration=1, silence=True)

# RESTS
_15_seconds_rest = Rest(duration=15)
_30_seconds_rest = Rest(duration=30)
_45_seconds_rest = Rest(duration=45)
_60_seconds_rest = _1_minute_rest = Rest(duration=60)
_120_seconds_rest = _2_minutes_rest = Rest(duration=120)

# SIMPLE

# Warm-Up
_30_seconds_heels_rise = Exercice("Heels rise", duration=30, tags={'warming-up'})
_30_seconds_knees_rise = Exercice("Knees rise", duration=30, tags={'warming-up'})
_30_seconds_heels_to_buttocks = Exercice("Heels to buttocks", duration=30, tags={'warming-up'})

# Jumping jacks
_30_seconds_jumping_jacks = Exercice("Jumping jacks", duration=30, tags={'warming-up', 'strengthening'})
_60_seconds_jumping_jacks = Exercice("Jumping jacks", duration=60, tags={'warming-up', 'strengthening'})

# Lunges
_30_seconds_forward_lunges = Exercice("Forward lunges", duration=30, tags={'warming-up', 'strengthening'})
_60_seconds_backward_lunges = Exercice("Backward lunges", duration=60, tags={'warming-up', 'strengthening'})

# Alternate lunges
_30_seconds_alternate_lunges = Exercice("Alternate lunges", duration=30, tags={'strengthening'})
_60_seconds_alternate_lunges = Exercice("Alternate lunges", duration=60, tags={'strengthening'})

# Crunchs
_30_seconds_crunchs = Exercice("Crunchs", duration=30, tags={'strengthening'})
_60_seconds_crunchs = Exercice("Crunchs", duration=60, tags={'strengthening'})

# Twists
_30_seconds_twists = Exercice("Twists", duration=30, tags={'strengthening'})
_60_seconds_twists = Exercice("Twists", duration=60, tags={'strengthening'})

# Mountain climbers
_30_seconds_mountain_climber = Exercice("Mountain climber", duration=30, tags={'warming-up', 'strengthening'})
_60_seconds_mountain_climber = Exercice("Mountain climber", duration=60, tags={'warming-up', 'strengthening'})

# Plank
_30_seconds_plank = Exercice("Plank", duration=30, tags={'strengthening'})
_60_seconds_plank = Exercice("Plank", duration=60, tags={'strengthening'})

# Chair
_30_seconds_chair = Exercice("Chair", duration=30, tags={'strengthening'})
_60_seconds_chair = Exercice("Chair", duration=60, tags={'strengthening'})

# Squats
_30_seconds_squats = Exercice("Squats", duration=30, tags={'strengthening'})
_60_seconds_squats = Exercice("Squats", duration=60, tags={'strengthening'})

# Squats
_30_seconds_jump_squats = Exercice("Jump squats", duration=30, tags={'strengthening'})
_60_seconds_jump_squats = Exercice("Jump squats", duration=60, tags={'strengthening'})

# Burpees
_30_seconds_burpees = Exercice("Burpees", duration=30, tags={'strengthening'})
_60_seconds_burpees = Exercice("Burpees", duration=60, tags={'strengthening'})

# Push-ups
_10_push_up = Exercice("10 push-ups", duration=60, tags={'warming-up', 'strengthening'})
rhythmic_push_up = Exercice("Push-up", duration=2, tags={'strengthening'})
_10_rhythmic_push_up = rounds(10, rhythmic_push_up, maintain)

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

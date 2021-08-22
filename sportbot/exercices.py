# type: ignore
# bug: https://github.com/python/mypy/issues/8625
from sportbot.helpers import create_rounds
from sportbot.exercice import Exercice

maintain = Exercice("Maintain", duration=1, silence=True)

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
_10_rhythmic_push_up = create_rounds(10, rhythmic_push_up, maintain)

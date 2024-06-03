from sportbot.exercises import create_exercise
from sportbot.exercises.tag import Tag

# SIMPLE

# Warm-Up
_30s_heels_rise = create_exercise("Heels rise", duration=30, tags={Tag.EASY, Tag.WARM_UP})
_30s_knees_rise = create_exercise("Knees rise", duration=30, tags={Tag.EASY, Tag.WARM_UP})
_30s_heels_to_buttocks = create_exercise("Heels to buttocks", duration=30, tags={Tag.EASY, Tag.WARM_UP})

# Jumping jacks
_30s_jumping_jacks = create_exercise("Jumping jacks", duration=30, tags={Tag.EASY, Tag.FULL_BODY, Tag.DYNAMIC, Tag.WARM_UP, Tag.STRENGTHENING})
_60s_jumping_jacks = create_exercise("Jumping jacks", duration=60, tags={Tag.MEDIUM, Tag.FULL_BODY, Tag.DYNAMIC, Tag.WARM_UP, Tag.STRENGTHENING})

# Lunges
_30s_forward_lunges = create_exercise("Forward lunges", duration=30, tags={Tag.EASY, Tag.DYNAMIC, Tag.WARM_UP, Tag.STRENGTHENING})
_60s_backward_lunges = create_exercise("Backward lunges", duration=60, tags={Tag.MEDIUM, Tag.DYNAMIC, Tag.WARM_UP, Tag.STRENGTHENING})

# Alternate lunges
_30s_alternate_lunges = create_exercise("Alternate lunges", duration=30, tags={Tag.EASY, Tag.DYNAMIC, Tag.STRENGTHENING})
_60s_alternate_lunges = create_exercise("Alternate lunges", duration=60, tags={Tag.MEDIUM, Tag.DYNAMIC, Tag.STRENGTHENING})

# Twists
_30s_twists = create_exercise("Russian twists", duration=30, tags={Tag.EASY, Tag.DYNAMIC, Tag.ABS, Tag.STRENGTHENING})
_60s_twists = create_exercise("Russian twists", duration=60, tags={Tag.MEDIUM, Tag.DYNAMIC, Tag.ABS, Tag.STRENGTHENING})

# Mountain climbers
_30s_mountain_climber = create_exercise("Mountain climber", duration=30, tags={Tag.EASY, Tag.DYNAMIC, Tag.WARM_UP, Tag.STRENGTHENING, Tag.ABS})
_60s_mountain_climber = create_exercise("Mountain climber", duration=60, tags={Tag.MEDIUM, Tag.DYNAMIC, Tag.WARM_UP, Tag.STRENGTHENING, Tag.ABS})

# Plank
_30s_plank = create_exercise("Plank", duration=30, tags={Tag.EASY, Tag.STATIONARY, Tag.ABS, Tag.STRENGTHENING})
_60s_plank = create_exercise("Plank", duration=60, tags={Tag.MEDIUM, Tag.STATIONARY, Tag.ABS, Tag.STRENGTHENING})
_120s_plank = create_exercise("Plank", duration=120, tags={Tag.HARD, Tag.STATIONARY, Tag.ABS, Tag.STRENGTHENING})

# Chair
_30s_chair = create_exercise("Chair", duration=30, tags={Tag.EASY, Tag.STATIONARY, Tag.STRENGTHENING})
_60s_chair = create_exercise("Chair", duration=60, tags={Tag.MEDIUM, Tag.STATIONARY, Tag.STRENGTHENING})

# Squats
_30s_squats = create_exercise("Squats", duration=30, tags={Tag.EASY, Tag.DYNAMIC, Tag.STRENGTHENING})
_60s_squats = create_exercise("Squats", duration=60, tags={Tag.MEDIUM, Tag.DYNAMIC, Tag.STRENGTHENING})

# Jump squats
_30s_jump_squats = create_exercise("Jump squats", duration=30, tags={Tag.EASY, Tag.DYNAMIC, Tag.STRENGTHENING})
_60s_jump_squats = create_exercise("Jump squats", duration=60, tags={Tag.MEDIUM, Tag.DYNAMIC, Tag.STRENGTHENING})

# Burpees
_30s_burpees = create_exercise("Burpees", duration=30, tags={Tag.MEDIUM, Tag.FULL_BODY, Tag.DYNAMIC, Tag.STRENGTHENING})
_60s_burpees = create_exercise("Burpees", duration=60, tags={Tag.MEDIUM, Tag.FULL_BODY, Tag.DYNAMIC, Tag.STRENGTHENING})
_120s_burpees = create_exercise("Burpees", duration=120, tags={Tag.HARD, Tag.FULL_BODY, Tag.DYNAMIC, Tag.STRENGTHENING})

# Push-ups
_5_push_up = create_exercise("5 push-ups", duration=30, tags={Tag.EASY, Tag.DYNAMIC, Tag.WARM_UP})
_10_push_up = create_exercise("10 push-ups", duration=60, tags={Tag.EASY, Tag.DYNAMIC, Tag.WARM_UP})
_15_push_up = create_exercise("15 push-ups", duration=90, tags={Tag.MEDIUM, Tag.DYNAMIC, Tag.WARM_UP, Tag.STRENGTHENING})
_20_push_up = create_exercise("20 push-ups", duration=120, tags={Tag.MEDIUM, Tag.DYNAMIC, Tag.WARM_UP, Tag.STRENGTHENING})
_25_push_up = create_exercise("25 push-ups", duration=150, tags={Tag.HARD, Tag.DYNAMIC, Tag.WARM_UP, Tag.STRENGTHENING})

# Crunchs
_30s_crunchs = create_exercise("Crunchs", duration=30, tags={Tag.EASY, Tag.DYNAMIC, Tag.ABS, Tag.STRENGTHENING})
_60s_crunchs = create_exercise("Crunchs", duration=60, tags={Tag.MEDIUM, Tag.DYNAMIC, Tag.ABS, Tag.STRENGTHENING})
_120s_crunchs = create_exercise("Crunchs", duration=120, tags={Tag.HARD, Tag.DYNAMIC, Tag.ABS, Tag.STRENGTHENING})

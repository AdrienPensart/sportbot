from sportbot.helpers import flatten, seconds_to_human


class Sequence:
    def __init__(self, exercices):
        self.exercices = exercices
        self.exercices = list(flatten(exercices))

    @property
    def length(self):
        return len(self.exercices)

    @property
    def total_duration(self):
        return sum([exercice.duration for exercice in self.exercices])

    @property
    def human_total_duration(self):
        return seconds_to_human(self.total_duration)

    @property
    def left_stopwatch(self):
        return sum([exercice.stopwatch for exercice in self.exercices])

    @property
    def human_left_stopwatch(self):
        return seconds_to_human(self.left_stopwatch)

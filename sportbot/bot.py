import logging
from asciimatics.screen import Screen
from sportbot.sequence import Sequence
from sportbot.screen import SportScreen
from sportbot.sound import bell

logger = logging.getLogger(__name__)


class Sportbot:
    def __init__(self, exercices):
        self.sequence = Sequence(exercices)

    def run(self):
        def _run(screen):
            sportscreen = SportScreen(screen)
            sportscreen.display(f"{self.sequence.length} exercices, duration : {self.sequence.human_total_duration}")
            for number, exercice in enumerate(self.sequence.exercices):
                exercice.run(number, self.sequence.length, sportscreen)
            bell()

        Screen.wrapper(_run)

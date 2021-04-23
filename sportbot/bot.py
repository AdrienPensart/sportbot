import logging
import time
from asciimatics.screen import Screen
from colorama import Fore
from sportbot.screen import SportScreen
from sportbot.sound import bell

logger = logging.getLogger(__name__)


class Sportbot:
    def __init__(self, sequence):
        self.sequence = sequence

    def run(self, dry=False):
        def _run(screen=None):
            if screen:
                sportscreen = SportScreen(screen)
                sportscreen.display(f"{Fore.BLUE}{self.sequence}{Fore.RESET}")
                time.sleep(5)
            for number, exercice in enumerate(self.sequence.exercices):
                if screen:
                    exercice.run(number, self.sequence.length, sportscreen)
                else:
                    print(exercice)
            bell()

        if not dry:
            Screen.wrapper(_run)
        else:
            _run()

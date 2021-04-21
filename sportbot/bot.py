import logging
import os
import sys
import time
import vlc
from asciimatics.screen import Screen
from sportbot.helpers import flatten, seconds_to_human

logger = logging.getLogger(__name__)


class Sportbot:
    def __init__(self, exercices):
        self.exercices = list(flatten(exercices))
        self.total_duration = sum([exercice.duration for exercice in self.exercices])
        self.instance = vlc.Instance("--vout=dummy --aout=pulse")
        if not self.instance:
            logger.critical('Unable to start VLC instance')
            sys.exit(1)

        self.player = self.instance.media_list_player_new()
        if not self.player:
            logger.critical('Unable to create VLC player')
            return

        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)
        self.bell_path = dir_path + '/bell.wav'

    def bell(self):
        self.player.stop()
        media_list = self.instance.media_list_new([self.bell_path])
        if not media_list:
            logger.critical('Unable to create VLC media list')
            return
        self.player.set_media_list(media_list)
        self.player.play()

    def display(self, screen, msg):
        screen.clear()
        screen.print_at(msg, 0, 0)
        screen.refresh()

    def run(self):
        def _run(screen):
            self.display(screen, f"{len(self.exercices)} exercices, duration : {seconds_to_human(self.total_duration)}")
            time.sleep(2)

            for number, exercice in enumerate(self.exercices):
                self.run_exercice(number, exercice, screen)

            self.bell()

        Screen.wrapper(_run)

    def run_exercice(self, number, exercice, screen):
        if not exercice.silence:
            self.bell()
        while exercice.stopwatch > 0:
            self.display(screen, f"{number}/{len(self.exercices)} : {exercice}")
            exercice.stopwatch -= 1
            time.sleep(1)
            self.player.stop()

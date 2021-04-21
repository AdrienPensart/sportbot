import time
import os
from slugify import slugify
from gtts import gTTS
from colorama import Fore
from sportbot.sound import player, bell, say


def get_tts_path(label):
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    return dir_path + f'/tts/{label}.mp3'


class Exercice:
    def __init__(self, label, duration, silence=False, intensity=10, color=Fore.RESET, tags=None):

        self.tts_path = get_tts_path(slugify(label))
        if not os.path.isfile(self.tts_path):
            tts = gTTS(label)
            tts.save(self.tts_path)

        self.tags = tags if tags is not None else []
        self.intensity = intensity
        self.label = label
        self.duration = duration
        self.stopwatch = duration
        self.color = color
        self.silence = silence

    def __repr__(self):
        return f"{self.color}{self.label} : {self.stopwatch} / {self.duration}{Fore.RESET}"

    def run(self, number, length, sportscreen):
        if not self.silence:
            wait_for = say(self.tts_path)
            time.sleep(wait_for)
            bell()
        while self.stopwatch > 0:
            sportscreen.display(f"{number}/{length} : {self}")
            self.stopwatch -= 1
            time.sleep(1)
            player().stop()

import time
import os
from slugify import slugify
from gtts import gTTS
from colorama import Fore
from sportbot.sound import player, bell, say


def default_tts_path(name):
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    return f'{dir_path}/tts/{name}.mp3'


class Exercice:
    def __init__(self, name, duration, silence=False, color=Fore.RESET, tags=None):
        self.tags = tags if tags is not None else []
        self.name = name
        self.duration = duration
        self.stopwatch = duration
        self.color = color
        self.silence = silence

    def __repr__(self):
        return f"{self.color}{self.name} : {self.stopwatch} / {self.duration}{Fore.RESET}"

    @property
    def tts_path(self):
        slug = slugify(self.name)
        _tts_path = default_tts_path(slug)
        if not os.path.isfile(_tts_path):
            tts = gTTS(self.name)
            _tts_path = f'/tmp/{slug}.mp3'
            tts.save(_tts_path)
        return _tts_path

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

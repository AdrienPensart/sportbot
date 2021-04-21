#!/usr/bin/env python3
import os
import sys
import time
import logging
import collections
import vlc
from colorama import Fore

logger = logging.getLogger(__name__)
logging.getLogger("vlc").setLevel(logging.NOTSET)


def flatten(iterables):
    '''Recursively flatten argument'''
    for element in iterables:
        if isinstance(element, collections.Iterable) and not isinstance(element, (str, bytes)):
            yield from flatten(element)
        else:
            yield element


def joinit(iterable, delimiter):
    it = iter(iterable)
    yield next(it)
    for x in it:
        yield delimiter
        yield x


def intersperse(iterable, delimiter):
    return list(joinit(iterable, delimiter))


def rounds(n, exercice, rest):
    return intersperse([exercice] * n, rest),


class Exercice:
    def __init__(self, label, duration, color=Fore.RESET):
        self.label = label
        self.duration = duration
        self.stopwatch = duration
        self.color = color

    def __repr__(self):
        return f"{self.color}{self.label} : {self.stopwatch} / {self.duration}{Fore.RESET}"


prepare = Exercice("Prepare", 5),
rest = Exercice("Rest", 60, Fore.YELLOW)
shadow_boxing = Exercice("Boxing", 120, Fore.GREEN)

exercices = [
    prepare,
    rounds(12, shadow_boxing, rest),
]


class Sportbot:
    def __init__(self):
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

    def run(self):
        def demo(screen):
            for exercice in flatten(exercices):
                self.bell()
                while exercice.stopwatch > 0:
                    screen.clear()
                    screen.print_at(f"{exercice}", 0, 0)
                    screen.refresh()
                    exercice.stopwatch -= 1
                    time.sleep(1)
            self.bell()

        from asciimatics.screen import Screen
        Screen.wrapper(demo)


def main():
    bot = Sportbot()
    bot.run()

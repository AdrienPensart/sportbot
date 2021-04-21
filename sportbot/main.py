#!/usr/bin/env python3
import datetime
import copy
import os
import sys
import time
import logging
import collections
import vlc
from colorama import Fore
from asciimatics.screen import Screen

logger = logging.getLogger(__name__)
logging.getLogger("vlc").setLevel(logging.NOTSET)


def seconds_to_human(seconds: int) -> str:
    '''Human readable duration from seconds'''
    return str(datetime.timedelta(seconds=seconds))


def flatten(iterables):
    '''Recursively flatten argument'''
    for element in iterables:
        if isinstance(element, collections.Iterable) and not isinstance(element, (str, bytes)):
            yield from flatten(element)
        else:
            yield element


def join_exercices(iterable, rest):
    it = iter(iterable)
    n_round = 1
    total_round = len(iterable)

    first_exercice = next(it)
    first_exercice.label = f"{first_exercice.label} (round {n_round}/{total_round})"

    yield first_exercice
    for next_exercice in it:
        yield rest
        n_round += 1
        next_exercice.label = f"{next_exercice.label} (round {n_round}/{total_round})"
        yield next_exercice


def intersperse(exercices, rest):
    return list(join_exercices(exercices, rest))


def rounds(n, exercice, rest):
    return intersperse([copy.deepcopy(exercice) for _ in range(n)], rest),


class Exercice:
    def __init__(self, label, duration, intensity=10, color=Fore.RESET):
        self.intensity = intensity
        self.label = label
        self.duration = duration
        self.stopwatch = duration
        self.color = color

    def __repr__(self):
        return f"{self.color}{self.label} : {self.stopwatch} / {self.duration}{Fore.RESET}"


prepare = Exercice("Prepare", 5),
one_minute_rest = Exercice("Standard Rest", 60, color=Fore.YELLOW)
two_minutes_rest = Exercice("Long Rest", 120, color=Fore.YELLOW)
shadow_boxing = Exercice("Boxing", 120, color=Fore.GREEN)
jab_cross = Exercice("Jab/Cross", 60, color=Fore.RED)
uppercuts = Exercice("Uppercuts", 60, color=Fore.RED)


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
        self.bell()
        while exercice.stopwatch > 0:
            self.display(screen, f"{number}/{len(self.exercices)} : {exercice}")
            exercice.stopwatch -= 1
            time.sleep(1)
            self.player.stop()


def main():
    exercices = [
        prepare,
        rounds(12, shadow_boxing, one_minute_rest),
        two_minutes_rest,
    ]
    # for exercice in flatten(exercices):
    #     print(exercice)
    bot = Sportbot(exercices)
    bot.run()

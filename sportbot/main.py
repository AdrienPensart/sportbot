#!/usr/bin/env python3
import logging
from colorama import Fore
from sportbot.exercice import Exercice
from sportbot.helpers import rounds
from sportbot.bot import Sportbot

logger = logging.getLogger(__name__)
logging.getLogger("vlc").setLevel(logging.NOTSET)

prepare = Exercice("Prepare", 5),
one_minute_rest = Exercice("Standard Rest", 60, color=Fore.YELLOW)
two_minutes_rest = Exercice("Long Rest", 120, color=Fore.YELLOW)
shadow_boxing = Exercice("Boxing", 120, color=Fore.GREEN)
jab_cross = Exercice("Jab/Cross", 60, color=Fore.RED)
uppercuts = Exercice("Uppercuts", 60, color=Fore.RED)


def main():
    exercices = [
        prepare,
        rounds(12, shadow_boxing, one_minute_rest),
        two_minutes_rest,
    ]
    bot = Sportbot(exercices)
    bot.run()

#!/usr/bin/env python3
import logging
from colorama import Fore
from sportbot.exercice import Exercice
from sportbot.helpers import rounds
from sportbot.bot import Sportbot

logger = logging.getLogger(__name__)
logging.getLogger("vlc").setLevel(logging.NOTSET)

prepare = Exercice("Prepare", 5),
maintain = Exercice("Rest", 1, silence=True, color=Fore.YELLOW)
one_minute_rest = Exercice("Standard Rest", 60, color=Fore.YELLOW)
two_minutes_rest = Exercice("Long Rest", 120, color=Fore.YELLOW)
jab_cross = Exercice("Jab/Cross", 60, color=Fore.RED)
uppercuts = Exercice("Uppercuts", 60, color=Fore.RED)

mountain_climber = Exercice("Mountain climber", 60, color=Fore.RED)
_10_push_up = Exercice("10 push-ups", 60, color=Fore.RED)
rhythmic_push_up = Exercice("Push-up", 2)

shadow_boxing = Exercice("Shadow boxing", 120, color=Fore.GREEN)
double_ended_bag_boxing = Exercice("Double-ended bag boxing", 120, color=Fore.GREEN)

_10_rhythmic_push_up = rounds(10, rhythmic_push_up, maintain)

_12_shadow_boxing_rounds_2_minutes = [
    prepare,
    rounds(12, shadow_boxing, one_minute_rest),
]

_12_double_ended_bag_boxing_rounds_2_minutes = [
    prepare,
    rounds(12, double_ended_bag_boxing, one_minute_rest),
]


def main():
    # bot = Sportbot(_12_shadow_boxing_rounds_2_minutes)
    bot = Sportbot(_10_rhythmic_push_up)
    bot.run()

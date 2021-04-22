#!/usr/bin/env python3
import logging
import click
from colorama import Fore
from click_skeleton import skeleton, doc, backtrace
from sportbot import version
from sportbot.sequence import Sequence
from sportbot.exercice import Exercice
from sportbot.helpers import rounds, flatten
from sportbot.bot import Sportbot

PROG_NAME = "sportbot"
logger = logging.getLogger(__name__)
logging.getLogger("vlc").setLevel(logging.NOTSET)

prepare = Exercice(label="Prepare", duration=5, color=Fore.GREEN)
maintain = Exercice(label="Maintain", duration=1, silence=True, color=Fore.YELLOW)

# RESTS
_15_seconds_rest = Exercice("Rest", duration=15, color=Fore.YELLOW, tags=['rest'])
_30_seconds_rest = Exercice("Rest", duration=30, color=Fore.YELLOW, tags=['rest'])
_45_seconds_rest = Exercice("Rest", duration=45, color=Fore.YELLOW, tags=['rest'])
_60_seconds_rest = _1_minute_rest = Exercice("Rest", duration=60, color=Fore.YELLOW, tags=['rest'])
_120_seconds_rest = _2_minutes_rest = Exercice("Rest", duration=120, color=Fore.YELLOW, tags=['rest'])

# SIMPLE

# Warm-Up
_30_seconds_heels_rise = Exercice("Heels rise", duration=30, color=Fore.GREEN, tags=['warming-up'])
_30_seconds_knees_rise = Exercice("Knees rise", duration=30, color=Fore.GREEN, tags=['warming-up'])
_30_seconds_heels_to_buttocks = Exercice("Heels to buttocks", duration=30, color=Fore.GREEN, tags=['warming-up'])

# Jumping jacks
_30_seconds_jumping_jacks = Exercice("Jumping jacks", duration=30, color=Fore.YELLOW, tags=['warming-up', 'strengthening'])
_60_seconds_jumping_jacks = Exercice("Jumping jacks", duration=60, color=Fore.YELLOW, tags=['warming-up', 'strengthening'])

# Lunges
_30_seconds_forward_lunges = Exercice("Forward lunges", duration=30, color=Fore.YELLOW, tags=['warming-up', 'strengthening'])
_60_seconds_backward_lunges = Exercice("Backward lunges", duration=60, color=Fore.YELLOW, tags=['warming-up', 'strengthening'])

# Alternate lunges
_30_seconds_alternate_lunges = Exercice("Alternate lunges", duration=30, color=Fore.YELLOW, tags=['strengthening'])
_60_seconds_alternate_lunges = Exercice("Alternate lunges", duration=60, color=Fore.YELLOW, tags=['strengthening'])

# Crunchs
_30_seconds_crunchs = Exercice("Crunchs", duration=30, color=Fore.YELLOW, tags=['strengthening'])
_60_seconds_crunchs = Exercice("Crunchs", duration=60, color=Fore.YELLOW, tags=['strengthening'])

# Twists
_30_seconds_twists = Exercice("Twists", duration=30, color=Fore.YELLOW, tags=['strengthening'])
_60_seconds_twists = Exercice("Twists", duration=60, color=Fore.YELLOW, tags=['strengthening'])

# Mountain climbers
_30_seconds_mountain_climber = Exercice("Mountain climber", duration=30, color=Fore.YELLOW, tags=['warming-up', 'strengthening'])
_60_seconds_mountain_climber = Exercice("Mountain climber", duration=60, color=Fore.YELLOW, tags=['warming-up', 'strengthening'])

# Plank
_30_seconds_plank = Exercice("Plank", duration=30, color=Fore.YELLOW, tags=['strengthening'])
_60_seconds_plank = Exercice("Plank", duration=60, color=Fore.YELLOW, tags=['strengthening'])

# Chair
_30_seconds_chair = Exercice("Chair", duration=30, color=Fore.YELLOW, tags=['strengthening'])
_60_seconds_chair = Exercice("Chair", duration=60, color=Fore.YELLOW, tags=['strengthening'])

# Squats
_30_seconds_squats = Exercice("Squats", duration=30, color=Fore.YELLOW, tags=['strengthening'])
_60_seconds_squats = Exercice("Squats", duration=60, color=Fore.YELLOW, tags=['strengthening'])

# Squats
_30_seconds_jump_squats = Exercice("Jump squats", duration=30, color=Fore.YELLOW, tags=['strengthening'])
_60_seconds_jump_squats = Exercice("Jump squats", duration=60, color=Fore.YELLOW, tags=['strengthening'])

# Burpees
_30_seconds_burpees = Exercice("Burpees", duration=30, color=Fore.YELLOW, tags=['strengthening'])
_60_seconds_burpees = Exercice("Burpees", duration=60, color=Fore.YELLOW, tags=['strengthening'])

# Push-ups
_10_push_up = Exercice("10 push-ups", duration=60, color=Fore.YELLOW, tags=['warming-up', 'strengthening'])
rhythmic_push_up = Exercice("Push-up", duration=2, tags=['strengthening'])
_10_rhythmic_push_up = rounds(10, rhythmic_push_up, maintain)

# Kicks
_30_seconds_jab_cross = Exercice("Jab/Cross", duration=30, color=Fore.YELLOW, tags=['boxing'])
_60_seconds_jab_cross = _1_minute_jab_cross = Exercice("Jab/Cross", duration=60, color=Fore.YELLOW, tags=['boxing'])

_30_seconds_uppercuts = Exercice("Left/right uppercuts", duration=30, color=Fore.YELLOW, tags=['boxing'])
_60_seconds_uppercuts = _1_minute_uppercuts = Exercice("Left/right uppercuts", duration=60, color=Fore.YELLOW, tags=['boxing'])

_30_seconds_hooks = Exercice("Left/right hooks", duration=30, color=Fore.YELLOW, tags=['boxing'])
_60_seconds_hooks = _1_minute_hooks = Exercice("Left/right hooks", duration=60, color=Fore.YELLOW, tags=['boxing'])

_30_seconds_knee_kicks = Exercice("Knee kicks", duration=30, color=Fore.YELLOW, tags=['boxing'])
_60_seconds_knee_kicks = _1_minute_knee_kicks = Exercice("Knee kicks", duration=60, color=Fore.YELLOW, tags=['boxing'])

# Boxing
_2_minutes_shadow_boxing = Exercice("Shadow boxing", duration=120, color=Fore.RED, tags=['boxing'])
_3_minutes_shadow_boxing = Exercice("Shadow boxing", duration=180, color=Fore.RED, tags=['boxing'])

_2_minutes_double_ended_bag_boxing = Exercice("Double-ended bag boxing", duration=120, color=Fore.RED, tags=['boxing'])
_3_minutes_double_ended_bag_boxing = Exercice("Double-ended bag boxing", duration=180, color=Fore.RED, tags=['boxing'])


backtrace.hook(
    reverse=False,
    align=True,
    strip_path=False,
    enable_on_envvar_only=False,
    on_tty=False,
    conservative=False,
)

sequences = [
    Sequence(
        name="12_rounds_2_minutes_shadow_boxing",
        exercices=flatten(
            prepare,
            rounds(12, _2_minutes_shadow_boxing, _60_seconds_rest),
        ),
        tags=["boxing"],
    ),
    Sequence(
        name="12_double_ended_bag_boxing_rounds_2_minutes",
        exercices=flatten(
            prepare,
            rounds(12, _2_minutes_double_ended_bag_boxing, _1_minute_rest),
        ),
        tags=["boxing"],
    ),
]


@skeleton(name=PROG_NAME, version=version.__version__, auto_envvar_prefix='SP')
def cli():
    """SportBot."""


@cli.command('sequences', help='List available sequences')
@click.option('--tag', 'tags', help="Tag filter", multiple=True)
def _sequences(tags):
    for sequence in sequences:
        if tags:
            for tag in tags:
                if tag in sequence.tags:
                    print(sequence)
        else:
            print(sequence)


@cli.command(help='List available tags')
def tags():
    unique_tags = set()
    for sequence in sequences:
        unique_tags.update(sequence.tags)
    for unique_tag in unique_tags:
        print(unique_tag)


@cli.command(help='Start sequence')
@click.argument('name')
def start(name):
    for sequence in sequences:
        if name == sequence.name:
            bot = Sportbot(sequence)
            bot.run()
            return
    print("Unknown sequence")


@cli.command(short_help='Generates a README.rst', aliases=['doc'])
@click.pass_context
@click.option('--output', help='README output format', type=click.Choice(['rst', 'markdown']), default='rst', show_default=True)
def readme(ctx, output):
    '''Generates a complete readme'''
    doc.readme(cli, ctx.obj.prog_name, ctx.obj.context_settings, output)


def main(**kwargs):
    return cli.main(prog_name=PROG_NAME, **kwargs)

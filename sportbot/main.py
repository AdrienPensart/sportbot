#!/usr/bin/env python3
from pathlib import Path
import sys
import logging
import click
import colorlog  # type: ignore
import progressbar  # type: ignore
from click_skeleton import skeleton, doc, backtrace, AdvancedGroup
from sportbot import version
from sportbot.sound import TempSound
from sportbot.training import known_trainings
from sportbot.sequence import known_sequences, Sequence, create_sequence
from sportbot.exercice import known_exercices, Exercice, Prepare, TheEnd
from sportbot.boxing import Boxing  # type: ignore
from sportbot.rest import Rest
from sportbot.helpers import flatten, Py2Key

PROG_NAME = "sportbot"
logger = logging.getLogger(__name__)
logging.getLogger("vlc").setLevel(logging.NOTSET)
backtrace.hook(reverse=False, align=True, strip_path=False, enable_on_envvar_only=False, on_tty=False, conservative=False)

dry_option = click.option('--dry', is_flag=True)


@skeleton(name=PROG_NAME, version=version.__version__, auto_envvar_prefix='SP')
@click.option('--debug', help="Verbose mode", is_flag=True)
def cli(debug):
    """SportBot."""
    if 'pytest' not in sys.modules:
        progressbar.streams.wrap(stderr=True, stdout=True)
    if debug:
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(
            colorlog.ColoredFormatter(
                fmt='%(log_color)s%(name)s | %(asctime)s | %(levelname)s | line: %(lineno)d | %(message)s',
                datefmt='%Y-%d-%d %H:%M:%S',
                log_colors={
                    'DEBUG': 'cyan',
                    'INFO': 'green',
                    'WARNING': 'yellow',
                    'ERROR': 'red',
                    'CRITICAL': 'white,bg_red',
                },
            )
        )
        root_logger.handlers = []
        root_logger.addHandler(stream_handler)


@cli.group(help='Boxing Training', cls=AdvancedGroup)
def boxing():
    pass


@boxing.command('rounds', help='Create custom rounds')
@dry_option
@click.option('--name', default="Rounds")
@click.option('--rounds', type=int, default=12)
@click.option('--duration', type=int, default=120)
@click.option('--prepare', type=int, default=10)
@click.option('--end', type=int, default=5)
@click.option('--rest', type=int, default=60)
def boxing_rounds(name: str, prepare: int, duration: int, rest: int, dry: bool, end: int, rounds: int):
    create_sequence(
        name=name,
        description='Boxing rounds',
        exercices=flatten(
            Prepare(duration=prepare),
            Sequence.rounds(
                n=rounds,
                exercice=Boxing("Boxing", duration=duration),
                waiting=Rest(duration=rest)
            ).exercices,
            TheEnd(duration=end),
        ),
        tags={"boxing"},
    ).run(dry)


@cli.group(help='Sequence Tool', cls=AdvancedGroup)
def sequence():
    pass


@sequence.command('list', help='List available sequences')
@click.option('--tag', 'tags', help="Tag filter", multiple=True)
def sequence_list(tags: str):
    for sequence in known_sequences.values():
        if tags and not any(tag in sequence.tags for tag in tags):
            continue
        print(sequence)
        for exercice in sequence.exercices:
            print(f"\t{exercice}")


@sequence.command('start', help='Start sequence')
@click.argument('name')
@dry_option
def sequence_start(name: str, dry: bool):
    sequence = known_sequences.get(name, None)
    if not sequence:
        print("Unknown sequence")
        return

    sequence.run(dry)


@cli.group(help='Training Tool', cls=AdvancedGroup)
def training():
    pass


@training.command('list', help='List available trainings')
@click.option('--tag', 'tags', help="Tag filter", multiple=True)
def training_list(tags: str):
    for training in sorted(known_trainings.values(), key=Py2Key):
        if tags and not any(tag in training.tags for tag in tags):
            continue
        print(training)
        for sequence in training.sequences:
            if tags and not any(tag in sequence.tags for tag in tags):
                continue
            print(f"\t{sequence}")
            for exercice in sequence.exercices:
                print(f"\t\t{exercice}")


@training.command('start', help='Start training')
@click.argument('name')
@dry_option
def training_start(name: str, dry: bool):
    training = known_trainings.get(name, None)
    if not training:
        print("Unknown training")
        return

    training.run(dry)


@cli.group(help='Exercice Tool', cls=AdvancedGroup)
def exercice():
    pass


@exercice.command('list', help='List available exercices')
@click.option('--tag', 'tags', help="Tag filter", multiple=True)
def exercice_list(tags: str):
    for exercice in sorted(known_exercices.values(), key=Py2Key):
        if tags and not any(tag in exercice.tags for tag in tags):
            continue
        print(exercice)


@exercice.command('tags', help='List available tags')
def exercice_tags():
    for tag in Exercice.known_tags:  # pylint: disable=not-an-iterable
        print(tag)


@exercice.command('start', help='Start exercice')
@click.argument('name')
@dry_option
def exercice_start(name: str, dry: bool):
    exercice = known_exercices.get(name, None)
    if not exercice:
        print("Unknown exercice")
        return

    exercice.run(dry=dry)


@cli.command(help='Generate sound')
@click.argument("name")
@dry_option
@click.option('--force', help="Recreate sound if already exists", is_flag=True)
@click.option(
    "--path",
    help="Sound output path",
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
    default='.',
    show_default=True,
)
def generate_sound(name: str, dry: bool, path: str, force: bool):
    sound = TempSound(name, directory=Path(path))
    sound.create(dry=dry, force=force)
    sound.say(dry)


@cli.command(short_help='Generates a README.rst', aliases=['doc'])
@click.pass_context
@click.option('--output', help='README output format', type=click.Choice(['rst', 'markdown']), default='rst', show_default=True)
def readme(ctx, output: str):
    '''Generates a complete readme'''
    doc.readme(cli, ctx.obj.prog_name, ctx.obj.context_settings, output)


def main(**kwargs):
    return cli.main(prog_name=PROG_NAME, **kwargs)

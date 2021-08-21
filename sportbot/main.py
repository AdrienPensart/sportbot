#!/usr/bin/env python3
import logging
import click
import progressbar  # type: ignore
from gtts import gTTS  # type: ignore
from click_skeleton import skeleton, doc, backtrace, ExpandedPath
from sportbot import version
from sportbot.sequence import Sequence
from sportbot.exercice import known_exercices, Rest, Waiting, Boxing
from sportbot.boxing import boxing_training  # type: ignore
from sportbot.helpers import rounds, flatten, Py2Key

PROG_NAME = "sportbot"
logger = logging.getLogger(__name__)
logging.getLogger("vlc").setLevel(logging.NOTSET)
backtrace.hook(reverse=False, align=True, strip_path=False, enable_on_envvar_only=False, on_tty=False, conservative=False)

dry_option = click.option('--dry', is_flag=True)


@skeleton(name=PROG_NAME, version=version.__version__, auto_envvar_prefix='SP')
def cli():
    """SportBot."""
    progressbar.streams.wrap(stderr=True, stdout=True)


@cli.command(help='Create custom rounds')
@dry_option
@click.option('--name', default="Rounds")
@click.option('--rounds', '_rounds', type=int, default=12)
@click.option('--duration', type=int, default=120)
@click.option('--prepare', type=int, default=10)
@click.option('--rest', type=int, default=60)
def boxing(name, prepare, duration, rest, dry, _rounds):
    _round = Boxing("Boxing", duration=duration)
    _rest = Rest(duration=rest)
    all_rounds = flatten(
        Waiting("Prepare", duration=prepare),
        rounds(n=_rounds, exercice=_round, rest=_rest),
        Waiting("The End", duration=5),
    )
    sequence = Sequence(
        name=name,
        exercices=all_rounds,
        tags={"boxing"},
    )
    sequence.run(dry)


@cli.command('sequences', help='List available sequences')
@click.option('--tag', 'tags', help="Tag filter", multiple=True)
def _sequences(tags: str):
    for sequence in boxing_training.sequences:
        if tags and not any(tag in sequence.tags for tag in tags):
            continue
        print(sequence)
        for exercice in sequence.exercices:
            print(f"   {exercice}")


@cli.command('exercices', help='List available exercices')
@click.option('--tag', 'tags', help="Tag filter", multiple=True)
def _exercices(tags: str):
    for exercice in sorted(known_exercices, key=Py2Key):
        if tags:
            for tag in tags:
                if tag not in exercice.tags:
                    print(exercice)
        else:
            print(exercice)


@cli.command(help='List available tags')
def tags():
    for tag in boxing_training.tags:
        print(tag)


@cli.command(help='Generate sound')
@click.argument("name")
@dry_option
@click.option(
    "--path",
    help="Sound output path",
    type=ExpandedPath(exists=True, dir_okay=True, file_okay=False),
    default='.',
    show_default=True,
)
def generate_sound(name, dry, path):
    tts = gTTS(name)
    if not dry:
        tts.save(path)


@cli.command(help='Start sequence')
@click.argument('name')
@dry_option
def start(name, dry):
    for sequence in boxing_training.sequences:
        if name == sequence.name:
            sequence.run(dry)
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

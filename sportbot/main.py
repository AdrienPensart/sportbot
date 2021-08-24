#!/usr/bin/env python3
from pathlib import Path
import sys
import logging
import click
import colorlog  # type: ignore
import progressbar  # type: ignore
from click_skeleton import skeleton, doc, backtrace
from sportbot import version
from sportbot.options import dry_option
from sportbot.sound import TempSound
import sportbot
import sportbot.commands


PROG_NAME = "sportbot"
logger = logging.getLogger(__name__)
logging.getLogger("vlc").setLevel(logging.NOTSET)
backtrace.hook(strip_path=False, enable_on_envvar_only=False, on_tty=False)


@skeleton(name=PROG_NAME, version=version.__version__, auto_envvar_prefix='SP')
@click.option('--debug', help="Verbose mode", is_flag=True)
def cli(debug):
    """SportBot."""
    if 'pytest' not in sys.modules:
        progressbar.streams.wrap(stderr=True, stdout=True)
    level = logging.DEBUG if debug else logging.WARNING
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
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


@cli.command(short_help='Generates a README.rst', aliases=['doc'])
@click.pass_context
@click.option('--output', help='README output format', type=click.Choice(['rst', 'markdown']), default='rst', show_default=True)
def readme(ctx, output: str):
    '''Generates a complete readme'''
    doc.readme(cli, ctx.obj.prog_name, ctx.obj.context_settings, output)


cli.add_groups_from_package(sportbot.commands)


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


@cli.command(help='Generate sound')
@click.argument('duration', type=click.DateTime(formats=["%H:%M"]))
def countdown(duration):
    print(duration)


def main(**kwargs):
    return cli.main(prog_name=PROG_NAME, **kwargs)

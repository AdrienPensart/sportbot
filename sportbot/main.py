#!/usr/bin/env python3
import asyncio
import logging
from pathlib import Path

import cfonts
import click
import colorlog
import pendulum
from beartype import beartype
from beartype.typing import Any
from click_skeleton import backtrace, doc, skeleton
from click_skeleton.helpers import mysplit
from prompt_toolkit import ANSI, Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, VerticalAlign, VSplit
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.widgets import Label

import sportbot
import sportbot.commands
from sportbot import version
from sportbot.options import dry_option
from sportbot.playsound import PlaysoundException
from sportbot.sound import TempSound

PROG_NAME = "sportbot"
logger = logging.getLogger(__name__)
logging.getLogger("vlc").setLevel(logging.NOTSET)
backtrace.hook(strip_path=False, enable_on_envvar_only=False, on_tty=False)


@skeleton(name=PROG_NAME, version=version.__version__, auto_envvar_prefix="SP")
@click.option("--debug", help="Verbose mode", is_flag=True)
@beartype
def cli(debug: bool) -> None:
    """SportBot."""
    level = logging.DEBUG if debug else logging.WARNING
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(
        colorlog.ColoredFormatter(
            fmt="%(log_color)s%(name)s | %(asctime)s | %(levelname)s | line: %(lineno)d | %(message)s",
            datefmt="%Y-%d-%d %H:%M:%S",
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "white,bg_red",
            },
        )
    )
    root_logger.handlers = []
    root_logger.addHandler(stream_handler)


@cli.command(short_help="Generates a README.rst", aliases=["doc"])
@click.pass_context
@click.option(
    "--output",
    help="README output format",
    type=click.Choice(["rst", "markdown"]),
    default="rst",
    show_default=True,
)
@beartype
def readme(ctx: click.Context, output: str) -> None:
    """Generates a complete readme"""
    doc.readme(cli, ctx.obj.prog_name, ctx.obj.context_settings, output)


cli.add_groups_from_package(sportbot.commands)


@cli.command(help="Generate sound")
@click.argument("name")
@dry_option
@click.option("--test", help="Test sound afterwards", is_flag=True)
@click.option("--force", help="Recreate sound if already exists", is_flag=True)
@click.option(
    "--path",
    help="Sound output path",
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
    default=".",
    show_default=True,
)
@beartype
def generate_sound(name: str, dry: bool, path: str, force: bool, test: bool) -> None:
    sound = TempSound(name, directory=Path(path))
    sound.create(dry=dry, force=force)
    if test:
        sound.say(dry)


@cli.command("countdown", help="Generate sound")
@click.argument("duration")
@click.option("--paused", is_flag=True)
@beartype
def _countdown(duration: str, paused: bool) -> None:
    """
    DURATION : HH:MM:SS or MM:SS or SS
    """
    elems = mysplit(duration, ":")
    seconds = 0
    minutes = 0
    hours = 0
    try:
        if len(elems) == 1:
            seconds = int(elems[0])
        elif len(elems) == 2:
            minutes = int(elems[0])
            seconds = int(elems[1])
        elif len(elems) == 3:
            hours = int(elems[0])
            minutes = int(elems[1])
            seconds = int(elems[2])
        else:
            logger.error("Bad format for duration, should be HH:MM:SS or HH:MM or SS")
            raise click.Abort()
    except ValueError as e:
        logger.error("Bad format for duration, should be HH:MM:SS or HH:MM or SS")
        raise click.Abort() from e

    def output_countdown(c: Any, is_paused: bool) -> ANSI:
        formatted_countdown = f"{c.hours:02d}:{c.minutes:02d}:{c.remaining_seconds:02d}"
        if is_paused:
            formatted_countdown += " (paused)"
        return ANSI(
            cfonts.render(
                formatted_countdown,
                gradient=["green", "red"],
                align="center",
                font="huge",
                transition=True,
            )
        )

    loop = asyncio.get_event_loop()
    kb = KeyBindings()

    @kb.add("c-c")
    @kb.add("q")
    def leave(event: Any) -> None:
        event.app.exit()

    @kb.add("space")
    def switch_paused(event: Any) -> None:
        event.app.paused = not event.app.paused
        label.text = output_countdown(event.app.countdown, event.app.paused)
        app.invalidate()

    base_countdown = pendulum.duration(hours=hours, minutes=minutes, seconds=seconds)
    label = Label(text=output_countdown(base_countdown, paused))
    root_container = VSplit(
        [
            HSplit(
                [label],
                align=VerticalAlign.CENTER,
            ),
        ],
    )
    layout = Layout(root_container)
    app: Application = Application(layout=layout, key_bindings=kb, full_screen=True)

    app.countdown = base_countdown  # type: ignore[attr-defined]
    app.paused = paused  # type: ignore[attr-defined]

    async def update_countdown() -> None:
        while True:
            if not app.paused:  # type: ignore[attr-defined]
                app.countdown -= pendulum.duration(seconds=1)  # type: ignore[attr-defined]
            label.text = output_countdown(app.countdown, app.paused)  # type: ignore[attr-defined]
            app.invalidate()
            if not app.countdown.seconds:  # type: ignore[attr-defined]
                break
            if app.paused:  # type: ignore[attr-defined]
                await asyncio.sleep(0.1)
            else:
                await asyncio.sleep(1)

    async def wait_complete() -> None:
        tasks = [
            asyncio.create_task(app.run_async()),
            asyncio.create_task(update_countdown()),
        ]
        await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    loop.run_until_complete(wait_complete())


def main(**kwargs: Any) -> Any:
    try:
        return cli.main(prog_name=PROG_NAME, **kwargs)
    except PlaysoundException as e:
        logger.error(e)
    return 1


if __name__ == "__main__":
    main()

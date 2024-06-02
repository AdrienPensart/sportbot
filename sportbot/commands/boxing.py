import click
from beartype import beartype
from click_skeleton import AdvancedGroup

from sportbot import Boxing, Prepare, Rest, Sequence, Tag, TheEnd
from sportbot.helpers import flatten
from sportbot.options import (
    dry_option,
    duration_option,
    end_option,
    prepare_option,
    rest_option,
    rounds_option,
    silence_option,
)
from sportbot.sequence import create_sequence


@click.group(help="Boxing Training", cls=AdvancedGroup)
@beartype
def cli() -> None:
    pass


@cli.command("rounds", help="Create custom rounds")
@dry_option
@silence_option
@duration_option
@prepare_option
@end_option
@rest_option
@rounds_option
@click.option("--name", default="Rounds")
@beartype
def _rounds(
    name: str,
    prepare: int,
    duration: int,
    rest: int,
    dry: bool,
    silence: bool,
    end: int,
    rounds: int,
) -> None:
    create_sequence(
        name=name,
        description="Boxing rounds",
        exercices=flatten(
            Prepare(duration=prepare),
            Sequence.rounds(
                n=rounds,
                exercice=Boxing(duration=duration),
                waiting=Rest(duration=rest),
            ).exercices,
            TheEnd(duration=end),
        ),
        tags={Tag.BOXING},
    ).run(dry=dry, silence=silence)

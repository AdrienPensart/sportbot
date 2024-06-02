import click
from beartype import beartype
from click_skeleton import AdvancedGroup

from sportbot import Boxing, Prepare, Rest, Sequence, TheEnd
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
    Sequence(
        name=name,
        description="Boxing rounds",
        exercises=flatten(
            Prepare(duration=prepare),
            Sequence.rounds(
                n=rounds,
                exercise=Boxing(duration=duration),
                waiting=Rest(duration=rest),
            ).exercises,
            TheEnd(duration=end),
        ),
    ).run(dry=dry, silence=silence)

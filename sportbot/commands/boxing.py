import click
from beartype import beartype
from click_skeleton import AdvancedGroup

from sportbot.boxing import Boxing
from sportbot.exercise import Prepare, TheEnd
from sportbot.helpers import flatten
from sportbot.options import dry_option, silence_option
from sportbot.rest import Rest
from sportbot.sequence import Sequence, create_sequence
from sportbot.tag import Tag


@click.group(help="Boxing Training", cls=AdvancedGroup)
@beartype
def cli() -> None:
    pass


@cli.command("rounds", help="Create custom rounds")
@dry_option
@silence_option
@click.option("--name", default="Rounds")
@click.option("--rounds", type=int, default=12)
@click.option("--duration", type=int, default=120)
@click.option("--prepare", type=int, default=10)
@click.option("--end", type=int, default=5)
@click.option("--rest", type=int, default=60)
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

import click
from click_skeleton import AdvancedGroup

from sportbot.boxing import Boxing  # type: ignore
from sportbot.exercise import Prepare, TheEnd
from sportbot.helpers import flatten
from sportbot.options import dry_option
from sportbot.rest import Rest
from sportbot.sequence import Sequence, create_sequence


@click.group(help="Boxing Training", cls=AdvancedGroup)
def cli():
    pass


@cli.command("rounds", help="Create custom rounds")
@dry_option
@click.option("--name", default="Rounds")
@click.option("--rounds", type=int, default=12)
@click.option("--duration", type=int, default=120)
@click.option("--prepare", type=int, default=10)
@click.option("--end", type=int, default=5)
@click.option("--rest", type=int, default=60)
def boxing_rounds(name: str, prepare: int, duration: int, rest: int, dry: bool, end: int, rounds: int):
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
        tags={"boxing"},
    ).run(dry)

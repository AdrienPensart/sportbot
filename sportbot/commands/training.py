import click
from beartype import beartype
from click_skeleton import AdvancedGroup

from sportbot.helpers import Py2Key
from sportbot.options import dry_option
from sportbot.training import known_trainings


@click.group(help="Training Tool", cls=AdvancedGroup)
@beartype
def cli() -> None:
    pass


@cli.command("list", help="List available trainings")
@click.option("--tag", "tags", help="Tag filter", multiple=True)
@beartype
def _list(tags: tuple[str, ...]) -> None:
    for training in sorted(known_trainings.values(), key=Py2Key):
        if tags and not any(tag in training.tags for tag in tags):
            continue
        print(f"{training}")
        for sequence in training.sequences:
            if tags and not any(tag in sequence.tags for tag in tags):
                continue
            print(f"\t{sequence}")
            for exercice in sequence.exercices:
                print(f"\t\t{exercice}")


@cli.command("start", help="Start training")
@click.argument("name")
@beartype
@dry_option
def start(name: str, dry: bool) -> None:
    training = known_trainings.get(name, None)
    if not training:
        print("Unknown training")
        return

    training.run(dry)

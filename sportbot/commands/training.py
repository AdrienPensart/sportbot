import click
from beartype import beartype
from click_skeleton import AdvancedGroup

from sportbot import KnownTrainings
from sportbot.exercises.helpers import Py2Key
from sportbot.options import dry_option, silence_option


@click.group(help="Training Tool", cls=AdvancedGroup)
@beartype
def cli() -> None:
    pass


@cli.command("list", help="List available trainings")
@click.option("--tag", "tags", help="Tag filter", multiple=True)
@beartype
def _list(tags: tuple[str, ...]) -> None:
    for training in sorted(KnownTrainings.values(), key=Py2Key):
        if tags and not any(tag in training.tags for tag in tags):
            continue
        print(f"{training}")
        for sequence in training.sequences:
            if tags and not any(tag in sequence.tags for tag in tags):
                continue
            print(f"\t{sequence}")
            for exercise in sequence.exercises:
                print(f"\t\t{exercise}")


@cli.command("start", help="Start training")
@click.argument("name")
@dry_option
@silence_option
@beartype
def start(name: str, dry: bool, silence: bool) -> None:
    training = KnownTrainings.get(name, None)
    if not training:
        print("Unknown training")
        return

    training.run(dry=dry, silence=silence)

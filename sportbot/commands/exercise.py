import click
from beartype import beartype
from click_skeleton import AdvancedGroup

from sportbot import Exercise, KnownExercises
from sportbot.helpers import Py2Key
from sportbot.options import dry_option, duration_option, silence_option


@click.group(help="Exercise Tool", cls=AdvancedGroup)
@beartype
def cli() -> None:
    pass


@cli.command("list", help="List available exercices")
@click.option("--tag", "tags", help="Tag filter", multiple=True)
@beartype
def _list(tags: tuple[str, ...]) -> None:
    for exercice in sorted(KnownExercises.values(), key=Py2Key):
        if tags and not any(tag in exercice.tags for tag in tags):
            continue
        print(f"{exercice}")


@cli.command("tags", help="List available tags")
@beartype
def tags() -> None:
    for tag in Exercise.known_tags():
        print(tag)


@cli.command(help="Start exercice")
@click.argument("name")
@dry_option
@silence_option
@beartype
def start(name: str, dry: bool, silence: bool) -> None:
    exercice = KnownExercises.get(name, None)
    if not exercice:
        print("Unknown exercice")
        return

    exercice.run(dry=dry, silence=silence)


@cli.command(help="Start custom exercice")
@click.argument("name")
@duration_option
@dry_option
@silence_option
@beartype
def custom(name: str, dry: bool, silence: bool, duration: int) -> None:
    exercice = Exercise(name=name, duration=duration)
    exercice.run(dry=dry, silence=silence)

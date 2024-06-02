import click
from beartype import beartype
from click_skeleton import AdvancedGroup

from sportbot.exercise import Exercise, known_exercises
from sportbot.helpers import Py2Key
from sportbot.options import dry_option, silence_option


@click.group(help="Exercise Tool", cls=AdvancedGroup)
@beartype
def cli() -> None:
    pass


@cli.command("list", help="List available exercices")
@click.option("--tag", "tags", help="Tag filter", multiple=True)
@beartype
def _list(tags: tuple[str, ...]) -> None:
    for exercice in sorted(known_exercises.values(), key=Py2Key):
        if tags and not any(tag in exercice.tags for tag in tags):
            continue
        print(f"{exercice}")


@cli.command("tags", help="List available tags")
@beartype
def tags() -> None:
    for tag in Exercise.known_tags():
        print(tag)


@cli.command("start", help="Start exercice")
@click.argument("name")
@dry_option
@silence_option
@beartype
def start(name: str, dry: bool, silence: bool) -> None:
    exercice = known_exercises.get(name, None)
    if not exercice:
        print("Unknown exercice")
        return

    exercice.run(dry=dry, silence=silence)

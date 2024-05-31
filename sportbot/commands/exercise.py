import click
from click_skeleton import AdvancedGroup

from sportbot.exercise import Exercise, known_exercises
from sportbot.helpers import Py2Key
from sportbot.options import dry_option


@click.group(help="Exercise Tool", cls=AdvancedGroup)
def cli():
    pass


@cli.command("list", help="List available exercices")
@click.option("--tag", "tags", help="Tag filter", multiple=True)
def _list(tags: str):
    for exercice in sorted(known_exercises.values(), key=Py2Key):
        if tags and not any(tag in exercice.tags for tag in tags):
            continue
        print(exercice)


@cli.command("tags", help="List available tags")
def tags():
    for tag in Exercise.known_tags():
        print(tag)


@cli.command("start", help="Start exercice")
@click.argument("name")
@dry_option
def start(name: str, dry: bool):
    exercice = known_exercises.get(name, None)
    if not exercice:
        print("Unknown exercice")
        return

    exercice.run(dry=dry)

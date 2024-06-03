import click
from beartype import beartype
from click_skeleton import AdvancedGroup

from sportbot import Exercise, KnownExercises
from sportbot.exercises.helpers import Py2Key
from sportbot.options import dry_option, duration_option, silence_option


@click.group(help="Exercise Tool", cls=AdvancedGroup)
@beartype
def cli() -> None:
    pass


@cli.command("list", help="List available exercises")
@click.option("--tag", "tags", help="Tag filter", multiple=True)
@beartype
def _list(tags: tuple[str, ...]) -> None:
    for exercise in sorted(KnownExercises.values(), key=Py2Key):
        if tags and not any(tag in exercise.tags for tag in tags):
            continue
        print(f"{exercise}")


@cli.command("tags", help="List available tags")
@beartype
def tags() -> None:
    for tag in Exercise.known_tags():
        print(tag)


@cli.command(help="Start exercise")
@click.argument("name")
@dry_option
@silence_option
@beartype
def start(name: str, dry: bool, silence: bool) -> None:
    exercise = KnownExercises.get(name, None)
    if not exercise:
        print("Unknown exercise")
        return

    exercise.run(dry=dry, silence=silence)


@cli.command(help="Start custom exercise")
@click.argument("name")
@duration_option
@dry_option
@silence_option
@beartype
def custom(name: str, dry: bool, silence: bool, duration: int) -> None:
    exercise = Exercise(name=name, duration=duration)
    exercise.run(dry=dry, silence=silence)

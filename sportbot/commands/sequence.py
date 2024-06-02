import click
from beartype import beartype
from click_skeleton import AdvancedGroup

from sportbot import KnownSequences
from sportbot.options import dry_option, silence_option


@click.group(help="Sequence Tool", cls=AdvancedGroup)
@beartype
def cli() -> None:
    pass


@cli.command("list", help="List available sequences")
@click.option("--tag", "tags", help="Tag filter", multiple=True)
@beartype
def _list(tags: tuple[str, ...]) -> None:
    for sequence in KnownSequences.values():
        if tags and not any(tag in sequence.tags for tag in tags):
            continue
        print(f"{sequence}")
        for exercise in sequence.exercises:
            print(f"\t{exercise}")


@cli.command("start", help="Start sequence")
@click.argument("name")
@dry_option
@silence_option
@beartype
def start(name: str, dry: bool, silence: bool) -> None:
    sequence = KnownSequences.get(name, None)
    if not sequence:
        print("Unknown sequence")
        return

    sequence.run(dry=dry, silence=silence)

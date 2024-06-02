import click
from beartype import beartype
from click_skeleton import AdvancedGroup

from sportbot.options import dry_option, silence_option
from sportbot.sequence import known_sequences


@click.group(help="Sequence Tool", cls=AdvancedGroup)
@beartype
def cli() -> None:
    pass


@cli.command("list", help="List available sequences")
@click.option("--tag", "tags", help="Tag filter", multiple=True)
@beartype
def _list(tags: tuple[str, ...]) -> None:
    for sequence in known_sequences.values():
        if tags and not any(tag in sequence.tags for tag in tags):
            continue
        print(f"{sequence}")
        for exercice in sequence.exercices:
            print(f"\t{exercice}")


@cli.command("start", help="Start sequence")
@click.argument("name")
@dry_option
@silence_option
@beartype
def start(name: str, dry: bool, silence: bool) -> None:
    sequence = known_sequences.get(name, None)
    if not sequence:
        print("Unknown sequence")
        return

    sequence.run(dry=dry, silence=silence)

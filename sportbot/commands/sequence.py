import click
from click_skeleton import AdvancedGroup
from sportbot.options import dry_option
from sportbot.sequence import known_sequences


@click.group(help='Sequence Tool', cls=AdvancedGroup)
def cli():
    pass


@cli.command('list', help='List available sequences')
@click.option('--tag', 'tags', help="Tag filter", multiple=True)
def sequence_list(tags: str):
    for sequence in known_sequences.values():
        if tags and not any(tag in sequence.tags for tag in tags):
            continue
        print(sequence)
        for exercice in sequence.exercices:
            print(f"\t{exercice}")


@cli.command('start', help='Start sequence')
@click.argument('name')
@dry_option
def sequence_start(name: str, dry: bool):
    sequence = known_sequences.get(name, None)
    if not sequence:
        print("Unknown sequence")
        return

    sequence.run(dry)

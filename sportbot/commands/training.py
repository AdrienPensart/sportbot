import click
from click_skeleton import AdvancedGroup
from sportbot.options import dry_option
from sportbot.training import known_trainings
from sportbot.helpers import Py2Key


@click.group(help='Training Tool', cls=AdvancedGroup)
def cli():
    pass


@cli.command('list', help='List available trainings')
@click.option('--tag', 'tags', help="Tag filter", multiple=True)
def _list(tags: str):
    for training in sorted(known_trainings.values(), key=Py2Key):
        if tags and not any(tag in training.tags for tag in tags):
            continue
        print(training)
        for sequence in training.sequences:
            if tags and not any(tag in sequence.tags for tag in tags):
                continue
            print(f"\t{sequence}")
            for exercice in sequence.exercices:
                print(f"\t\t{exercice}")


@cli.command('start', help='Start training')
@click.argument('name')
@dry_option
def start(name: str, dry: bool):
    training = known_trainings.get(name, None)
    if not training:
        print("Unknown training")
        return

    training.run(dry)

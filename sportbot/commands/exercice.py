import click
from click_skeleton import AdvancedGroup
from sportbot.options import dry_option
from sportbot.exercice import known_exercices, Exercice
from sportbot.helpers import Py2Key


@click.group(help='Exercice Tool', cls=AdvancedGroup)
def cli():
    pass


@cli.command('list', help='List available exercices')
@click.option('--tag', 'tags', help="Tag filter", multiple=True)
def _list(tags: str):
    for exercice in sorted(known_exercices.values(), key=Py2Key):
        if tags and not any(tag in exercice.tags for tag in tags):
            continue
        print(exercice)


@cli.command('tags', help='List available tags')
def tags():
    for tag in Exercice.known_tags:  # pylint: disable=not-an-iterable
        print(tag)


@cli.command('start', help='Start exercice')
@click.argument('name')
@dry_option
def start(name: str, dry: bool):
    exercice = known_exercices.get(name, None)
    if not exercice:
        print("Unknown exercice")
        return

    exercice.run(dry=dry)

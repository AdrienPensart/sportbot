import click

dry_option = click.option(
    "--dry/--no-dry",
    is_flag=True,
    default=False,
    show_default=True,
)

silence_option = click.option(
    "--silence/--no-silence",
    is_flag=True,
    default=False,
    show_default=True,
)

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

duration_option = click.option("--duration", type=int, default=120)
prepare_option = click.option("--prepare", type=int, default=10)
end_option = click.option("--end", type=int, default=5)
rest_option = click.option("--rest", type=int, default=60)
rounds_option = click.option("--rounds", type=int, default=12)

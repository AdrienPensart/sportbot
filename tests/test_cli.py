# pylint: disable=missing-module-docstring,missing-function-docstring
from click.testing import CliRunner
from click_skeleton.testing import run_cli

from sportbot import version
from sportbot.main import cli


def test_cli(cli_runner: CliRunner) -> None:
    run_cli(cli_runner, cli)


def test_cli_readme_rst(cli_runner: CliRunner) -> None:
    run_cli(
        cli_runner,
        cli,
        [
            "readme",
            "--output",
            "rst",
        ],
    )


def test_cli_readme_md(cli_runner: CliRunner) -> None:
    run_cli(
        cli_runner,
        cli,
        [
            "readme",
            "--output",
            "markdown",
        ],
    )


def test_cli_version(cli_runner: CliRunner) -> None:
    output1 = run_cli(
        cli_runner,
        cli,
        [
            "-V",
        ],
    )
    output2 = run_cli(
        cli_runner,
        cli,
        [
            "--version",
        ],
    )
    output3 = run_cli(
        cli_runner,
        cli,
        [
            "version",
        ],
    )
    assert output1 == output2 == output3
    assert version.__version__ in output1


def test_cli_help(cli_runner: CliRunner) -> None:
    output1 = run_cli(
        cli_runner,
        cli,
        [
            "-h",
        ],
    )
    output2 = run_cli(
        cli_runner,
        cli,
        [
            "--help",
        ],
    )
    output3 = run_cli(
        cli_runner,
        cli,
        [
            "help",
        ],
    )
    assert output1 == output2 == output3


def test_cli_boxing_rounds(cli_runner: CliRunner) -> None:
    run_cli(
        cli_runner,
        cli,
        [
            "boxing",
            "rounds",
            "--dry",
        ],
    )


def test_cli_training_list(cli_runner: CliRunner) -> None:
    run_cli(
        cli_runner,
        cli,
        [
            "training",
            "list",
        ],
    )


def test_cli_training_start(cli_runner: CliRunner) -> None:
    run_cli(
        cli_runner,
        cli,
        [
            "training",
            "start",
            "boxing-training",
            "--dry",
        ],
    )


def test_cli_sequence_list(cli_runner: CliRunner) -> None:
    run_cli(
        cli_runner,
        cli,
        [
            "sequence",
            "list",
        ],
    )


def test_cli_sequence_start(cli_runner: CliRunner) -> None:
    run_cli(
        cli_runner,
        cli,
        [
            "sequence",
            "start",
            "12-rounds-2-minutes-shadow-boxing",
            "--dry",
        ],
    )


def test_cli_exercises_list(cli_runner: CliRunner) -> None:
    run_cli(
        cli_runner,
        cli,
        [
            "exercise",
            "list",
        ],
    )


def test_cli_exercise_start(cli_runner: CliRunner) -> None:
    run_cli(
        cli_runner,
        cli,
        [
            "exercise",
            "start",
            "prepare",
            "--dry",
        ],
    )


def test_cli_exercise_custom(cli_runner: CliRunner) -> None:
    run_cli(
        cli_runner,
        cli,
        [
            "exercise",
            "custom",
            "custom-exercise",
            "--duration",
            1,
            "--dry",
        ],
    )


def test_cli_exercise_tags(cli_runner: CliRunner) -> None:
    run_cli(
        cli_runner,
        cli,
        [
            "exercise",
            "tags",
        ],
    )


def test_cli_generate_sound(cli_runner: CliRunner) -> None:
    run_cli(
        cli_runner,
        cli,
        [
            "generate-sound",
            "test",
            "--path",
            "/tmp/",
            "--force",
        ],
    )


def test_cli_countdown(cli_runner: CliRunner) -> None:
    run_cli(
        cli_runner,
        cli,
        [
            "countdown",
            "1",
        ],
    )

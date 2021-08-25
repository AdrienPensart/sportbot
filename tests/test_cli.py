# pylint: disable=missing-module-docstring,missing-function-docstring
import pytest
from click_skeleton.testing import run_cli
from sportbot import version
from sportbot.main import cli


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli(cli_runner):
    run_cli(cli_runner, cli)


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_readme_rst(cli_runner):
    run_cli(cli_runner, cli, [
        'readme',
        '--output', 'rst',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_readme_md(cli_runner):
    run_cli(cli_runner, cli, [
        'readme',
        '--output', 'markdown',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_version(cli_runner):
    output1 = run_cli(cli_runner, cli, [
        '-V',
    ])
    output2 = run_cli(cli_runner, cli, [
        '--version',
    ])
    output3 = run_cli(cli_runner, cli, [
        'version',
    ])
    assert output1 == output2 == output3
    assert version.__version__ in output1


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_help(cli_runner):
    output1 = run_cli(cli_runner, cli, [
        '-h',
    ])
    output2 = run_cli(cli_runner, cli, [
        '--help',
    ])
    output3 = run_cli(cli_runner, cli, [
        'help',
    ])
    assert output1 == output2 == output3


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_completion_show(cli_runner):
    shells = [
        "bash",
        "fish",
        "zsh",
        "powershell",
    ]

    for shell in shells:
        run_cli(cli_runner, cli, [
            'completion',
            'show',
            shell,
        ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_boxing_rounds(cli_runner):
    run_cli(cli_runner, cli, [
        'boxing', 'rounds',
        '--dry',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_trainings_list(cli_runner):
    run_cli(cli_runner, cli, [
        'training', 'list',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_training_start(cli_runner):
    run_cli(cli_runner, cli, [
        'training', 'start',
        'boxing-training',
        '--dry',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_sequences_list(cli_runner):
    run_cli(cli_runner, cli, [
        'sequence', 'list',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_sequence_start(cli_runner):
    run_cli(cli_runner, cli, [
        'sequence', 'start',
        '12-rounds-2-minutes-shadow-boxing',
        '--dry',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_exercices_list(cli_runner):
    run_cli(cli_runner, cli, [
        'exercice', 'list',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_exercice_start(cli_runner):
    run_cli(cli_runner, cli, [
        'exercice', 'start',
        'prepare',
        '--dry',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_exercice_tags(cli_runner):
    run_cli(cli_runner, cli, [
        'exercice', 'tags',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_generate_sound(cli_runner):
    run_cli(cli_runner, cli, [
        'generate-sound',
        'test',
        '--path', '/tmp/',
        '--force',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_countdown(cli_runner):
    run_cli(cli_runner, cli, [
        'countdown',
        '1',
    ])

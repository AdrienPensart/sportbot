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
def test_cli_trainings(cli_runner):
    run_cli(cli_runner, cli, [
        'trainings',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_start_training(cli_runner):
    run_cli(cli_runner, cli, [
        'start-training',
        'boxing-training',
        '--dry',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_sequences(cli_runner):
    run_cli(cli_runner, cli, [
        'sequences',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_start_sequence(cli_runner):
    run_cli(cli_runner, cli, [
        'start-sequence',
        '12-rounds-2-minutes-shadow-boxing',
        '--dry',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_exercices(cli_runner):
    run_cli(cli_runner, cli, [
        'exercices',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_start_exercice(cli_runner):
    run_cli(cli_runner, cli, [
        'start-exercice',
        'prepare',
        '--dry',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_cli_tags(cli_runner):
    run_cli(cli_runner, cli, [
        'tags',
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
def test_cli_boxing(cli_runner):
    run_cli(cli_runner, cli, [
        'boxing',
        '--dry',
    ])

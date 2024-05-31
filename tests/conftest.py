from beartype import beartype
from click.testing import CliRunner
from prompt_toolkit.application import create_app_session
from prompt_toolkit.input import create_pipe_input
from prompt_toolkit.output import DummyOutput
from pytest import fixture


@fixture
@beartype
def cli_runner() -> CliRunner:
    """Instance of `click.testing.CliRunner` with mix_stderr=False"""
    return CliRunner(mix_stderr=False)


@fixture(autouse=True, scope="function")
@beartype
def mock_input():
    with create_pipe_input() as pipe_input:
        with create_app_session(input=pipe_input, output=DummyOutput()):
            yield pipe_input

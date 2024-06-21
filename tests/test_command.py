import pytest
import typer
from typer.testing import CliRunner

from frobnicate.main import app

runner = CliRunner()


def get_all_commands(app: typer.Typer, prefix: str = ""):
    commands = []
    for command in app.registered_commands:
        commands.append(f"{prefix} {command.name}")

    for subcommand in app.registered_groups:
        commands.append(f"{prefix} {subcommand.name}")
        nested_prefix = f"{prefix} {subcommand.name}"
        commands.extend(get_all_commands(subcommand.typer_instance, nested_prefix))

    return [command.strip() for command in commands]


class TestHelp:
    @pytest.mark.parametrize("cmd", get_all_commands(app))
    def test_base_help(self, cmd):
        result = runner.invoke(app, f"{cmd} --help")
        assert result.exit_code == 0

import pytest
import tempfile

from nexuscli.cli import nexus_cli

SCRIPT_NAME = 'test_script_run'
_, TMP_FILE = tempfile.mkstemp()


@pytest.mark.parametrize('command', ['run dummy', 'create dummy ' + TMP_FILE, 'del dummmy'])
def test_script_disabled(monkeypatch, cli_runner, command):
    """Test that NEXUS3_GROOVY_ENABLED disables `repo script` run, create, del commands """
    monkeypatch.setenv('NEXUS3_GROOVY_ENABLED', 'False')
    cmd = f'script {command}'
    result = cli_runner.invoke(nexus_cli, cmd)

    assert result.exit_code != 0
    assert 'groovy_enabled is False' in result.output


@pytest.mark.integration
def test_create(cli_runner, nexus_client):
    """Test that the `repo script` commands for create works"""
    cmd_create = f'script create {SCRIPT_NAME} tests/fixtures/script.groovy'
    result = cli_runner.invoke(nexus_cli, cmd_create)

    assert result.exit_code == 0
    assert result.output == ''
    assert SCRIPT_NAME in [s.get('name') for s in nexus_client.scripts.list]


@pytest.mark.integration
def test_run(cli_runner, nexus_client):
    """Test that the `repo script` commands for run works"""
    cmd_run = f'script run {SCRIPT_NAME}'
    result = cli_runner.invoke(nexus_cli, cmd_run)

    assert result.exit_code == 0
    assert SCRIPT_NAME in result.output


@pytest.mark.integration
def test_del(cli_runner, nexus_client):
    """Test that the `repo script` commands for del works"""
    cmd_del = f'script del {SCRIPT_NAME}'
    result = cli_runner.invoke(nexus_cli, cmd_del)
    nexus_client.scripts.reset()

    assert result.exit_code == 0
    assert result.output == ''
    assert SCRIPT_NAME not in [s.get('name') for s in nexus_client.scripts.list]

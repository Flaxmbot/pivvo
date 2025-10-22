import pytest
from pathlib import Path
import tempfile
import shutil
from pysmith.cli import app
from typer.testing import CliRunner

runner = CliRunner()


def test_main_callback():
    """Test that the main callback displays the banner."""
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    assert "PySmith" in result.output


def test_init_command():
    """Test the init command creates a project structure."""
    with tempfile.TemporaryDirectory() as temp_dir:
        project_name = "test_project"
        project_path = Path(temp_dir) / project_name

        result = runner.invoke(app, ["init", project_name], cwd=temp_dir)
        assert result.exit_code == 0
        assert f"{project_name} initialized successfully" in result.output

        # Check that project structure was created
        assert project_path.exists()
        assert (project_path / "__init__.py").exists()
        assert (project_path / "README.md").exists()
        assert (project_path / ".gitignore").exists()
        assert (project_path / "venv").exists()


def test_init_existing_project():
    """Test that init fails when project already exists."""
    with tempfile.TemporaryDirectory() as temp_dir:
        project_name = "existing_project"
        project_path = Path(temp_dir) / project_name
        project_path.mkdir()

        result = runner.invoke(app, ["init", project_name], cwd=temp_dir)
        assert result.exit_code == 1
        assert f"{project_path} already exists" in result.output


def test_run_command_no_venv():
    """Test that run command fails without virtual environment."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a dummy script
        script_path = Path(temp_dir) / "test_script.py"
        script_path.write_text("print('Hello, World!')")

        result = runner.invoke(app, ["run", "test_script.py"], cwd=temp_dir)
        assert result.exit_code == 1
        assert "No virtual environment found" in result.output


def test_list_command_no_venv():
    """Test that list command fails without virtual environment."""
    with tempfile.TemporaryDirectory() as temp_dir:
        result = runner.invoke(app, ["list"], cwd=temp_dir)
        assert result.exit_code == 1
        assert "No virtual environment found" in result.output


def test_freeze_command_no_venv():
    """Test that freeze command fails without virtual environment."""
    with tempfile.TemporaryDirectory() as temp_dir:
        result = runner.invoke(app, ["freeze"], cwd=temp_dir)
        assert result.exit_code == 1
        assert "No virtual environment found" in result.output


def test_upgrade_command_no_venv():
    """Test that upgrade command fails without virtual environment."""
    with tempfile.TemporaryDirectory() as temp_dir:
        result = runner.invoke(app, ["upgrade"], cwd=temp_dir)
        assert result.exit_code == 1
        assert "No virtual environment found" in result.output


def test_remove_command_no_venv():
    """Test that remove command fails without virtual environment."""
    with tempfile.TemporaryDirectory() as temp_dir:
        result = runner.invoke(app, ["remove", "some-package"], cwd=temp_dir)
        assert result.exit_code == 1
        assert "No virtual environment found" in result.output


def test_install_deps_no_venv():
    """Test that install-deps command fails without virtual environment."""
    with tempfile.TemporaryDirectory() as temp_dir:
        result = runner.invoke(app, ["install-deps", "pytest"], cwd=temp_dir)
        assert result.exit_code == 1
        assert "No virtual environment found" in result.output
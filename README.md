# PySmith

PySmith is a small, pragmatic CLI tool to initialize and manage Python projects. It helps you
bootstrap a project directory (with a virtual environment, git repo, basic files), manage
dependencies inside the project's venv, and perform common tasks like running scripts,
freezing requirements, or upgrading packages.

This repository is intended to be contribution-friendly. Whether you want to fix a bug,
add features, or improve documentation — you're welcome!

---

## Key Features

- Initialize a new Python project with venv, `README.md`, `__init__.py`, and `.gitignore`.
- Create and manage a per-project virtual environment.
- Install, list, freeze, upgrade, and remove dependencies using the venv's pip.
- Run scripts inside the project's venv.
- Small, dependency-light implementation using `typer`, `rich`, `gitpython`, and `pyfiglet`.

---

## Quickstart

Prerequisites:

- Python 3.10+ (project was developed using 3.11/3.13)
- pip

Install dependencies for development (recommended in a separate venv):

````text
    ____        _____           _ __  __  
   / __ \__  __/ ___/____ ___  (_) /_/ /_
  / /_/ / / / /\__ \/ __ `__ \/ / __/ __ \
 / ____/ /_/ /___/ / / / / / / / /_/ / / /
/_/    \__, //____/_/ /_/ /_/_/\__/_/ /_/ 
  /____/                              

# PySmith

PySmith is a small, pragmatic CLI tool to initialize and manage Python projects. It helps you
bootstrap a project directory (with a virtual environment, git repo, basic files), manage
dependencies inside the project's venv, and perform common tasks like running scripts,
freezing requirements, or upgrading packages.

This repository is intended to be contribution-friendly. Whether you want to fix a bug,
add features, or improve documentation — you're welcome!

---

## Key Features

- Initialize a new Python project with venv, `README.md`, `__init__.py`, and `.gitignore`.
- Create and manage a per-project virtual environment.
- Install, list, freeze, upgrade, and remove dependencies using the venv's pip.
- Run scripts inside the project's venv.
- Small, dependency-light implementation using `typer`, `rich`, `gitpython`, and `pyfiglet`.

---

This will create a folder `my_new_project/` containing:

- `venv/` (virtual environment)
- `__init__.py`
- `README.md`
- `.gitignore`

---

## Commands

The CLI exposes the following commands (via `typer`):

- `init <project_name>` — initialize a new project directory with venv and git.
- `install-deps [packages...]` — install packages into the local venv. Use `-f/--file` to install from a requirements file.
- `run <script.py>` — execute a script inside the venv.
- `list` — list packages installed in the venv.
- `freeze` — write current venv packages to `requirements.txt`.
- `upgrade` — upgrade packages listed in `requirements.txt`.
- `remove <package>` — uninstall a package and update `requirements.txt`.

Use `--help` to see command-specific options:

```bash
python pysmith/main.py --help
python pysmith/main.py install-deps --help
```

---

## Development notes

- The CLI implementation is at `pysmith/cli.py` and the package entrypoint is `pysmith/main.py`.
- The project uses `rich` for pretty terminal output and `typer` for argument handling.
- Errors from subprocess calls are written to `pysmith-error.log` in the current working directory.

Tips while developing:

- When running CLI tools from Git Bash (MINGW64) on Windows you may see raw ANSI escape codes or unexpected terminal output. Two common solutions:
  - Force ANSI rendering in `rich` by creating the Console with `Console(force_terminal=True, color_system="auto")` in `cli.py`.
  - Run Python under `winpty` in Git Bash: `winpty python pysmith/main.py ...`, or use PowerShell/cmd/Windows Terminal.

---

## Tests

There is a `tests/` directory for unit tests — please add tests for new features and bug fixes.

Run tests using your preferred test runner (example using pytest):

```bash
python -m pip install pytest
pytest -q
```

---

## Contributing

We welcome contributions. A good contribution flow:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feat/some-feature`.
3. Add tests that demonstrate the bug or cover the new behavior.
4. Run tests and linters locally.
5. Open a pull request with a clear description of the change.

Please follow standard GitHub etiquette and add a meaningful commit message.

---

## Troubleshooting

- If `typer` fails to run, ensure you have `typer` (and other dependencies) installed in your environment.
- On Windows, if virtual environment activation fails, ensure your Python installation can create venvs and that antivirus or OneDrive policies are not blocking virtualenv creation.
- If subprocess commands fail during package installation, check `pysmith-error.log` for the stdout/stderr that was captured.

---

## License

This project is released under the MIT License. See `LICENSE` for details (add one if missing).

---

## Maintainers

- Primary: (add your name or GitHub handle here)

Thanks for checking out PySmith — contributions, issues, and stars are all appreciated!

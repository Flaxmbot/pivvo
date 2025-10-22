# PySmith

[![PyPI version](https://img.shields.io/pypi/v/pysmith.svg)](https://pypi.org/project/pysmith/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![CI](https://github.com/Flaxmbot/pysmith/workflows/CI/badge.svg)](https://github.com/Flaxmbot/pysmith/actions)

<div align="center">
  <pre>
 ____        _____           _ __  __  
/ __ \__  __/ ___/____ ___  (_) /_/ /_
/ /_/ / / / /\__ \/ __ `__ \/ / __/ __ \
/ ____/ /_/ /___/ / / / / / / / /_/ / / /
/_/    \__, //____/_/ /_/ /_/_/\__/_/ /_/ 
  /____/                              
  </pre>
</div>

> A small, pragmatic CLI tool to initialize and manage Python projects with ease. Bootstrap your projects, manage dependencies, and streamline your workflow—all from the command line.

PySmith helps developers quickly set up Python projects with virtual environments, Git repositories, and essential files. It provides a suite of commands to manage dependencies, run scripts, and maintain your project's environment without leaving the terminal.

## Table of Contents

- [✨ Features](#-features)
- [📦 Installation](#-installation)
- [🚀 Quickstart](#-quickstart)
- [📖 Commands](#-commands)
- [🛠️ Development](#️-development)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👥 Authors](#-authors)

## ✨ Features

- **Project Initialization**: Create new Python projects with virtual environments, Git repos, and basic files in seconds
- **Dependency Management**: Install, list, freeze, upgrade, and remove packages within the project's venv
- **Script Execution**: Run Python scripts directly inside the project's virtual environment
- **Beautiful Output**: Rich terminal interface with progress indicators and colored output
- **Error Handling**: Comprehensive error logging for troubleshooting
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Lightweight**: Minimal dependencies for fast installation and execution

## 📦 Installation

### From PyPI (Recommended)

```bash
pip install pysmith
```

### From Source

```bash
git clone https://github.com/Flaxmbot/pysmith.git
cd pysmith
pip install -e .
```

### Prerequisites

- Python 3.10 or higher
- pip (usually included with Python)

## 🚀 Quickstart

1. **Install PySmith**:
   ```bash
   pip install pysmith
   ```

2. **Initialize a new project**:
   ```bash
   pysmith init my-awesome-project
   cd my-awesome-project
   ```

3. **Install dependencies**:
   ```bash
   pysmith install-deps requests flask python-dotenv
   ```

4. **Run your application**:
   ```bash
   pysmith run app.py
   ```

That's it! Your project is ready with a virtual environment, Git repository, and all dependencies installed.

## 📖 Commands

PySmith provides the following commands:

| Command | Description |
|---------|-------------|
| `pysmith init <name>` | Initialize a new project directory with venv and Git |
| `pysmith install-deps [packages...]` | Install packages into the local venv. Use `-f/--file` to install from requirements file |
| `pysmith run <script.py>` | Execute a Python script inside the venv |
| `pysmith list` | List all packages installed in the venv |
| `pysmith freeze` | Write current venv packages to `requirements.txt` |
| `pysmith upgrade` | Upgrade all packages listed in `requirements.txt` to latest versions |
| `pysmith remove <package>` | Uninstall a package and update `requirements.txt` |

### Getting Help

```bash
# General help
pysmith --help

# Command-specific help
pysmith install-deps --help
pysmith init --help
```

## 🛠️ Development

### Setting Up Development Environment

```bash
git clone https://github.com/Flaxmbot/pysmith.git
cd pysmith
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
```

### Project Structure

```
pysmith/
├── pysmith/
│   ├── __init__.py
│   ├── cli.py          # Main CLI implementation
│   └── main.py         # Package entry point
├── tests/              # Unit tests
├── requirements.txt    # Dependencies
├── pyproject.toml      # Package configuration
├── LICENSE
├── CONTRIBUTING.md
└── README.md
```

### Running Tests

```bash
# Install test dependencies
pip install pytest

# Run tests
pytest

# Run with coverage
pytest --cov=pysmith
```

### Development Notes

- **CLI Implementation**: Located in `pysmith/cli.py` using Typer for argument parsing
- **Terminal Output**: Uses Rich for beautiful, colored terminal output
- **Error Logging**: Failed subprocess commands are logged to `pysmith-error.log`
- **Git Integration**: Uses GitPython for repository initialization
- **Cross-Platform**: Handles different Python executable paths for Windows/macOS/Linux

### Tips for Windows Development

When using Git Bash on Windows, you might see raw ANSI escape codes. Solutions:
- Force ANSI rendering: Modify `cli.py` to use `Console(force_terminal=True, color_system="auto")`
- Use `winpty`: `winpty python pysmith/main.py ...`
- Use PowerShell, CMD, or Windows Terminal instead of Git Bash

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on:

- Reporting bugs
- Requesting features
- Setting up your development environment
- Submitting pull requests
- Code style guidelines

### Quick Contribution Flow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Add tests for your changes
4. Ensure all tests pass: `pytest`
5. Commit your changes: `git commit -m "Add amazing feature"`
6. Push to your branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Devrat Kuntal** - *Creator & Maintainer* - [rdxdevbhai76@gmail.com](mailto:rdxdevbhai76@gmail.com)

---

<div align="center">
  <p>Made with ❤️ for the Python community</p>
  <p>
    <a href="#pysmith">Back to top</a> •
    <a href="https://github.com/Flaxmbot/pysmith/issues">Report Bug</a> •
    <a href="https://github.com/Flaxmbot/pysmith/issues">Request Feature</a>
  </p>
</div>

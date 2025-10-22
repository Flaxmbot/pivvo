# Contributing to PySmith

[![PyPI version](https://img.shields.io/pypi/v/pysmith.svg)](https://pypi.org/project/pysmith/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

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

> Welcome! We're thrilled you're interested in contributing to PySmith. This guide will help you get started with contributing to this Python CLI tool for project initialization and management.

## Table of Contents

- [🎯 Ways to Contribute](#-ways-to-contribute)
- [🚀 Getting Started](#-getting-started)
- [🛠️ Development Setup](#️-development-setup)
- [📝 Coding Standards](#-coding-standards)
- [🧪 Testing](#-testing)
- [🔄 Pull Request Process](#-pull-request-process)
- [🐛 Reporting Issues](#-reporting-issues)
- [📋 Code of Conduct](#-code-of-conduct)
- [🙏 Recognition](#-recognition)

## 🎯 Ways to Contribute

We welcome contributions in various forms:

### 🐛 Bug Reports
- Found a bug? [Open an issue](https://github.com/Flaxmbot/pysmith/issues/new?template=bug_report.md) with detailed steps to reproduce
- Include your Python version, OS, and PySmith version
- Screenshots or error logs are helpful

### ✨ Feature Requests
- Have an idea for a new feature? [Create a feature request](https://github.com/Flaxmbot/pysmith/issues/new?template=feature_request.md)
- Describe the problem it solves and how it would work
- Consider if it aligns with PySmith's goal of streamlining Python project management

### 📚 Documentation
- Improve existing documentation
- Add examples or tutorials
- Translate documentation to other languages
- Fix typos or clarify confusing sections

### 💻 Code Contributions
- Fix bugs or implement new features
- Improve performance or code quality
- Add support for new platforms
- Refactor code for better maintainability

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/Flaxmbot/pysmith.git
   cd pysmith
   ```
3. **Set up your development environment** (see below)
4. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
5. **Make your changes** and ensure tests pass
6. **Commit your changes**:
   ```bash
   git commit -m "Add your descriptive commit message"
   ```
7. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
8. **Open a Pull Request** on the main repository

## 🛠️ Development Setup

### Prerequisites
- Python 3.10 or higher
- Git
- pip (usually included with Python)

### Environment Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Flaxmbot/pysmith.git
   cd pysmith
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - **Windows**:
     ```cmd
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

5. **Install development dependencies**:
   ```bash
   pip install pytest pytest-cov black isort mypy
   ```

6. **Verify installation**:
   ```bash
   pysmith --version
   ```

### Project Structure

```
pysmith/
├── pysmith/
│   ├── __init__.py
│   ├── cli.py          # Main CLI implementation (Typer)
│   └── main.py         # Package entry point
├── tests/              # Unit tests (pytest)
├── requirements.txt    # Dependencies
├── pyproject.toml      # Package configuration
├── LICENSE
├── CONTRIBUTING.md
└── README.md
```

## 📝 Coding Standards

We follow Python best practices to maintain high code quality:

### Style Guidelines
- **PEP 8**: Follow Python's official style guide
- **Type Hints**: Use type annotations for function parameters and return values
- **Docstrings**: Document all public functions, classes, and modules using Google-style docstrings
- **Line Length**: Keep lines under 88 characters (Black default)

### Code Formatting
We use automated tools to ensure consistent formatting:

- **Black**: Code formatter
- **isort**: Import sorter
- **mypy**: Static type checker

Run formatting before committing:
```bash
black pysmith/
isort pysmith/
mypy pysmith/
```

### Naming Conventions
- **Variables/Functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Modules**: `snake_case`

### Commit Messages
Follow conventional commit format:
```
type(scope): description

[optional body]

[optional footer]
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## 🧪 Testing

We use pytest for testing with coverage reporting.

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pysmith --cov-report=html

# Run specific test file
pytest tests/test_cli.py

# Run tests matching pattern
pytest -k "test_init"
```

### Writing Tests
- Place tests in the `tests/` directory
- Name test files as `test_*.py`
- Use descriptive test function names: `test_function_name_should_do_something`
- Aim for high test coverage (>80%)
- Test both success and failure cases
- Mock external dependencies when appropriate

### Test Structure
```python
import pytest
from pysmith.cli import app

def test_command_success():
    # Test successful execution
    pass

def test_command_failure():
    # Test error handling
    pass
```

## 🔄 Pull Request Process

1. **Ensure your PR is ready**:
   - [ ] Tests pass locally: `pytest`
   - [ ] Code follows style guidelines: `black pysmith/ && isort pysmith/`
   - [ ] Type checking passes: `mypy pysmith/`
   - [ ] Documentation updated if needed
   - [ ] Commit messages are clear and descriptive

2. **Create a Pull Request**:
   - Use a clear, descriptive title
   - Provide detailed description of changes
   - Reference any related issues
   - Include screenshots for UI changes

3. **PR Template**:
   - **What does this PR do?**
   - **Why is this change needed?**
   - **How was this tested?**
   - **Any breaking changes?**
   - **Additional notes**

4. **Review Process**:
   - Maintainers will review your PR
   - Address any requested changes
   - Once approved, your PR will be merged

### Branch Naming
- `feature/description`: New features
- `fix/description`: Bug fixes
- `docs/description`: Documentation changes
- `refactor/description`: Code refactoring

## 🐛 Reporting Issues

### Bug Reports
When reporting bugs, please include:

- **PySmith version**: `pysmith --version`
- **Python version**: `python --version`
- **Operating System**: Windows/macOS/Linux + version
- **Steps to reproduce**: Detailed steps
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Error logs**: Any relevant error messages
- **Screenshots**: If applicable

### Feature Requests
For feature requests, include:

- **Problem**: What's the problem you're trying to solve?
- **Solution**: How would you like it to work?
- **Alternatives**: Any alternative solutions considered?
- **Use case**: How would this benefit users?

## 📋 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/). By participating, you agree to:

- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards other contributors
- Help create a positive community

## 🙏 Recognition

We appreciate all contributions, big and small! Contributors will be:

- Listed in the project's contributors file
- Mentioned in release notes
- Recognized in the README
- Invited to join as maintainers for significant contributions

### Hall of Fame

Special thanks to our top contributors:

- **Devrat Kuntal** - Creator & Lead Developer

---

<div align="center">
  <p>Made with ❤️ by the PySmith community</p>
  <p>
    <a href="#contributing-to-pysmith">Back to top</a> •
    <a href="https://github.com/Flaxmbot/pysmith/issues">Report Issue</a> •
    <a href="https://github.com/Flaxmbot/pysmith/discussions">Start Discussion</a>
  </p>
</div>

# Contributing to Embed Cost Estimator
Thank you for your interest in improving **Embed Cost Estimator** 
We welcome contributions of all kinds—from bug reports and feature requests to code fixes and documentation improvements.

## Getting Started
1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
```bash
git clone git@github.com:<your-username>/embedding-cost-calc.git
cd embedding-cost-calc
```
3. **Create** a feature branch:
```bash
git checkout -b feat/my-feature
```

## Reporting Bugs
If you encounter a problem, please open an issue with:
- A clear and descriptive title
- A minimal code snippet or steps to reproduce the bug
- Expected vs. actual behaviour
- Any relevant logs or error messages

## Suggesting Enhancements
For new features of API changes, please open an issue first to discuss:
- The motivation for the change
- Proposed implementation approach
- Any backwards-compatibility considerations

## Development Setup
We use [Poetry](https://python-poetry.org/) for dependency management and packaging:
```bash
# Install project dependencies
poetry install

# Enter the virtual environment
poetry shell
```
If you prefer `pip` and `venv`:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install poetry build flake8 black pytest
poetry install --no-dev # or pip install -e
```

## Running Tests and Linting
Before submitting your changes, ensure everything passes:
```bash
# Run the full test suite
pytest --maxfail=1 --disable-warnings -q

# Check coverage for estimator module
pytest --cov=embed_cost.estimator --cov-report=term-missing

# Lint with Flake8
flake8 src/embed_cost tests

# Format-check with Black
black --check .
```

## Code Style Guidelines
- **Formatting:** We use [Black](https://black.readthedocs.io/en/stable/) - no custom style
- **Linting:** We enforce PEP-8 and logic checks via [Flake8](https://flake8.pycqa.org/en/latest/)
- **Imports:**
    - Standard library first
    - Third-party libraries next
    - Local application imports last
- **Line Length** 79 characters
- **Docstrings:** Use [PEP-257](https://peps.python.org/pep-0257/)

## Commit Message Conventions
We follow a lightweight [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) style:
```bash
<type>(<scope>): <short description>

[optional body]

[optional footer(s)]
```
- **type:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- **scope:** the module or feature affected (eg. `estimator`, `cli`)
- **short description:** imperative, no trailing period
- **body:** motivation and contrast with previous behaviour
- **footer:** references to issues or breaking changes (`BREAKING CHANGE:`)
```bash
feat(estimator): infer mode from chunk_texts vs. num_chunks

BREAKING CHANGE: `precise` flag removed. Callers must now supply
`chunk_texts=` for precise mode or `num_chunks=` for rough mode.
```

## Pull Request Process
1. **Sync** your branch with `main`:
```bash
git fetch upstream
git rebase upstream/main
```
2. **Run** tests, lint, and format checks locally
3. **Push** your branch to your fork and open a PR against `main`
4. In your PR description, link relevant issues and describe your changes clearly
5. A reviewer will provide feedback; please address any requested changes

## Versioning and Releases

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR** version when you make incompatible API changes  
- **MINOR** version when you add functionality in a backwards-compatible manner  
- **PATCH** version when you make backwards-compatible bug fixes

After merging features or fixes, bump the version using Poetry:

```bash
# patch release (0.1.0 → 0.1.1)
poetry version patch

# minor release (0.1.0 → 0.2.0)
poetry version minor

# major release (0.1.0 → 1.0.0)
poetry version major
```

Then update `CHANGELOG.md`, commit, tag and publish:
```bash
git add pyproject.toml CHANGELOG.md
git commit -m "chore: release vX.Y.Z"
git tag vX.Y.Z
git push origin main --tags
poetry publish
```

## License
By contributing, you agree that your contributions will be licensed under the project's MIT License
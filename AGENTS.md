# API Parity

Python CLI and library for comparing HTTP API responses across versions or implementations.

## Development

The project uses `uv` for dependency management, `pytest` for tests, `ruff` for linting, and `mypy` for type checking.

```bash
uv sync
uv run pytest
uv run ruff check .
uv run mypy src
```

## Architecture

- Keep HTTP transport, response comparison, and CLI output separate.
- Core comparison logic must work independently of the CLI.
- Avoid framework-specific assumptions and unnecessary dependencies.
- Keep the public Python API stable once released.

## Testing

- Mock HTTP interactions; tests should not depend on external services.
- Cover response mismatches, malformed data, and network failures.
- Use fixtures for representative API responses.

## Working conventions

- Follow existing patterns before introducing new abstractions.
- Keep changes within the scope of the current issue.
- Do not commit, push, or modify unrelated files unless requested.

Feature requirements and acceptance criteria belong in GitHub Issues, not this file.
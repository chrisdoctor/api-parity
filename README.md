
# API Parity

A Python CLI and library for comparing HTTP responses across API implementations.

The goal is to catch behavioral differences when migrating, upgrading, or refactoring an API.

## Status

Early development. The repository currently contains the project scaffold; response comparison is not implemented yet.

## Initial scope

- Fetch responses from a baseline API and a candidate API.
- Compare HTTP status codes and JSON response bodies.
- Report field-level differences in the terminal.
- Return an appropriate exit code for CI use.

Follow-up work will cover ignored fields, reusable test cases, and structured reports.

## Development

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

Install dependencies and run the current CLI:

```bash
uv sync
uv run api-parity
```

The CLI currently prints a placeholder message.

Static checks:

```bash
uv run ruff check .
uv run mypy src
```

install:
	uv sync

run-gendiff:
	uv run gendiff -h

test:
	uv run pytest

lint:
	uv run ruff check

build:
	uv build
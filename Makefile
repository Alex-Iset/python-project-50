install:
	uv sync

run-gd-help:
	uv run gendiff -h

run-gd:
	uv run gendiff -d tests/test_data/file1.json tests/test_data/file2.json

read-files:
	uv run gendiff --file tests/test_data/file1.json
	uv run gendiff --file tests/test_data/file2.json

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

lint:
	uv run ruff check

build:
	uv build
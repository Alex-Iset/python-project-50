install:
	uv sync

run-help-gd:
	uv run gendiff -h

run-json-gd:
	uv run gendiff tests/test_data/file1.json tests/test_data/file2.json

run-yaml-gd:
	uv run gendiff tests/test_data/file1.yaml tests/test_data/file2.yaml

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

build:
	uv build
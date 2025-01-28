install:
	uv sync

run-help-gd:
	uv run gendiff -h

run-stylish:
	uv run gendiff -f stylish tests/test_data/file1.json tests/test_data/file2.json

run-plain:
	uv run gendiff -f plain tests/test_data/file1.json tests/test_data/file2.json

run-json_form:
	uv run gendiff -f json tests/test_data/file1.json tests/test_data/file2.json

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
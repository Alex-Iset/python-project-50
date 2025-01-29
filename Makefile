install:
	uv sync

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

package-install:
	uv tool install dist/*.whl

package-uninstall:
	uv tool uninstall dist/*.whl

run-help:
	uv run gendiff -h

run-stylish:
	uv run gendiff -f stylish tests/fixtures/file1.json tests/fixtures/file2.json

run-plain:
	uv run gendiff -f plain tests/fixtures/file1.json tests/fixtures/file2.json

run-json:
	uv run gendiff -f json tests/fixtures/file1.json tests/fixtures/file2.json
install:
	uv sync

run-gd-help:
	uv run gendiff -h

run-jgd:
	uv run gendiff -j tests/test_data/file1.json tests/test_data/file2.json

run-ygd:
	uv run gendiff -y tests/test_data/file1.yaml tests/test_data/file2.yaml

read-files:
	uv run gendiff --jfile tests/test_data/file1.json
	uv run gendiff --jfile tests/test_data/file2.json
	uv run gendiff --yfile tests/test_data/file1.yaml
	uv run gendiff --yfile tests/test_data/file2.yaml

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

lint:
	uv run ruff check

build:
	uv build
install:
	uv sync

run-gd-help:
	uv run gendiff -h

run-gd:
	uv run gendiff -d gendiff/json_files/file1.json gendiff/json_files/file2.json

read-gd-files:
	uv run gendiff --file gendiff/json_files/file1.json
	uv run gendiff --file gendiff/json_files/file2.json

test:
	uv run pytest

lint:
	uv run ruff check

build:
	uv build
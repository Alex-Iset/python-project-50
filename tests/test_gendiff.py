from pathlib import Path

import pytest

from gendiff.generate_diff import generate_diff
from gendiff.parser import file_loader


def get_path(fixture_name):
    base_dir = Path(__file__).resolve().parent / 'fixtures'
    return base_dir / fixture_name


@pytest.mark.parametrize(
    "file1, file2, output, formatter",
    [
        (
            # stylish (json)
            get_path("file1.json"),
            get_path("file2.json"),
            get_path("stylish_output.txt"),
            "stylish"
        ),
        (
            # stylish (yaml)
            get_path("file1.yaml"),
            get_path("file2.yaml"),
            get_path("stylish_output.txt"),
            "stylish"
        ),
        (
            # plain (json)
            get_path("file1.json"),
            get_path("file2.json"),
            get_path("plain_output.txt"),
            "plain"
        ),
        (
            # plain (yaml)
            get_path("file1.yaml"),
            get_path("file2.yaml"),
            get_path("plain_output.txt"),
            "plain"
        ),
        (
            # json_format (json)
            get_path("file1.json"),
            get_path("file2.json"),
            get_path("json_format_output.txt"),
            "json"
        ),
        (
            # json_format (yaml)
            get_path("file1.yaml"),
            get_path("file2.yaml"),
            get_path("json_format_output.txt"),
            "json"
        )
    ]
)
def test_gendiff(file1, file2, output, formatter):
    load_output_file = file_loader(output)
    assert generate_diff(
        file1, file2, formatter=formatter
    ) == load_output_file

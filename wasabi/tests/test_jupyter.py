from pathlib import Path
import subprocess

TEST_DATA = Path(__file__).absolute().parent / "test-data"


def test_jupyter():
    result = subprocess.run(
        [
            "jupyter",
            "nbconvert",
            TEST_DATA / "wasabi-test-notebook.ipynb",
            "--execute",
            "--stdout",
            "--to",
            "notebook",
        ],
        check=True,
    )

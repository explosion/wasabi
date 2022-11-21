import pytest

from pathlib import Path
import subprocess
import os
import shutil

import wasabi

jupyter_missing = shutil.which("jupyter") is None

TEST_DATA = Path(__file__).absolute().parent / "test-data"
WASABI_DIR = Path(wasabi.__file__).absolute().parent.parent


@pytest.mark.skipif(jupyter_missing, reason="no jupyter install")
def test_jupyter():
    # Make sure that the notebook can 'import wasabi', and will get the version of
    # wasabi under test. (Important if we're running tests out of the source tree.)
    env = dict(os.environ)
    if "PYTHONPATH" in env:
        env["PYTHONPATH"] = f"{WASABI_DIR}{os.pathsep}{env['PYTHONPATH']}"
    else:
        env["PYTHONPATH"] = str(WASABI_DIR)
    subprocess.run(
        [
            "jupyter",
            "nbconvert",
            str(TEST_DATA / "wasabi-test-notebook.ipynb"),
            "--execute",
            "--stdout",
            "--to",
            "notebook",
        ],
        env=env,
        check=True,
    )

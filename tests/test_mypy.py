# mypy: ignore-errors


import subprocess

from pexpect import EOF

import conftest

def test_mypy_1_pt() -> None:
    cmd = conftest.Console("mypy --exclude 'test' --strict . ", timeout=30)
    assert "Success: no issues found" in cmd, "mypy validation failed"


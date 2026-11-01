# mypy: ignore-errors


import sys
from typing import Any, Callable

import pexpect


def pytest_assertrepr_compare(op: Any, left: Any, right: Any) -> list[str] | None:
    """ Print captured output if we failed to find anything """
    if isinstance(right, pexpect.spawn) and op == "in":
        return ([f"output matches '{left}'", f"Actual output: "] +
                right.before.decode().splitlines()[-3:])
    return None

def verify(fn: Callable[[], None]) -> None:
    """
    Re-throws any underlying exceptions with stack traces removed for brevity.
    """
    __tracebackhide__ = True
    try:
        fn()
    except AssertionError as e:
        raise AssertionError(str(e)) from None

class Console(pexpect.spawn):
    """
    Subclass of pexepect.spawn to allow nicer integration with pytest.
    Supports matching with '<expected value>' in Console and doesn't throw
    exceptions, since unmatched elements will throw AssertionErrors.
    """

    def __init__(self, command: str, timeout: int = 5) -> None:
        super().__init__(command=command,
                         logfile=sys.stdout.buffer,
                         echo=False,
                         timeout=timeout)

    def __contains__(self, item: Any) -> Any:
        """ Allow pytest assert statements like 'whatever' in cmd """
        try:
            super().expect(item)
            return self.match
        except pexpect.exceptions.ExceptionPexpect:
            return None  # EOF & TIMEOUT will just fail assertions

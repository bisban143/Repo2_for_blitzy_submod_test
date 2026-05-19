"""Tests for the Runtime Context Output feature in hello_world.py.

Validates that hello_world.main() emits five new lines with the prefixes
Host:, Working directory:, Timezone:, Date:, Time: — in addition to
preserving the existing greetings and runtime-version output.

Part of the cross-submodule "Runtime Context Output" feature added in
parallel to repo1-java21/test/java/com/example/HelloWorldFeatureTest.java
and repo1-java11/test/java/com/example/HelloWorldFeatureTest.java to
preserve the F-011 "Multilingual Console Output Parity" contract.
"""

import re

import hello_world


def test_prints_host_date_and_time(capsys):
    """Verifies that main() emits Host / Working directory / Timezone / Date / Time lines.

    Also verifies backward compatibility by checking that the original
    English greeting and the Python runtime-version line remain present.
    """
    hello_world.main()
    captured = capsys.readouterr().out

    # AAP §0.6.2.1 Submodule Parity Rule — these prefixes MUST match
    # exactly across all three submodules (Java 21, Java 11, Python).
    assert "Host:" in captured
    assert "Working directory:" in captured
    assert "Timezone:" in captured

    # AAP §0.4.2.5 — Date and Time format regex conformance.
    # Use re.search (not re.match) because the markers appear in the
    # middle of the output, not at the start.
    assert re.search(r"Date: \d{4}-\d{2}-\d{2}", captured) is not None
    assert re.search(r"Time: \d{2}:\d{2}:\d{2}", captured) is not None

    # AAP §0.6.2.5 Backward Compatibility Rule — existing output preserved.
    assert "Hello, World!" in captured
    assert "Running on: Python" in captured

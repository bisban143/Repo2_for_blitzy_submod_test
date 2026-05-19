"""
HelloWorld — requires Python 3.10+.

Uses modern Python features:
  • Dataclasses        (Python 3.7+)
  • Match statements   (Python 3.10+)
  • F-strings          (Python 3.6+)
  • zoneinfo           (Python 3.9+)
"""

from dataclasses import dataclass
import os
import socket
import sys
from datetime import datetime
from zoneinfo import ZoneInfo


@dataclass
class Greeting:
    """A simple dataclass — similar to Java records."""
    language: str
    message: str


def print_runtime_context() -> None:
    """Print the host's current location, current date, and current time.

    Emits five lines to standard output describing the runtime context in
    which this script is executing:

      1. ``Host: <hostname>``           — the local machine's hostname.
      2. ``Working directory: <cwd>``   — the process's current working dir.
      3. ``Timezone: <zone-id>``        — the local IANA timezone identifier
                                          (e.g., ``"UTC"`` or
                                          ``"America/Los_Angeles"``), falling
                                          back to the symbolic name returned
                                          by :py:meth:`datetime.tzname` if no
                                          IANA database key is available.
      4. ``Date: YYYY-MM-DD``           — the current local calendar date in
                                          ISO-8601 format.
      5. ``Time: HH:MM:SS``             — the current local wall-clock time
                                          on the 24-hour clock with zero-
                                          padded fields and no fractional
                                          seconds.

    Added as part of the cross-submodule "Runtime Context Output" feature.
    Uses only Python standard-library APIs (:mod:`os`, :mod:`socket`,
    :mod:`datetime`, :mod:`zoneinfo`) and therefore introduces no new runtime
    dependencies.

    The function is invoked from :func:`main` after the greetings have been
    printed and before the interpreter-version line, so the
    ``"Running on: Python ..."`` line remains the final line of output —
    preserving the "Multilingual Console Output Parity" contract that this
    file shares with its sibling Java submodules.
    """
    # socket.gethostname() normally returns a non-empty identifier even when
    # DNS resolution is unavailable (e.g., it returns "localhost" or a
    # synthesised name). However, on rare platforms or in stripped-down
    # container images the call may raise OSError or return an empty
    # string — for example, when the kernel's UTS namespace hostname is
    # unset. Wrap the lookup defensively and fall back to the literal
    # string "unknown" so the feature always emits a Host: line that is
    # both non-empty and unambiguous, preserving the cross-submodule
    # output-parity contract with the Java siblings.
    try:
        hostname = socket.gethostname() or "unknown"
    except OSError:
        hostname = "unknown"

    # os.getcwd() reads the process's current working directory. It only
    # raises FileNotFoundError if the cwd has been unlinked out from under
    # the process — an exceedingly rare scenario not worth guarding against
    # in a demonstration program.
    cwd = os.getcwd()

    # datetime.now().astimezone() returns a timezone-aware datetime carrying
    # the system's local timezone object. On modern Linux distributions and
    # macOS, this is typically a ``zoneinfo.ZoneInfo`` instance derived from
    # /etc/localtime and exposes a ``.key`` attribute with the IANA zone id.
    now = datetime.now().astimezone()

    # Best-effort extraction of the timezone identifier with graceful
    # degradation across platforms:
    #
    #   * Preferred: a ``ZoneInfo`` instance whose ``.key`` gives the IANA
    #     identifier ("UTC", "America/Los_Angeles", ...).
    #   * Fallback 1: ``datetime.tzname()`` — synthesises an offset-based
    #     name such as "UTC+00:00" when no IANA database is mounted (e.g.,
    #     in stripped-down container images).
    #   * Fallback 2: the literal string ``"unknown"`` — only reached when
    #     both of the above return falsy values, which should not occur on
    #     any supported runtime but is included for defensive completeness.
    tzinfo = now.tzinfo
    if isinstance(tzinfo, ZoneInfo):
        timezone_id = tzinfo.key
    else:
        timezone_id = now.tzname() or "unknown"

    print(f"Host: {hostname}")
    print(f"Working directory: {cwd}")
    print(f"Timezone: {timezone_id}")
    print(f"Date: {now.date().isoformat()}")
    print(f"Time: {now.strftime('%H:%M:%S')}")


def main():
    # Multi-line string
    banner = """
╔══════════════════════════════════╗
║  Hello World — Python 3.10+ Ed.  ║
╚══════════════════════════════════╝
"""

    print(banner)

    # Pattern-matching (match-case) — Python 3.10+
    greetings = [
        Greeting("English", "Hello, World!"),
        Greeting("Spanish", "¡Hola, Mundo!"),
        Greeting("Japanese", "こんにちは、世界！"),
        Greeting("Portuguese", "Olá, Mundo!"),
    ]

    for g in greetings:
        match g.language:
            case "English":
                line = f"🇬🇧  {g.message}"
            case "Spanish":
                line = f"🇪🇸  {g.message}"
            case "Japanese":
                line = f"🇯🇵  {g.message}"
            case "Portuguese":
                line = f"🇧🇷  {g.message}"
            case _:
                line = f"🌍  {g.message}"
        print(line)

    # Emit the new runtime context (host, working directory, timezone,
    # date, time) before the runtime-version line so that the
    # "Running on: Python ..." line remains the final line of output —
    # preserving the cross-submodule output-parity contract.
    print_runtime_context()

    print(f"\nRunning on: Python {sys.version}")


if __name__ == "__main__":
    main()

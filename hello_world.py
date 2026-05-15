"""
HelloWorld — requires Python 3.10+.

Uses modern Python features:
  • Dataclasses        (Python 3.7+)
  • Match statements   (Python 3.10+)
  • F-strings          (Python 3.6+)
"""

from dataclasses import dataclass
import sys


@dataclass
class Greeting:
    """A simple dataclass — similar to Java records."""
    language: str
    message: str


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

    print(f"\nRunning on: Python {sys.version}")


if __name__ == "__main__":
    main()

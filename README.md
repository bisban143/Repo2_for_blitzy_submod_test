# Hello World — Python 3.10+ Edition

A simple "Hello World" application showcasing modern Python features.

## Features

This application demonstrates:
- **Dataclasses** (Python 3.7+) — Similar to Java records
- **Match statements** (Python 3.10+) — Pattern matching
- **F-strings** (Python 3.6+) — String interpolation
- **Runtime Context Output** — Prints the host, working directory, timezone, current date, and current time after the greetings

## Requirements

- Python 3.10 or higher

## Running

```bash
python hello_world.py
```

## Output

The program prints, in order:

1. A decorative banner
2. Four multilingual greetings (English 🇬🇧, Spanish 🇪🇸, Japanese 🇯🇵, Portuguese 🇧🇷)
3. The host runtime context — five lines with the prefixes:
   - `Host: <hostname>`
   - `Working directory: <cwd>`
   - `Timezone: <zone-id>`
   - `Date: YYYY-MM-DD`
   - `Time: HH:MM:SS`
4. The active Python interpreter version (`Running on: Python ...`)

## Testing

Automated tests are organized under a literal `test/` directory at the submodule root (per the user-mandated convention — pytest discovers tests from this location).

### Installing dev dependencies

```bash
pip install -r requirements-dev.txt
```

This installs `pytest` (declared in `requirements-dev.txt`).

### Running the tests

```bash
pytest test/
```

The test suite (`test/test_hello_world.py`) captures the program's standard-output via the `capsys` fixture and asserts that:

- The output contains the markers `Host:`, `Working directory:`, and `Timezone:`
- The output contains a `Date:` line matching the regex `\d{4}-\d{2}-\d{2}`
- The output contains a `Time:` line matching the regex `\d{2}:\d{2}:\d{2}`

### Test Evidence (Screenshots)

Test/run output captures are persisted under `test/screenshot/`:

- `test/screenshot/run-output.txt` — captured stdout from `python hello_world.py`
- `test/screenshot/test-output.txt` — captured stdout from `pytest`

These files are automatically populated and committed back by the GitHub Actions workflow (`.github/workflows/build.yml`) on each green CI run, and are also published as a downloadable workflow artifact (`screenshot-evidence-python`).

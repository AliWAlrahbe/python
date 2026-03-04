# Log Parser

Simple Python CLI script to scan a log file and count keyword matches.

## What It Does

- Reads a log file line by line (memory-friendly).
- Searches for one or more keywords (case-insensitive).
- Writes matched lines to `report.txt`.
- Appends a final summary dictionary with total counts per keyword.

## Requirements

- Python 3.x

## Usage

Run from this folder:

```powershell
py logParser.py <logfile> <keyword1> <keyword2> ...
```

Example:

```powershell
py logParser.py app.log ERROR Failed
```

## Arguments

- `logfile`: path to input log file (required)
- `keywords`: one or more search terms (required)

## Output

The script creates/overwrites:

- `report.txt`

`report.txt` contains:

1. One line per match in this format:
   `line # <n> <date> -- <time> match: <keyword>`
2. Final summary line, for example:
   `{'error': 6, 'failed': 2}`

## Notes

- Matching is case-insensitive.
- Punctuation around tokens is stripped before matching.
- If the input file is missing or invalid, the script prints an error and exits.

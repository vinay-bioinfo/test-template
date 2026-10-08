# Data Processing Script Template

A small, dependency-free Python starter project for processing CSV files. The
example trims whitespace from each CSV value; replace `process_row` with the
transformations your data needs.

## Project structure

```text
.
├── data/
│   ├── processed/       # Processed output files
│   └── raw/             # Input files (keep original data unchanged)
├── src/
│   └── data_processing.py
└── tests/
    └── test_data_processing.py
```

## Usage

Requires Python 3.8 or later. Place an input CSV in `data/raw/`, then run:

```bash
python src/data_processing.py data/raw/input.csv data/processed/output.csv
```

The script preserves the CSV columns and row order while trimming leading and
trailing whitespace from values. Keep source data in `data/raw/` and write
results to `data/processed/`.

## Tests

Run the tests using Python's standard-library test runner:

```bash
python -m unittest discover -s tests -v
```

Add tests in `tests/` whenever you add or change processing behavior.
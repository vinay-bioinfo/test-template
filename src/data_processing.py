"""CSV processing starter script."""

import argparse
import csv
from pathlib import Path


def process_row(row):
    """Trim surrounding whitespace from each CSV value."""
    return {
        key: value.strip() if isinstance(value, str) else value
        for key, value in row.items()
    }


def process_csv(input_path, output_path):
    """Process a CSV file and write the result to a separate file."""
    input_path = Path(input_path)
    output_path = Path(output_path)
    if input_path.resolve() == output_path.resolve():
        raise ValueError("Input and output files must be different")

    with input_path.open(newline="", encoding="utf-8") as input_file:
        reader = csv.DictReader(input_file)
        if reader.fieldnames is None:
            raise ValueError("Input CSV must include a header row")
        rows = [process_row(row) for row in reader]

    with output_path.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description="Process a CSV file.")
    parser.add_argument("input", help="Path to the input CSV file")
    parser.add_argument("output", help="Path to the output CSV file")
    args = parser.parse_args()
    process_csv(args.input, args.output)


if __name__ == "__main__":
    main()

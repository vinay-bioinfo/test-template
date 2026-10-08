import csv
import tempfile
import unittest
from pathlib import Path

from src.data_processing import process_csv, process_row


class ProcessRowTests(unittest.TestCase):
    def test_trims_string_values(self):
        self.assertEqual(
            process_row({"name": "  Ada ", "count": "2"}),
            {"name": "Ada", "count": "2"},
        )


class ProcessCsvTests(unittest.TestCase):
    def test_processes_csv_and_preserves_columns(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            input_path = Path(temporary_directory) / "input.csv"
            output_path = Path(temporary_directory) / "output.csv"
            input_path.write_text("name,count\n Ada , 2 \n", encoding="utf-8")

            process_csv(input_path, output_path)

            with output_path.open(newline="", encoding="utf-8") as output_file:
                rows = list(csv.DictReader(output_file))
            self.assertEqual(rows, [{"name": "Ada", "count": "2"}])

    def test_rejects_same_input_and_output(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            input_path = Path(temporary_directory) / "input.csv"
            input_path.write_text("name\nAda\n", encoding="utf-8")

            with self.assertRaises(ValueError):
                process_csv(input_path, input_path)

    def test_rejects_csv_without_header(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            input_path = Path(temporary_directory) / "input.csv"
            output_path = Path(temporary_directory) / "output.csv"
            input_path.write_text("", encoding="utf-8")

            with self.assertRaises(ValueError):
                process_csv(input_path, output_path)


if __name__ == "__main__":
    unittest.main()

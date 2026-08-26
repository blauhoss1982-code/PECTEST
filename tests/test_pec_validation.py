from pathlib import Path
import unittest


EXPECTED = b"PEC_VALIDATION_FIRST_OK\nPEC_VALIDATION_SECOND_OK\n"
VALIDATION_FILE = Path(__file__).resolve().parents[1] / "pec-validation.txt"


class PecValidationTest(unittest.TestCase):
    def test_exact_final_bytes(self):
        self.assertEqual(VALIDATION_FILE.read_bytes(), EXPECTED)


if __name__ == "__main__":
    unittest.main()

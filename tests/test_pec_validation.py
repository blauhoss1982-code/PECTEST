from pathlib import Path


EXPECTED = b"PEC_VALIDATION_FIRST_OK\nPEC_VALIDATION_SECOND_OK\n"
VALIDATION_FILE = Path(__file__).resolve().parents[1] / "pec-validation.txt"


actual = VALIDATION_FILE.read_bytes()
assert actual == EXPECTED, actual
print("PASS checkpoint-b validation")

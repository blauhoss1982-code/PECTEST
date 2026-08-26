from pathlib import Path


EXPECTED = b"PEC_VALIDATION_FIRST_OK\nPEC_VALIDATION_SECOND_OK\n"
validation_file = Path(__file__).resolve().parents[1] / "pec-validation.txt"
actual = validation_file.read_bytes()
assert actual == EXPECTED, actual
print("PASS checkpoint-b pec-validation bytes")

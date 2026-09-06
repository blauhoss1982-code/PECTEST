from pathlib import Path
import unittest


class ExecutorFirstRerunOneTest(unittest.TestCase):
    def test_exact_bytes(self):
        artifact = Path(__file__).resolve().parents[1] / "e2e-executor-first-rerun-1.txt"
        self.assertEqual(artifact.read_bytes(), b"PECTEST_EXECUTOR_FIRST_E2E_RERUN_1_OK\n")


if __name__ == "__main__":
    unittest.main()

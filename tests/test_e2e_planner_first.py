from pathlib import Path
import unittest


class PlannerFirstTest(unittest.TestCase):
    def test_exact_bytes(self):
        artifact = Path(__file__).resolve().parents[1] / "e2e-planner-first.txt"
        self.assertEqual(artifact.read_bytes(), b"PECTEST_PLANNER_FIRST_E2E_OK\n")


if __name__ == "__main__":
    unittest.main()

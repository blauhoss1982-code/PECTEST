from pathlib import Path
import unittest


class ExecutorFirstArtifactTest(unittest.TestCase):
    def test_artifact_has_exact_bytes(self):
        artifact = Path(__file__).resolve().parents[1] / "e2e-executor-first.txt"
        self.assertEqual(
            artifact.read_bytes(),
            b"PECTEST_EXECUTOR_FIRST_E2E_OK\n",
        )


if __name__ == "__main__":
    unittest.main()

import unittest
from pathlib import Path
from src import utils

PROJECT_ROOT = Path(__file__).resolve().parent.parent


class TestUtils(unittest.TestCase):

    def test_search_file(self):
        expected = "w1_slave"
        actual = utils.search_file(
            PROJECT_ROOT / "tests" / "fixtures" / "test_device", expected
        )[0].name
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

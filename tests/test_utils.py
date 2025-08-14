import unittest
from pathlib import Path
from src import utils
from src import exceptions

PROJECT_ROOT = Path(__file__).resolve().parent.parent


class TestUtils(unittest.TestCase):

    def test_search_file(self):
        expected = "w1_slave"
        actual = utils.search_file(
            PROJECT_ROOT / "tests" / "fixtures" / "test_device" / "sys", expected
        )[0].name
        self.assertEqual(actual, expected)

    def test_parse_temp_in_cesius(self):
        expected = 31.375
        w1_slave_file = (
            PROJECT_ROOT
            / "tests/fixtures/test_device/sys/bus/w1/devices/10-000803cd476f/w1_slave"
        )
        actual = utils.parse_temp_in_cesius(w1_slave_file)
        self.assertEqual(actual, expected)

    def test_parse_temp_in_cesius_excpetion(self):
        expected = 31.375
        w1_slave_file = PROJECT_ROOT / "tests/fixtures/test_device/w1_slave_fail"
        with self.assertRaises(exceptions.CRCError):
            utils.parse_temp_in_cesius(w1_slave_file)


if __name__ == "__main__":
    unittest.main()

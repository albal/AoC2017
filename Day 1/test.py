from main import *
import unittest

if __name__ == '__main__':
    unittest.main()


class TestDay1Part1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(part_one("1122"), 3, "Should be 3")

    def test_2(self):
        self.assertEqual(part_one("1111"), 4, "Should be 4")

    def test_3(self):
        self.assertEqual(part_one("1234"), 0, "Should be 0")

    def test_4(self):
        self.assertEqual(part_one("91212129"), 9, "Should be 9")
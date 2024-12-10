import unittest
from caradura import day_03

class Day3Test(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_part_one(self):
        total = day_03.part_one(["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"])

        self.assertEqual(161, total)

    def test_dont_do_extract(self):
        matches = day_03.extract_mul_do_dont_instructions("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+do()mul(2,3)")
        self.assertEqual(["mul(2,4)", "don't()", "mul(5,5)", "do()", "mul(2,3)"], matches)

    def test_do_extract(self):
        matches = day_03.extract_mul_do_dont_instructions("do()mul(2,3)")
        self.assertEqual(["do()", "mul(2,3)"], matches)

    def test_part_two_1(self):
        total = day_03.part_two(["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"])
        self.assertEqual(48, total)

    def test_part_two_2(self):
        total = day_03.part_two(["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+do()mul(2,3)(mul(11,8)undo()?mul(8,5))"])
        self.assertEqual(2*4 + 2*3 + 11*8 + 8*5, total)

    def test_part_two_3(self):
        total = day_03.part_two(["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)", "+mul(32,64](mul(11,8)undo()?mul(8,5))"])
        self.assertEqual(48, total)

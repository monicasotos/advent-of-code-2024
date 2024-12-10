import unittest
from caradura import day_04

complexGridExample = """
MMMMASXMMM
MAAXMXMAAA
MSSSMMSSMM
XMAMAAXXMM
MMAMSXSAMA
"""

simpleGridExample = [
    ["M", ".", "M"],
    [".", "A", "."],
    ["S", ".", "S"],
]

simpleGridExample2 = [
    ["M", ".", "S"],
    [".", "A", "."],
    ["M", ".", "S"],
]

simpleGridExample4 = [
    ["M", ".", "M"],
    [".", "A", "."],
    ["M", ".", "M"],
]

simpleGridExample5 = [
    ["S", ".", "S"],
    [".", "A", "."],
    ["S", ".", "S"],
]

simpleGridExample51 = [
    ["M", "M", "A", "S"],
    ["A", "A", "A", "A"],
    ["S", "M", "S", "S"],
]

simpleGridExample3 = [
    [".", "M", "."],
    ["M", "A", "S"],
    [".", "S", "."],
]

simpleGridExampleWithTwoXmas = [
    ["M", ".", "M", ".", "M", ".", "M", ".", "M"],
    [".", "A", ".", "M", "A", "S", ".", "A", "."],
    ["S", ".", "S", ".", "S", ".", "S", ".", "S"],
]

simpleGridGivenExample = [
    ".M.S......",
    "..A..MSMS.",
    ".M.S.MAA..",
    "..A.ASMSM.",
    ".M.S.M....",
    "..........",
    "S.S.S.S.S.",
    ".A.A.A.A..",
    "M.M.M.M.M.",
]

class Day4TestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_grid(self):
        inputLines = ["....XXMAS.", ".SAMXMS...", "...S..A...", "..A.A.MS.X"];
        grid = day_04.extract_grid(inputLines)
        result = day_04.count_xmas_occurrences(grid, "XMAS")

        self.assertEqual(3, result)

    def test_matrix1(self):
        count = day_04.count_xmas(simpleGridExample)
        self.assertEqual(1, count)

    def test_matrix2(self):
        count = day_04.count_xmas(simpleGridExample2)
        self.assertEqual(1, count)

    def test_matrix3(self):
        count = day_04.count_xmas(simpleGridExample3)
        self.assertEqual(0, count)

    def test_matrix4(self):
        count = day_04.count_xmas(simpleGridExampleWithTwoXmas)
        self.assertEqual(2, count)

    def test_matrix5(self):
        count = day_04.count_xmas(simpleGridExample4)
        self.assertEqual(0, count)

    def test_matrix6(self):
        count = day_04.count_xmas(simpleGridExample5)
        self.assertEqual(0, count)

    def test_matrix7(self):
        grid = day_04.extract_grid(simpleGridGivenExample)
        count = day_04.count_xmas(grid)
        self.assertEqual(9, count)

    def test_matrix5_1(self):
        count = day_04.count_xmas(simpleGridExample51)
        self.assertEqual(1, count)

    def test_center_list(self):
        result = day_04.find_center_list(['.', "A", "a", 'c', "A", "."])

        self.assertEqual([1, 4], result)

    def test_south_east(self):
        grid = day_04.extract_grid(simpleGridGivenExample)
        result = day_04.south_east_calculator(grid)

        self.assertEqual(9, result)

if __name__ == '__main__':
    unittest.main()

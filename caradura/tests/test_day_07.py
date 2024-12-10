import unittest
from caradura import day_07
from caradura.day_07 import  Equation

example_simle = [
    "190: 10 19",
    "3267: 81 40 27",
    "83: 17 5",
]

example_complex = [
    "190: 10 19",
    "3267: 81 40 27",
    "83: 17 5",
    "156: 15 6",
    "7290: 6 8 6 15",
    "161011: 16 10 13",
    "192: 17 8 14",
    "21037: 9 7 18 13",
    "292: 11 6 16 20",
]


class Day7TestCase(unittest.TestCase):
    def test_get_calibration_eqs(self):
        expected = [
            Equation(190, [10,19]),
            Equation(3267, [81, 40, 27]),
            Equation(83, [17, 5])
        ]
        equations = day_07.get_calibration_equations(example_simle)
        self.assertEqual(expected, equations)
        
    def test_generate_operations_0(self):
        example = ["190: 10",]
        equation = day_07.get_calibration_equations(list(example))[0]
        all_op_combis = equation.generate_all_operations()
        
        self.assertEqual(set(), all_op_combis)
        
        
    def test_generate_operations_1(self):
        example = ["190: 10 19",]
        equation = day_07.get_calibration_equations(list(example))[0]
        all_op_combis = equation.generate_all_operations()
        
        self.assertEqual({("+",),  ("*",)}, all_op_combis)
        
        is_true = equation.is_true()
        self.assertEqual(True, is_true)
        
        
    def test_generate_operations_2(self):
        example = ["190: 10 19 34",]
        equation = day_07.get_calibration_equations(list(example))[0]
        all_op_combis = equation.generate_all_operations()
        
        self.assertEqual({("+", "+",), ("+", "*"), ("*", "+"), ("*", "*")}, all_op_combis)
    
    
    
    def test_compute_eq_2(self):
        example = ["3267: 81 40 27"]
        equation = day_07.get_calibration_equations(list(example))[0]
        result1 = equation.compute(operations=('*', '+'))
        result2 = equation.compute(operations=('+', '*'))
        self.assertEqual(3267, result1)
        self.assertEqual(3267, result2)
        
        is_true = equation.is_true()
        self.assertEqual(True, is_true)
    
    
    def test_true_eq_2(self):
        example = ["83: 17 5",]
        equation = day_07.get_calibration_equations(example)[0]
        is_true = equation.is_true()
        
        self.assertEqual(False, is_true)
    
    
    def test_part_1(self):
        calibration = day_07.part_one(example_complex)
        self.assertEqual(3749, calibration)
    
    def test_compute_eq_concat_1(self):
        example = ["7290: 6 8 6 15"]
        equation = day_07.get_calibration_equations(list(example))[0]
        result = equation.compute(operations=('*', '||', '*'))
        self.assertEqual(7290, result)
    
    def test_compute_eq_concat_2(self):
        example = ["156: 15 6"]
        equation = day_07.get_calibration_equations(list(example))[0]
        result = equation.compute(operations=('||',))
        self.assertEqual(156, result)
    
    def test_add_concat_operator(self):
        example = ["156: 15 6"]
        equation = day_07.get_calibration_equations(list(example))[0]
        operations = equation.generate_all_operations_with_concat()
        expected_ops = set(
            [("+",), ("*",), ("||",)]
        )
        self.assertEqual(expected_ops, operations)
    
    def test_eq_true_after_concat(self):
        example = ["7290: 6 8 6 15"]
        equation = day_07.get_calibration_equations(list(example))[0]
        is_true = equation.is_true()
        self.assertEqual(False, is_true)
        
        is_now_true = equation.is_true_concat()
        self.assertEqual(True, is_now_true)
    
    def test_part_2(self):
        new_calibration = day_07.part_two(example_complex)
        self.assertEqual(11387, new_calibration)

    
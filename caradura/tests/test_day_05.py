import unittest
from caradura import day_05

simple_rules_1 = """47|53
75|47
97|13
97|61
97|47
75|29
61|13
75|53
97|75
"""

complex_example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
complex_input_lines = complex_example.split("\n")
complex_rules = day_05.get_ordering_rules(complex_input_lines)
complex_updates = day_05.get_updates(complex_input_lines)

simple_input_1_incorrect = [75, 97, 47, 61, 53]
simple_input_2_correct = [75, 47, 61, 53, 29]

class Day5TestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here
    
    def test_get_ordering_rules(self):
        input_lines = """1|2
        2|3
        
        1,2,3"""
        input_lines = input_lines.split("\n")
        rules = day_05.get_ordering_rules(input_lines)
        self.assertEqual([(1, 2), (2, 3)], rules)
    
    def test_get_updates(self):
        input_lines = """1|2
        2|3
        3|4
        
        1,2,3,4"""
        input_lines = input_lines.split("\n")
        rules = day_05.get_updates(input_lines)
        self.assertEqual([[1, 2, 3, 4]], rules)
    
    def test_update_right_order_1(self):
        input_rules = simple_rules_1.split("\n")
        rules = day_05.get_ordering_rules(input_rules)
        is_correct = day_05.verify_updates_order(simple_input_1_incorrect, rules)
        self.assertEqual(False, is_correct)
    
    def test_update_right_order_2(self):
        input_rules = simple_rules_1.split("\n")
        rules = day_05.get_ordering_rules(input_rules)
        is_correct = day_05.verify_updates_order(simple_input_2_correct, rules)
        self.assertEqual(True, is_correct)
    
    def test_update_right_order_3(self):
        example = """1|2
        2|3
        3|4
        4|5
        
        1,2,3,4,5"""
        input_lines = example.split("\n")
        rules = day_05.get_ordering_rules(input_lines)
        is_correct = day_05.verify_updates_order(example, rules)
        self.assertEqual(True, is_correct)
        
    def test_part_one_1(self):
        example = """1|2
        2|3
        3|4
        4|5
        
        1,2,3,4,5"""
        input_lines = example.split("\n")
        sum_medians = day_05.part_one(input_lines)
        self.assertEqual(3, sum_medians)
    
    def test_part_one_complex(self):
        input_lines = complex_example.split("\n")
        sum_medians = day_05.part_one(input_lines)
        self.assertEqual(143, sum_medians)
    
    def test_p2_reordering_easy_1(self):
        example = """1|2
        2|3
        3|4
        1|3
        
        3,2,1,4"""
        input_lines = example.split("\n")
        rules = day_05.get_ordering_rules(input_lines)
        update = day_05.get_updates(input_lines)[0]
        
        new_update = day_05.correct_update(update, rules)
        self.assertEqual([1, 2, 3, 4], new_update)

    def test_p2_reordering_easy_5(self):
        example = """1|2
        2|3
        3|4
        1|3
        
        2,3,1,4"""
        input_lines = example.split("\n")
        
        wrong_update = day_05.get_updates(input_lines)[0]
        rules = day_05.get_ordering_rules(input_lines)
        is_correct = day_05.verify_updates_order(wrong_update, rules)
        
        self.assertEqual(False, is_correct)
    
    def test_p2_reordering_complex_1(self):
        wrong_update = [75,97,47,61,53]
        corrected_update = day_05.correct_update(wrong_update, complex_rules)
        self.assertEqual([97,75,47,61,53], corrected_update)
    
    def test_p2_reordering_complex_2(self):
        wrong_update = [61,13,29]
        corrected_update = day_05.correct_update(wrong_update, complex_rules)
        self.assertEqual([61,29,13], corrected_update)
    
    def test_p2_reordering_complex_3(self):
        wrong_update = [97,13,75,29,47]
        corrected_update = day_05.correct_update(wrong_update, complex_rules)
        self.assertEqual([97,75,47,29,13], corrected_update)
    
    def test_p2_reordering_complex_4(self):
        incorrect_updates = []
        for update in complex_updates:
            is_correct = day_05.verify_updates_order(update, complex_rules)
            if not is_correct:
                incorrect_updates.append(update)
        
        new_updates = []
        for inc_update in incorrect_updates:
            new_update = day_05.correct_update(inc_update, complex_rules)
            new_updates.append(new_update)
        
        expected_updates_corrected = [
            [97,75,47,61,53],
            [61,29,13],
            [97,75,47,29,13],
        ]
        self.assertEqual(expected_updates_corrected, new_updates)
    
    
from caradura.utils import read_input_lines
import regex as re
from dataclasses import dataclass
from itertools import product
from typing import Literal, List, Set, Tuple

@dataclass
class Equation:
    test: int
    values: List[int]
    OPERATORS = ['+', '*']

    def generate_all_operations(self, operators= ['+', '*']) -> Set[Tuple[str, ...]]:
        '''Generates all possible combinations of operations'''
        num_spaces = len(self.values) - 1
        combinations = set(product(operators, repeat=num_spaces)) if num_spaces > 0 else set()
        return set(combinations) if num_spaces > 0 else set()

    def generate_all_operations_with_concat(self) -> Set[Tuple[str, ...]]:
        operators = ['+', '*', '||']
        return self.generate_all_operations(operators)

    def compute(self, operations: Tuple[str, ...]) -> int:
        accumulated = self.values[0]
        for idx, op in enumerate(operations):
            accumulated = self.operate(accumulated, self.values[idx + 1], op)
        return accumulated

    @staticmethod
    def operate(num1: int, num2: int, operation: Literal['*', '+', '||']) -> int:
        if operation == "+":
            return num1 + num2
        elif operation == "*":
            return num1 * num2
        elif operation == "||":
            return int(str(num1) + str(num2))
    

    def is_true(self) -> bool:
        all_operations = self.generate_all_operations()
        if all_operations:
            for ops in all_operations:
                if self.compute(ops) == self.test:
                    return True
        else:
            return self.values[0] == self.test
        return False
    
    def is_true_concat(self) -> bool:
        all_operations = self.generate_all_operations_with_concat()
        if all_operations:
            for ops in all_operations:
                if self.compute(ops) == self.test:
                    return True
        else:
            return self.values[0] == self.test
        return False



def get_calibration_equations(input_lines:list[str]) -> list[Equation]:
    return [
        Equation(int(line.split(':')[0]), [int(cal) for cal in re.findall(r"\d+", line.split(':')[1])])
        for line in input_lines
    ]

def get_false_equations(input_lines:list[str]) -> list[Equation]:
    equations = get_calibration_equations(input_lines)
    true_eqs = [equation for equation in equations if equation.is_true()]
    false_eqs = [equation for equation in equations if equation not in true_eqs]
    return false_eqs
        
######## main funcitons #########


def part_one(input_lines:list[str]) -> int:
    equations = get_calibration_equations(input_lines)
    return sum(equation.test for equation in equations if equation.is_true())


def part_two(input_lines:list[str]) -> int:
    false_equations = get_false_equations(input_lines)
    
    prev_total = part_one(input_lines)
    total_new_eqs = sum([eq.test for eq in false_equations if eq.is_true_concat()])
    return prev_total + total_new_eqs


if __name__ == "__main__":
    input_lines = read_input_lines(day=7)

    total_p1 = part_one(input_lines)
    print(f"(Part 1) Total: {total_p1}")

    total_p2 = part_two(input_lines)
    print(f"(Part 2) Total: {total_p2}")
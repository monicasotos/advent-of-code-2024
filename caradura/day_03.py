# https://adventofcode.com/2024/day/3
from caradura.utils import read_input_lines
import regex as re


def extract_correct_mul_instructions(line:str) -> list[str]:
    '''This extracts all the ocurrences of instructions like "mul(X,Y), where X, Y are integers. It will ignore all corrupted instructions such as "mul ( X Y )", "mul(4*".
    
    It returns a list of non-corrupted instructions of the form `['mul(2,43)', 'mul(23, 45)', ...]`'''
    matches = re.findall(r'mul\(\d+,\d+\)', line)
    return matches

def extract_mul_do_dont_instructions(line:str) -> list[str]:
    '''This extracts all the ocurrences of instructions like "mul(X,Y), where X, Y are integers. It will ignore all corrupted instructions such as "mul ( X Y )", "mul(4*".

    It returns a list of non-corrupted instructions of the form `['mul(2,43)', 'mul(23, 45)', ...]`'''
    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", line)
    return matches


def multiply(element: str) -> int:
    '''The input is of a string of the form "mul(X,Y)", where X, Y are integers. It returns the product of X and Y.'''
    assert re.match(r'mul\(\d+,\d+\)', element), f"Invalid input: {element}"
    nums = re.findall(r'\d+', element)
    return int(nums[0]) * int(nums[1])

def find_enabled_mul(matches:list[str], last_enabled:bool) -> tuple[list[str], bool]:
    enabled = last_enabled
    enabled_muls = []
    for match in matches:
        if match == "do()":
            enabled = True
            continue
        elif match == "don't()":
            enabled = False
            continue

        if enabled == True:
            enabled_muls.append(match)

    return enabled_muls, enabled


###### main functions ######
def part_one(corrupted_instructions) -> int:
    total = 0
    for line in corrupted_instructions:
        non_corrupted_memory = extract_correct_mul_instructions(line)
        memory_sum = sum([multiply(element) for element in non_corrupted_memory])
        total += memory_sum

    return total

def part_two(input_lines) -> int:
    total = 0
    enabled = True
    for line in input_lines:
        matches = extract_mul_do_dont_instructions(line)
        enabled_muls, enabled =  find_enabled_mul(matches, enabled)
        total += sum([multiply(mul) for mul in enabled_muls])

    return total



if __name__ == "__main__":
    input_lines = read_input_lines(day=3)
    total_p1 = part_one(input_lines)
    print(f"(Part 1) Total memory: {total_p1}")

    total_p2 = part_two(input_lines)
    print(f"(Part 2) Total enabled memory: {total_p2}")
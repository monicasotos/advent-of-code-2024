from caradura.utils import read_input_lines
import regex as re
from statistics import median

def get_ordering_rules(input_lines:list[str]) -> list[tuple[int]]:
    rules = []
    for line in input_lines:
        if "|" not in line:
            break
        nums = re.findall(r"\d+", line)
        rule = (int(nums[0]), int(nums[1]))
        rules.append(rule)
    return rules

def get_updates(input_lines:list[str]):
    '''Gets the all the updates only, from the input data'''
    updates = []
    for line in input_lines:
        if "|" in line or line == "\n":
            continue
        update = re.findall(r"\d+", line)
        if not update:
            continue
        update = [int(num) for num in update]
        updates.append(update)
    return updates

        
def verify_updates_order(numbers:list[int], rules:list[tuple[int]]):
    reversed_rules = [(rule[1], rule[0]) for rule in rules]
    for j, number in enumerate(numbers[:-1]):
        next_number = numbers[j + 1]
        if (number, next_number) in reversed_rules:
            return False
    return True

def switch_elements(incorrect_update:list[int],*, idx:int) -> list[int]:
    '''Switches the position of the elements at index `idx` and `idx + 1`'''
    # is_correct = verify_updates_order([num_1, num_2], rules)
    incorrect_update[idx], incorrect_update[idx + 1] = incorrect_update[idx + 1], incorrect_update[idx]
    return incorrect_update.copy()

def correct_update(incorrect_update:list[int], rules:list[tuple[int]]) -> list[int]:
    is_correct = verify_updates_order(incorrect_update, rules)
    if is_correct:
        # or maybe raise error here in case the input is correct
        # assert is_correct is not True, "Input update must be incorrect!"
        return incorrect_update
    
    reversed_rules = [(rule[1], rule[0]) for rule in rules]
    new_update = []
    for j, number in enumerate(incorrect_update[:-1]):
        next_number = incorrect_update[j + 1]
        if (number, next_number) in reversed_rules:
            new_update = switch_elements(incorrect_update, idx=j)
            new_update = correct_update(new_update, rules)
            break
    return new_update
    

###### main functions ######
def part_one(input_lines: list[str]) -> int:
    rules = get_ordering_rules(input_lines)
    list_updates = get_updates(input_lines)
    middle_points = []
    
    for numbers in list_updates:
        is_correct = verify_updates_order(numbers, rules)
        if not is_correct:
            continue
        middle_loc = len(numbers) // 2
        middle = numbers[middle_loc]
        middle_points.append(middle)
        # print(f"The median of {numbers=} is {_median}.")
    
    total = sum(middle_points)
    return total

def part_two(input_lines: list[str]) -> int:
    rules = get_ordering_rules(input_lines)
    list_updates = get_updates(input_lines)
    middle_points = []
    corrected_updates = []
    
    for numbers in list_updates:
        is_correct = verify_updates_order(numbers, rules)
        if is_correct:
            continue
        corrected_update = correct_update(numbers, rules)
        corrected_updates.append(corrected_update)
        
        middle_loc = len(corrected_update) // 2
        middle =  corrected_update[middle_loc]
        middle_points.append(middle)
        # print(f"The median of {numbers=} is {_median}.")
    
    total = sum(middle_points)
    return total


if __name__ == "__main__":
    input_lines = read_input_lines(day=5)

    total_p1 = part_one(input_lines)
    print(f"(Part 1) Total: {total_p1}")

    total_p2 = part_two(input_lines)
    print(f"(Part 2) Total: {total_p2}")



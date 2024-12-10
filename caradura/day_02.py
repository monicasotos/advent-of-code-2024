# https://adventofcode.com/2024/day/2
from utils import read_input_lines


def check_report_is_increasing_or_decreasing(report:list[int]) -> bool:
    sorted_report_asc = sorted(report)
    sorted_report_desc = sorted(report, reverse=True)
    if report == sorted_report_asc or report == sorted_report_desc:
        return True
    return False

def check_adj_levels(report:list[int]) -> bool:
    '''checks that the difference between any two adjacent levels is not smaller than 1, and at most 3'''
    differences = [abs(report[i] - report[i-1]) for i in range(1, len(report))]
    any_smaller_than_one = any([diff < 1 for diff in differences])
    any_bigger_than_three = any([diff > 3 for diff in differences])
    if any_smaller_than_one or any_bigger_than_three:
        return False
    return True

# non_valid_report_example = [1, 2, 7, 8, 9]

def check_report_safety(report:list[int]):
    if not check_report_is_increasing_or_decreasing(report):
        return False
    if not check_adj_levels(report):
        return False
    return True

def new_check_report_safety(report:list[int]):
    '''Checks if report is safe, if it is safe after removing at most one of the levels'''
    old_is_safe = check_report_safety(report)
    if old_is_safe:
        return True
    for i in range(len(report)):
        new_report = report.copy()
        new_report.pop(i)
        if check_report_safety(new_report):
            return True
    return False


###### main functions ######

def part_one(input_lines:list[str]) -> int:
    reports = [[int(num) for num in line.split()] for line in input_lines]
    num_safe_reports = 0
    for report in reports:
        if check_report_safety(report):
            num_safe_reports += 1
    return num_safe_reports

def part_two(input_lines:list[str]) -> int:
    reports = [[int(num) for num in line.split()] for line in input_lines]
    num_safe_reports = 0
    for report in reports:
        if new_check_report_safety(report):
            num_safe_reports += 1
    return num_safe_reports

if __name__ == "__main__":
    input_lines = read_input_lines(day=2)
    
    total_p1 = part_one(input_lines)
    print(f"(Part 1) Total: {total_p1}")
    
    total_p2 = part_two(input_lines)
    print(f"(Part 2) Total: {total_p2}")
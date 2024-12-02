# https://adventofcode.com/2024/day/2

reports_file = "./inputs/day_2.txt"

with open(reports_file) as f:
    content = f.readlines()


reports = [[int(num) for num in line.split()] for line in content]

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

new_valid_report_example = [1, 2, 7, 8, 9]

def old_check_report_safety(report:list[int]):
    if not check_report_is_increasing_or_decreasing(report):
        return False
    if not check_adj_levels(report):
        return False
    return True


def new_check_report_safety(report:list[int]):
    '''Checks if report is safe, if it is safe after removing at most one of the levels'''
    old_is_safe = old_check_report_safety(report)
    if old_is_safe:
        return True
    for i in range(len(report)):
        new_report = report.copy()
        new_report.pop(i)
        if old_check_report_safety(new_report):
            return True
    return False

examples = [[7,6,4,2,1], [1,2,7,8,9], [9,7,6,2,1], [1,3,2,4,5], [8,6,4,4,1], [1,3,6,7,9]]
for report in examples:
    is_valid = new_check_report_safety(report)
    print(f"Report {report} is safe: {is_valid}")
    
num_safe_reports = 0
for report in reports:
    if new_check_report_safety(report):
        num_safe_reports += 1

print(f"Number of safe reports: {num_safe_reports}")
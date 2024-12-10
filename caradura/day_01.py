# https://adventofcode.com/2024/day/1
from utils import read_input_lines

def get_locations(input_lines:list[str]) -> tuple[list, list]:
    locations = [line.split() for line in input_lines]
    locs_list1 = sorted([int(loc[0]) for loc in locations])
    locs_list2 = sorted([int(loc[1]) for loc in locations])
    return locs_list1, locs_list2


###### main functions ######
def part_one(input_lines:list[str]) -> int:
    locs_list1, locs_list2 = get_locations(input_lines)
    distances = [abs(locs_list1[i] - locs_list2[i]) for i in range(len(locs_list1))]
    sum_distances = sum(distances)
    return sum_distances

def part_two(input_lines:list[str]) -> int:
    locs_list1, locs_list2 = get_locations(input_lines)
    scores = {}
    unique_locs_list1 = list(set(locs_list1))
    for loc_number in unique_locs_list1:
        count_element = locs_list2.count(loc_number)
        score = loc_number * count_element
        scores[loc_number] = score

    sum_scores = 0
    for element in locs_list1:
        sum_scores += scores[element]
    return sum_scores


if __name__ == "__main__":
    input_lines = read_input_lines(day=1)
    
    total_p1 = part_one(input_lines)
    print(f"(Part 1) Total: {total_p1}")
    
    total_p2 = part_two(input_lines)
    print(f"(Part 2) Total: {total_p2}")



        
    

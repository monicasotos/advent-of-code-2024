# https://adventofcode.com/2024/day/1
location_file = "./inputs/day_1.txt"

with open(location_file) as f:
    content = f.readlines()

locations = [line.split() for line in content]
locs_list1 = sorted([int(loc[0]) for loc in locations])
locs_list2 = sorted([int(loc[1]) for loc in locations])


scores = {}
unique_locs_list1 = list(set(locs_list1))
for loc_number in unique_locs_list1:
    count_element = locs_list2.count(loc_number)
    score = loc_number * count_element
    scores[loc_number] = score

sum_scores = 0
for element in locs_list1:
    sum_scores += scores[element]

print(f"Sum of scores: {sum_scores}")
    

# https://adventofcode.com/2024/day/1
location_file = "./inputs/day_1_1.txt"

with open(location_file) as f:
    content = f.readlines()

locations = [line.split() for line in content]
locs_list1 = sorted([int(loc[0]) for loc in locations])
locs_list2 = sorted([int(loc[1]) for loc in locations])


distances = [abs(locs_list1[i] - locs_list2[i]) for i in range(len(locs_list1))]
sum_distances = sum(distances)

        
    

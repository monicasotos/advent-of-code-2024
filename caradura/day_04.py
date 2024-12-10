from caradura.utils import read_input_lines

def extract_grid(input_lines: list[str]) -> list[list[str]]:
    """
    Parses the input lines to extract the word search grid as a 2D list of characters.
    """
    return [list(line.strip()) for line in input_lines]

def count_xmas_occurrences(grid: list[list[str]], word: str) -> int:
    """
    Counts all occurrences of the word "XMAS" in the grid in all 8 possible directions.
    """
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    count = 0

    # Helper to check if word matches starting at (r, c) in a specific direction
    def check_direction(r, c, dr, dc):
        for i in range(word_length):
            nr, nc = r + dr * i, c + dc * i
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != word[i]:
                return 0
        return 1

    # Directions: (row_delta, col_delta)
    directions = [
        (0, 1),   # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
    ]

    # Traverse the grid
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                count += check_direction(r, c, dr, dc)

    return count



def count_xmas(grid:list[list[str]]):
    return south_east_calculator(grid)


def north_west_calculator(grid:list[list[str]]):
    count_mas = 0
    sliced_grid = grid[1: -1]
    for row_idx, row in enumerate(sliced_grid):
        for column_idx, letter in enumerate(row):
            if letter != "A":
                continue
            try:
                se_diag = grid[row_idx][column_idx - 1] + letter + grid[row_idx + 2][column_idx + 1]
            except IndexError:
                continue

            try:
                nw_diag = grid[row_idx][column_idx + 1] + letter + grid[row_idx + 2][column_idx - 1]
            except IndexError:
                continue

            if se_diag not in ["MAS", "SAM"]:
                continue
            if nw_diag not in ["MAS", "SAM"]:
                continue
            count_mas += 1

    return count_mas

def south_east_calculator(grid:list[list[str]]):
    count_mas = 0
    sliced_grid = grid[1: -1]
    for row_idx, row in enumerate(sliced_grid):
        sliced_row = row[1: -1]
        for column_idx, letter in enumerate(sliced_row):
            if letter != "A":
                continue
            try:
                se_diag = grid[row_idx][column_idx] + letter + grid[row_idx + 2][column_idx + 2]
            except IndexError:
                continue

            try:
                nw_diag = grid[row_idx][column_idx + 2] + letter + grid[row_idx + 2][column_idx]
            except IndexError:
                continue

            if se_diag not in ["MAS", "SAM"]:
                continue
            if nw_diag not in ["MAS", "SAM"]:
                continue
            count_mas += 1

    return count_mas

def find_center_list(line: list[str]) -> list[int] :
    center_list = []
    for k, v in enumerate(line):
        if v == 'A':
            center_list.append(k)

    return center_list



def find_X_masses(haystack: list[list[str]], needle: list[list[str]]):
    haystack_rows, haystack_cols = len(haystack), len(haystack[0])
    needle_rows, needle_cols = len(needle), len(needle[0])

    for i in range(haystack_rows - needle_rows + 1):
        for j in range(haystack_cols - needle_cols +1):
            continue
    return 0

###### main functions ######
def part_one(input_lines: list[str]) -> int:
    """
    Part 1: Count all occurrences of "XMAS" in the word search grid.
    """
    grid = extract_grid(input_lines)
    return count_xmas_occurrences(grid, "XMAS")

def part_two(input_lines: list[str]) -> int:
    grid = extract_grid(input_lines)
    return count_xmas(grid)


if __name__ == "__main__":
    DAY = 4
    input_lines = read_input_lines(day=4)

    total_p1 = part_one(input_lines)
    print(f"(Part 1) Total occurrences of 'XMAS': {total_p1}")

    total_p2 = part_two(input_lines)
    print(f"(Part 2) Total occurrences of 'XMAS': {total_p2}")



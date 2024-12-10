from dataclasses import dataclass
from caradura.utils import read_input_lines
from collections import namedtuple
from typing import Literal

Position = namedtuple('Position', field_names=['x', 'y'])

@dataclass
class Obstacle:
    position: Position
    num_hits: dict[Literal["x", "y"], int]# = {"x": 0, "y": 0}

def extract_grid(input_lines: list[str]) -> list[list[str]]:
    return [list(line.strip()) for line in input_lines]

def add_obstacle_to_grid(row:int, col:int, grid:list[list[str]]) -> list[list[str]]:
    new_grid = grid.copy()
    new_grid[row][col] = "#"
    return new_grid



class Cursor:
    def __init__(self, start: Position):
        self.x = start.x
        self.y = start.y
        self.step = -1
        self.direction = "y"
        self.rotationCounter = 1
        self.possible_coords:dict = {
            "x": start.x,
            "y": start.y,
        }
        self.__steps = []

    def nextPosition(self) -> Position:
        self.possible_coords[self.direction] += self.step

        return Position(self.possible_coords["x"], self.possible_coords["y"])

    def currentPosition(self):
        return Position(self.x, self.y)

    def go(self, position:Position):
        self.x = position.x
        self.y = position.y
        self.possible_coords = {
            "x": position.x,
            "y": position.y
        }

        if position not in self.__steps:
            self.__steps.append(position)

    def rotateClockWise(self):
        if self.direction == "y":
            self.direction = "x"
        else:
            self.direction = "y"

        self.rotationCounter += 1
        if self.rotationCounter % 2 == 0:
            self.step *= -1

        self.possible_coords = {
            "x": self.x,
            "y": self.y
        }

    def getSteps(self) -> list[Position]:
        return self.__steps


class Playground:
    def __init__(self, grid: list[list[str]]):
        self.grid = grid
        self.obstacles:dict[Position, Obstacle] = {}
        self.loop_found = False

    def play(self, start:Position = None) -> Cursor:
        if start is None:
            start = self.findStart()
        cursor = Cursor(start)
        x_size = len(self.grid[0])
        y_size = len(self.grid)
        directions = {
            "x": {-1: "-x", 1: "x"},
            "y": {-1: "-y", 1: "y"}
        }

        loops = 0
        maxLoops = x_size * y_size
        while True:
            if loops > maxLoops:
                break

            loops += 1

            next_pos = cursor.nextPosition()
            is_on_bounds = self.is_position_out_of_bounds(next_pos)
            if not is_on_bounds:
                break
            next_element = self.grid[next_pos.y][next_pos.x]
            if next_element == "#":
                direction = directions[cursor.direction][cursor.step]
                self.loop_found = self.register_obstacle_hit(next_pos, direction)
                if self.loop_found:
                    break
                cursor.rotateClockWise()
                continue

            cursor.go(next_pos)
        return cursor
    
    def is_position_out_of_bounds(self, position:Position):
        any_negative = any([position.x < 0, position.y < 0])
        if any_negative:
            return False
        try:
            self.grid[position.y][position.x]
        except IndexError:
            return False
        return True

    def findStart(self) -> Position:
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == '^':
                    return Position(x, y)
    
    def play_on_new_grid(self, coords_new_obstacle:Position, start:Position):
        self.grid[coords_new_obstacle.y][coords_new_obstacle.x] = "#"
        self.obstacles.clear()
        self.loop_found = False
        
        cursor = self.play(start=start)
        self.grid[coords_new_obstacle.y][coords_new_obstacle.x] = "." # put it back
        return self.loop_found
        
    
    def register_obstacle_hit(self, position:Position, direction:Literal["x", "-x", "y", "-y"]):
        """Resgisters obstacle hit. If hit twice, returns True, otherwise, False."""
        if position in self.obstacles:
            try:
                self.obstacles[position].num_hits[direction] += 1
            except Exception as e:
                raise e
            if self.obstacles[position].num_hits[direction] == 2:
                return True
        else:
            other_directions = [d for d in ["x", "-x", "y", "-y"] if d != direction]
            num_hits = dict(zip(other_directions, [0 for _ in other_directions]))
            num_hits[direction] = 1
            self.obstacles[position] = Obstacle(position=position, num_hits=num_hits)
        return False
    
    def current_obstacle_hits(self) -> list[Obstacle]:
        obstacles = list(self.obstacles.values())
        return obstacles


######## main funcitons #########

def part_one(input_lines:list[str]):
    p = Playground(extract_grid(input_lines))
    c = p.play()

    return len(c.getSteps())


def part_two(input_lines:list[str]):
    print("This takes a bit to complete. Be patient...")
    grid = extract_grid(input_lines)
    playground = Playground(grid)
    start = playground.findStart()
    initial_path:list[Position] = playground.play().getSteps()
    
    num_loops = 0
    num_elements = len(initial_path)
    j = 0
    new_start = start
    for position in initial_path:
        j += 1
        print(f"({j}/{num_elements}) Processing")
        element = grid[position.y][position.x]
        if element == "#":
            continue
                
        if playground.play_on_new_grid(position, start):
            num_loops += 1
    return num_loops


if __name__ == "__main__":
    input_lines = read_input_lines(day=6)

    total_p1 = part_one(input_lines)
    print(f"(Part 1) Total: {total_p1}")

    total_p2 = part_two(input_lines)
    print(f"(Part 2) Total: {total_p2}")
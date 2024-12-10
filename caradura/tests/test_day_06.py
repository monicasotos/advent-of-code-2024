import unittest
from caradura import day_06
from caradura.day_06 import  Position


example_grid_str = [
    "....#.....",
    "....^....#",
    "..........",
]

example_loop_grid = [
    "....#.....",
    "....^.#..#",
    "...#......",
    ".....#....",
]

example_loop_grid_2 = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#.#^.....",
    "........#.",
    "#.........",
    "......#...",
]

example_not_loop = [
    ".#..#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]

example_not_loop_2 = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#..#",
]

example_part_2 = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]

class Day6TestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_navigate_right(self):
        c = day_06.Cursor(Position(1, 1))

        self.assertEqual(Position(1, 0), c.nextPosition())

    def test_move(self):
        c = day_06.Cursor(Position(3, 3))
        p = c.nextPosition()
        c.go(p)
        c.rotateClockWise()
        p = c.nextPosition()
        c.go(p)
        p = c.nextPosition()
        c.go(p)
        p = c.nextPosition()
        c.go(p)
        c.rotateClockWise()
        p = c.nextPosition()
        c.go(p)

        self.assertEqual(Position(6, 3), c.currentPosition())

    def test_play(self):
        playground = day_06.Playground(day_06.extract_grid(example_grid_str))
        cursor = playground.play()
        self.assertEqual(5, len(cursor.getSteps()))

    def test_get_obstacle_hits(self):
        playground = day_06.Playground(day_06.extract_grid(example_grid_str))
        cursor = playground.play()
        obstacle_hits = [obs.position for obs in playground.current_obstacle_hits()]
        
        expected_obstacles = [
            Position(4, 0),
            Position(9, 1),
        ]
        self.assertEqual(expected_obstacles, obstacle_hits)
    
    def test_loop_not_found(self):
        playground = day_06.Playground(day_06.extract_grid(example_grid_str))
        cursor = playground.play()
        # for obstacle in playground.obstacles.values():
        #     print(obstacle)
        
        self.assertEqual(False, playground.loop_found)
    
    def test_loop_not_found_2(self):
        playground = day_06.Playground(day_06.extract_grid(example_not_loop))
        cursor = playground.play()
        # for obstacle in playground.obstacles.values():
        #     print(obstacle)
        
        self.assertEqual(False, playground.loop_found)
    
    
    def test_loop_found_1(self):
        playground = day_06.Playground(day_06.extract_grid(example_loop_grid))
        cursor = playground.play()
        for obstacle in playground.obstacles.values():
            print(obstacle)
        
        self.assertEqual(True, playground.loop_found)
    
    def test_loop_found_2(self):
        playground = day_06.Playground(day_06.extract_grid(example_loop_grid_2))
        cursor = playground.play()
        
        self.assertEqual(True, playground.loop_found)
    
    def test_not_loop_2(self):
        playground = day_06.Playground(day_06.extract_grid(example_not_loop_2))
        cursor = playground.play()
        
        self.assertEqual(False, playground.loop_found)
    
    def test_part_two_example(self):
        num_loops = day_06.part_two(example_part_2)
        self.assertEqual(6, num_loops)
        
        
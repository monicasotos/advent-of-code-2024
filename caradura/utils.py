import os

def read_input_lines(day:int) -> list[str]:
    if day < 10:
        day = f"0{day}"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_filename = os.path.join(script_dir, f"inputs/day_{day}.txt")
    with open(input_filename) as f:
        input_lines = f.readlines()
    return input_lines
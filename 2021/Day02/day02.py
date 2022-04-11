from typing import List, Union


def parse_input(input_file: str) -> List[List[Union[str, int]]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List of commands with their name and units.
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()
    return [[line.split()[0], int(line.split()[1])] for line in lines]


def part1(commands: List[List[Union[str, int]]]) -> int:
    """
    Solve part 1.
    @param commands: List of commands with their name and units.
    @return: The product of the final horizontal position and the final depth.
    """
    horizontal_position, depth = 0, 0
    for command in commands:
        name, units = command
        if name == 'forward':
            horizontal_position += units
        elif name == 'down':
            depth += units
        elif name == 'up':
            depth -= units
    return horizontal_position * depth


def part2(commands: List[List[Union[str, int]]]) -> int:
    """
    Solve part 2.
    @param commands: List of commands with their name and units.
    @return: The product of the final horizontal position and the final depth.
    """
    horizontal_position, depth, aim = 0, 0, 0
    for command in commands:
        name, units = command
        if name == 'forward':
            horizontal_position += units
            depth += units * aim
        elif name == 'down':
            aim += units
        elif name == 'up':
            aim -= units
    return horizontal_position * depth


def solve() -> None:
    """
    Solve the puzzle.
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

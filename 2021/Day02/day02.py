from typing import List, Union


def get_input() -> List[Union[str, int]]:
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return [[line.split()[0], int(line.split()[1])] for line in lines]


def part1(commands: List[Union[str, int]]) -> int:
    horizontal_position, depth = 0, 0
    for command in commands:
        name, units = command
        if name == "forward":
            horizontal_position += units
        elif name == "down":
            depth += units
        elif name == "up":
            depth -= units
    return horizontal_position * depth


def part2(commands: List[Union[str, int]]) -> int:
    horizontal_position, depth, aim = 0, 0, 0
    for command in commands:
        name, units = command
        if name == "forward":
            horizontal_position += units
            depth += units * aim
        elif name == "down":
            aim += units
        elif name == "up":
            aim -= units
    return horizontal_position * depth


def solve():
    puzzle_input = get_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

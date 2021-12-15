import math
from typing import List


def parse_input(input_file: str) -> List[int]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List representing the horizontal position of each crab.
    """
    with open(input_file, "r") as f:
        positions = [int(position) for position in f.readlines()[0].split(",")]
    return positions


def part1(crabs_position: List[int]) -> int:
    """
    Solve part 1.
    @param crabs_position: List representing the horizontal position of each crab.
    @return: Cheapest outcome to align all crabs.
    """
    positions = crabs_position[:]
    positions.sort()
    nb_positions = len(positions)
    half = nb_positions // 2
    median = positions[half] if nb_positions % 2 != 0 else (positions[half - 1] + positions[half]) // 2
    return sum([abs(p - median) for p in positions])


def part2(crabs_position: List[int]) -> int:
    """
    Solve part 2.
    @param crabs_position: List representing the horizontal position of each crab.
    @return: Cheapest outcome to align all crabs.
    """
    floor_mean = math.floor(sum(crabs_position) / len(crabs_position))
    floor_costs = [sum(range(abs(p - floor_mean) + 1)) for p in crabs_position]
    ceil_mean = math.ceil(sum(crabs_position) / len(crabs_position))
    ceil_costs = [sum(range(abs(p - ceil_mean) + 1)) for p in crabs_position]
    return min(sum(floor_costs), sum(ceil_costs))


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input("input.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

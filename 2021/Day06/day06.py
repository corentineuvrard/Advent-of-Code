from typing import List
from collections import Counter


def parse_input(input_file: str) -> List[int]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List representing the number of fishes for each creation timer (from 0 to 8 days).
    """
    with open(input_file, "r") as f:
        creation_timers = Counter(int(timer) for timer in f.readlines()[0].split(","))
    return [creation_timers[i] if i in creation_timers else 0 for i in range(9)]


def count_fishes(creation_timers: List[int], days: int) -> int:
    """
    Count the number of fishes for a given number of days.
    @param creation_timers: List representing the number of fishes for each creation timer (from 0 to 8 days).
    @param days:
    @return:
    """
    timers = creation_timers[:]
    for day in range(days):
        timers[0:6], timers[6], timers[7], timers[8] = timers[1:7], timers[0] + timers[7], timers[8], timers[0]
    return sum(timers)


def part1(creation_timers: List[int]) -> int:
    """
    Solve part 1.
    @param creation_timers: List representing the number of fishes for each creation timer (from 0 to 8 days).
    @return: Number of fish after 80 days.
    """
    return count_fishes(creation_timers, 80)


def part2(creation_timers: List[int]) -> int:
    """
    Solve part 2.
    @param creation_timers: List representing the number of fishes for each creation timer (from 0 to 8 days).
    @return: Number of fish after 256 days.
    """
    return count_fishes(creation_timers, 256)


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input("input.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

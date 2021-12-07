from typing import List


def get_input() -> List[int]:
    """
    Parse input.
    @return:
    """
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return [int(line) for line in lines]


def part1(nums: List[int]) -> int:
    """
    Solve part 1.
    @param nums: List of depth measurements.
    @return: Number of measurements larger than the previous measurement.
    """
    return sum(b > a for a, b in zip(nums, nums[1:]))


def part2(nums: List[int]) -> int:
    """
    Solve part 2.
    @param nums: List of depth measurements.
    @return: Number of times the sum of 3 consecutive measurements is larger than the previous sum.
    """
    return sum(b > a for a, b in zip(nums, nums[3:]))


def solve() -> None:
    """
    Solve the puzzle.
    """
    puzzle_input = get_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

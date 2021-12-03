from typing import List


def get_input() -> List[int]:
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return [int(line) for line in lines]


def part1(nums: List[int]) -> int:
    return sum(b > a for a, b in zip(nums, nums[1:]))


def part2(nums: List[int]) -> int:
    return sum(b > a for a, b in zip(nums, nums[3:]))


def solve():
    input_list = get_input()
    print(part1(input_list))
    print(part2(input_list))


solve()

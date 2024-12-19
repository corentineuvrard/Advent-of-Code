from functools import lru_cache
from typing import List, Tuple
import math


def parse_input(input_file: str) -> List[int]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List of stones represented by the number written on them.
    """
    with open(input_file, 'r') as f:
        stones = []
        for number in f.readline().split():
            stones.append(int(number))

    return stones


def split_stone(stone: int) -> Tuple[int, int]:
    """
    Split a stone into two halves based on its digits.
    @param stone: Stone to be split.
    @return: Tuple containing two integers: the left half and the right half of the digits.
    """
    nb_digits = int(math.log10(stone)) + 1

    left, right = 0, 0
    for i in reversed(range(nb_digits)):
        if i >= nb_digits // 2:
            left = left * 10 + (stone // (10 ** i)) % 10
        else:
            right = right * 10 + (stone // (10 ** i)) % 10

    return left, right


@lru_cache(maxsize=None)
def process_stone(stone: int, iteration: int) -> int:
    """
    Recursively compute the size contribution of a single stone after a given number of iterations.
    Stones are transformed as follows:
        - If `stone` is 0, it transforms into 1 in the next iteration.
        - If the number of digits in the `stone` is even, it is split into its left and right halves.
          Both parts are processed further.
        - If the number of digits is odd, the `stone` is multiplied by 2024 and processed further.
    @param stone: Value of the stone being processed.
    @param iteration: Number of remaining iterations to process the stone.
    @return: Total size contribution of the stone after processing.
    """
    if iteration == 0:
        return 1

    if stone == 0:
        return process_stone(stone=1, iteration=iteration - 1)

    nb_digits = int(math.log10(stone)) + 1
    if nb_digits % 2 == 0:
        left, right = split_stone(stone)
        return process_stone(left, iteration - 1) + process_stone(right, iteration - 1)
    else:
        return process_stone(stone * 2024, iteration - 1)


def blink(stones: List[int], iterations: int) -> int:
    """
    Compute the total number of stones after a given number of iterations.
    Applies the `process_stone` function to each stone in the tuple, aggregating their contribution
    @param stones: List of stones represented by the number written on them.
    @param iterations: Number of iterations to process the stones.
    @return: Total size contribution of all stones after the specified iterations.
    """
    return sum(process_stone(stone, iterations) for stone in stones)


def part1(stones: List[int]) -> int:
    """
    Solve part 1.
    @param stones: List of stones represented by the number written on them.
    @return: Total number of stones after blinking 25 times.
    """
    return blink(stones, iterations=25)


def part2(stones: List[int]) -> int:
    """
    Solve part 2.
    @param stones: List of stones represented by the number written on them.
    @return: Total number of stones after blinking 75 times.
    """
    return blink(stones, iterations=75)


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
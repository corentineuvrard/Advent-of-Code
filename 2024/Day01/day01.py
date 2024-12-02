from collections import defaultdict
from typing import List


def parse_input(input_file: str) -> List[List[int]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List of lists of locations IDs.
    """
    with open(input_file, 'r') as f:
        left, right = [], []
        for line in f:
            l, r = line.strip().split()
            left.append(int(l))
            right.append(int(r))

    return [left, right]


def part1(lists: List[List[int]]) -> int:
    """
    Solve part 1.
    @param lists: List of lists of location IDs.
    @return: Total distance between the two lists.
    """
    total_distance = 0
    left, right = lists

    left.sort()
    right.sort()

    for i in range(len(left)):
        total_distance += max(left[i], right[i]) - min(left[i], right[i])

    return total_distance


def part2(lists: List[List[int]]) -> int:
    """
    Solve part 2.
    @param lists: List of lists of locations IDs.
    @return: Similarity score between the two lists.
    """
    similarity_score = 0
    left, right = lists

    frequencies = defaultdict(int)
    left.sort()
    right.sort()
    i, j = 0, 0

    while i < len(left):
        if left[i] not in frequencies:
            while right[j] <= left[i]:
                if right[j] == left[i]:
                    frequencies[left[i]] += 1
                j += 1
        similarity_score += left[i] * frequencies[left[i]]
        i += 1

    return similarity_score


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
from typing import List, Tuple
import time
import numpy as np


def parse_input(input_file: str) -> List[List[int]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Two-dimensional grid of the height of each tree.
    """
    with open(input_file, 'r') as f:
        grid = [[int(c) for c in line.strip()] for line in f]

    return grid


def part1(grid: List[List[int]]) -> int:
    """
    Solve part 1.
    @param grid: Two-dimensional grid of the height of each tree.
    @return: Number of trees visible from outside the grid.
    """
    s = set()

    # Row-wise traversal
    for j in range(len(grid)):
        max_left, max_right = -1, -1
        left_done, right_done = False, False
        for i in range(len(grid[0])):
            # Check left-to-right
            if not left_done:
                if grid[j][i] > max_left:
                    s.add((i, j))
                    max_left = grid[j][i]
                if max_left == 9:
                    left_done = True
            # Check right-to-left
            if not right_done:
                if grid[j][-(i + 1)] > max_right:
                    s.add((len(grid[0]) - i - 1, j))
                    max_right = grid[j][-(i + 1)]
                if max_right == 9:
                    right_done = True

    # Column-wise traversal
    for i in range(len(grid[0])):
        max_top, max_bottom = -1, -1
        top_done, bottom_done = False, False
        for j in range(len(grid)):
            # Check top-to-bottom
            if not top_done:
                if grid[j][i] > max_top:
                    s.add((i, j))
                    max_top = grid[j][i]
                if max_top == 9:
                    top_done = True
            # Check bottom-to-top
            if not bottom_done:
                if grid[-(j + 1)][i] > max_bottom:
                    s.add((i, len(grid) - j - 1))
                    max_bottom = grid[-(j + 1)][i]
                if max_bottom == 9:
                    bottom_done = True

    return len(s)


def get_scenic_score(grid: List[List[int]], coords: Tuple[int, int]) -> int:
    """
    Get the scenic score of a given tree.
    @param grid: Two-dimensional grid of the height of each tree.
    @param coords: Coordinates of the given tree.
    @return: Scenic score of the given tree.
    """
    up, down, left, right = 0, 0, 0, 0
    row, col = coords

    for j in range(row, 0, -1):
        up += 1
        if grid[j - 1][col] >= grid[row][col]:
            break

    for j in range(row, len(grid) - 1):
        down += 1
        if grid[j + 1][col] >= grid[row][col]:
            break

    for i in range(col, 0, -1):
        left += 1
        if grid[row][i - 1] >= grid[row][col]:
            break

    for i in range(col, len(grid[0]) - 1):
        right += 1
        if grid[row][i + 1] >= grid[row][col]:
            break

    return up * down * left * right


def part2(grid: List[List[int]]) -> int:
    """
    Solve part 2.
    @param grid: Two-dimensional grid of the height of each tree.
    @return: Highest scenic score possible for any tree.
    """
    scenic_scores = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    highest_scenic_score = 0

    for j in range(len(grid)):
        for i in range(len(grid[0])):
            scenic_scores[j][i] = get_scenic_score(grid, coords=(j, i))
            if scenic_scores[j][i] > highest_scenic_score:
                highest_scenic_score = scenic_scores[j][i]

    return highest_scenic_score


def solve() -> None:
    """
    Solve the puzzle
    """
    t0 = time.perf_counter()
    puzzle_input = parse_input('input.txt')
    t1 = time.perf_counter()
    print(t1 - t0)
    print(part1(puzzle_input))
    t2 = time.perf_counter()
    print(t2 - t1)
    print(part2(puzzle_input))
    print(time.perf_counter() - t2)


solve()

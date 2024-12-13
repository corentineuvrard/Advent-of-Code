from collections import deque
import numpy as np


def parse_input(input_file: str) -> np.ndarray:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Topographic map.
    """
    with open(input_file, 'r') as f:
        topographic_map = []
        for line in f:
            topographic_map.append([int(c) for c in line.strip()])

    return np.array(topographic_map)


def part1(topographic_map: np.ndarray) -> int:
    """
    Solve part 1.
    @param topographic_map: Topographic map.
    @return: Sum of the scores of all trailheads in the topographic map.
    """
    # Retrieve trailheads coordinates
    trailheads = list(zip(*np.where(topographic_map == 0)))

    # Sum of all trailhead scores
    trailheads_score = 0

    for row, col in trailheads:
        # Summits reachable from the current trailhead
        summits = set()

        queue = deque([(row, col)])  # Queue used to perform a BFS

        # Find all the possible trailhead-summit paths using a BFS
        while queue:
            curr_row, curr_col = queue.popleft()
            curr_height = topographic_map[curr_row, curr_col]

            if curr_height == 9:
                summits.add((curr_row, curr_col))
                continue

            # Add valid neighbors to the queue
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:  # up, right, down, left
                next_row, next_col = curr_row + dr, curr_col + dc
                if 0 <= next_row < topographic_map.shape[0] and 0 <= next_col < topographic_map.shape[1]:
                    next_height = topographic_map[next_row, next_col]
                    if next_height - curr_height == 1:
                        queue.append((next_row, next_col))

        trailheads_score += len(summits)

    return trailheads_score


def part2(topographic_map: np.ndarray) -> int:
    """
    Solve part 2.
    @param topographic_map: Topographic map.
    @return: Sum of the ratings of all trailheads.
    """
    # Retrieve trailheads coordinates
    trailheads = list(zip(*np.where(topographic_map == 0)))

    # Sum of all ratings
    ratings = 0

    for row, col in trailheads:
        # Keep track of the rating of the current trailhead
        trailhead_rating = 0

        queue = deque([(row, col)])  # Queue used to perform a BFS

        # Find all the possible trailhead-summit paths using a BFS
        while queue:
            curr_row, curr_col = queue.popleft()
            curr_height = topographic_map[curr_row, curr_col]

            if curr_height == 9:
                trailhead_rating += 1
                continue

            # Add valid neighbors to the queue
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:  # up, right, down, left
                next_row, next_col = curr_row + dr, curr_col + dc
                if 0 <= next_row < topographic_map.shape[0] and 0 <= next_col < topographic_map.shape[1]:
                    next_height = topographic_map[next_row, next_col]
                    if next_height - curr_height == 1:
                        queue.append((next_row, next_col))

        ratings += trailhead_rating

    return ratings


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
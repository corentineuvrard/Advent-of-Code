from typing import List, Tuple
from collections import deque
from functools import reduce


def parse_input(input_file: str) -> List[List[int]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List of lists representing a heightmap.
    """
    with open(input_file, 'r') as f:
        content = f.read()
        lines = content.split()
    return [[int(n) for n in row] for row in lines]


def get_neighbors(heightmap: List[List[int]], row: int, col: int) -> List[Tuple[int, int]]:
    """
    Get the neighbors of the current point on the heightmap.
    @param heightmap: List of lists representing a heightmap.
    @param row: ID of the row where the current point is located.
    @param col: ID of the column where the current point is located.
    @return: List of tuples, each tuple containing the row ID and the column ID of a neighbor.
    """
    neighbors = []
    if row - 1 >= 0:
        neighbors.append((row - 1, col))
    if row + 1 < len(heightmap):
        neighbors.append((row + 1, col))
    if col - 1 >= 0:
        neighbors.append((row, col - 1))
    if col + 1 < len(heightmap[row]):
        neighbors.append((row, col + 1))
    return neighbors


def is_low_point(heightmap: List[List[int]], row: int, col: int) -> bool:
    """
    Determine if a given point is a low point by checking if its height is lower than the adjacent points.
    @param heightmap: List of lists representing a heightmap.
    @param row: ID of the row where the current point is located.
    @param col: ID of the column where the current point is located.
    @return: Return True if the current point is a local minimum, False otherwise.
    """
    current_point = heightmap[row][col]
    neighbors = get_neighbors(heightmap, row, col)
    min_point = 9
    for r, c in neighbors:
        min_point = min(min_point, heightmap[r][c])
    return current_point < min_point


def get_low_points(heightmap: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Get the low points on the given heightmap.
    @param heightmap: List of lists representing a heightmap.
    @return: List of all the low points on the heightmap.
    """
    nb_rows = len(heightmap)
    nb_cols = len(heightmap[0])
    low_points = []
    for row in range(nb_rows):
        for col in range(nb_cols):
            if is_low_point(heightmap, row, col):
                low_points.append((row, col))
    return low_points


def part1(heightmap: List[List[int]]) -> int:
    """
    Solve part 1.
    @param heightmap: List of lists representing a heightmap.
    @return: Sum of the risk levels of all low points on the heightmap.
    """
    risk_level = 0
    low_points = get_low_points(heightmap)
    for row, col in low_points:
        risk_level += heightmap[row][col] + 1
    return risk_level


def part2(heightmap: List[List[int]]) -> int:
    """
    Solve part 2.
    @param heightmap: List of lists representing a heightmap.
    @return: Product of the sizes of the three largest basins.
    """
    basins = []
    low_points = get_low_points(heightmap)
    for row, col in low_points:
        basin = set()
        queue = deque([(row, col)])
        while queue:
            c_row, c_col = queue.popleft()
            basin.add((c_row, c_col))
            current_value = heightmap[row][col]
            neighbors = get_neighbors(heightmap, c_row, c_col)
            for n_row, n_col in neighbors:
                neighbor_value = heightmap[n_row][n_col]
                if current_value < neighbor_value < 9 and (n_row, n_col) not in basin:
                    queue.append((n_row, n_col))
        basins.append(len(basin))
    basins.sort(reverse=True)
    return reduce((lambda x, y: x * y), basins[:3])


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

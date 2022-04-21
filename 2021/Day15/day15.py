from typing import List, Tuple
from queue import PriorityQueue


def get_neighbors(point: Tuple[int, int], dimensions: Tuple[int, int], visited: set) -> List[Tuple[int, int]]:
    """
    Get the non visited neighbors of the given point.
    @param point: Coordinates of the given point.
    @param dimensions: Dimensions of the matrix.
    @param visited: Points visited in the Dijkstra algorithm.
    @return: List of coordinates of the non visited neighbors of the given point.
    """
    neighbors = []
    width, height = dimensions
    x, y = point
    if y > 0 and (x, y - 1) not in visited:
        neighbors.append((x, y - 1))
    if x < width - 1 and (x + 1, y) not in visited:
        neighbors.append((x + 1, y))
    if y < height - 1 and (x, y + 1) not in visited:
        neighbors.append((x, y + 1))
    if x > 0 and (x - 1, y) not in visited:
        neighbors.append((x - 1, y))
    return neighbors


def parse_input(input_file: str) -> List[List[int]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Matrix of integers representing the risk level throughout the cave.
    """
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
    return [[int(n) for n in line] for line in lines]


def part1(matrix: List[List[int]]) -> int:
    """
    Solve part 1.
    @param matrix: Matrix of integers representing the risk level throughout the cave.
    @return: Lowest total risk of any path from the top left to the bottom right of the matrix.
    """
    width, height = len(matrix[0]), len(matrix)
    visited = set()
    costs = {(0, 0): 0}
    queue = PriorityQueue()

    queue.put((0, (0, 0)))
    while queue:
        _, current = queue.get()
        visited.add(current)
        if current[0] == width - 1 and current[1] == height - 1:
            break
        neighbors = get_neighbors(current, (width, height), visited)
        for neighbor in neighbors:
            old_cost = costs.get(neighbor, float('inf'))
            new_cost = costs[current] + matrix[neighbor[1]][neighbor[0]]
            if new_cost < old_cost:
                queue.put((new_cost, neighbor))
                costs[neighbor] = new_cost

    return costs[(width - 1, height - 1)]


def part2(matrix: List[List[int]]) -> int:
    """
    Solve part 2.
    @param matrix: Matrix of integers representing the risk level throughout the cave.
    @return: Lowest total risk of any path from the top left to the bottom right of the matrix five times larger in both
    dimensions.
    """
    width, height = len(matrix[0]), len(matrix)
    visited = set()
    costs = {(0, 0): 0}
    queue = PriorityQueue()

    queue.put((0, (0, 0)))
    while queue:
        _, current = queue.get()
        visited.add(current)
        if current[0] == 5 * width - 1 and current[1] == 5 * height - 1:
            break
        neighbors = get_neighbors(current, (5 * width, 5 * height), visited)
        for neighbor in neighbors:
            old_cost = costs.get(neighbor, float('inf'))
            x = neighbor[0] % width
            y = neighbor[1] % height
            factor = neighbor[0] // width + neighbor[1] // height
            value = factor + matrix[y][x]
            if value > 9:
                value = value % 10 + 1
            new_cost = costs[current] + value
            if new_cost < old_cost:
                queue.put((new_cost, neighbor))
                costs[neighbor] = new_cost

    return costs[(5 * width - 1, 5 * height - 1)]


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

from typing import List
import numpy as np


def get_neighbors(energy_levels: np.ndarray, point: List[int]) -> List[List[int]]:
    """
    Get the neighbors of a given point.
    @param energy_levels: Grid representing the energy level of octopuses.
    @param point: Coordinates x and y of the current point.
    @return: List of coordinates of each neighbor of the current point.
    """
    neighbors = []
    height, width = energy_levels.shape
    if point[0] - 1 >= 0:
        neighbors.append([point[0] - 1, point[1]])
    if point[0] - 1 >= 0 and point[1] + 1 < width:
        neighbors.append([point[0] - 1, point[1] + 1])
    if point[1] + 1 < width:
        neighbors.append([point[0], point[1] + 1])
    if point[0] + 1 < height and point[1] + 1 < width:
        neighbors.append([point[0] + 1, point[1] + 1])
    if point[0] + 1 < height:
        neighbors.append([point[0] + 1, point[1]])
    if point[0] + 1 < height and point[1] - 1 >= 0:
        neighbors.append([point[0] + 1, point[1] - 1])
    if point[1] - 1 >= 0:
        neighbors.append([point[0], point[1] - 1])
    if point[0] - 1 >= 0 and point[1] - 1 >= 0:
        neighbors.append([point[0] - 1, point[1] - 1])
    return neighbors


def parse_input(input_file: str) -> np.ndarray:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Grid representing the energy level of octopuses.
    """
    with open(input_file, "r") as f:
        content = f.read()
        lines = content.split()
    return np.array([[int(n) for n in row] for row in lines])


def part1(energy_levels: np.ndarray) -> int:
    """
    Solve part 1.
    @param energy_levels: Grid representing the energy level of octopuses.
    @return: Number of flashes after 100 steps.
    """
    nb_flashes = 0
    for _ in range(100):
        energy_levels = energy_levels.__add__(1)
        flashes_queue = list(np.transpose(np.nonzero(energy_levels > 9)))
        flashes = set([tuple(f) for f in flashes_queue])
        while len(flashes_queue) > 0:
            current = flashes_queue.pop()
            neighbors = get_neighbors(energy_levels, current)
            for n in neighbors:
                if tuple(n) not in flashes:
                    energy_levels[n[0], n[1]] += 1
                    if energy_levels[n[0], n[1]] > 9:
                        flashes_queue.append(n)
                        flashes.add(tuple(n))
        for f in flashes:
            energy_levels[f[0], f[1]] = 0
        nb_flashes += len(flashes)
    return nb_flashes


def part2(energy_levels: np.ndarray) -> int:
    """
    Solve part 2.
    @param energy_levels: Grid representing the energy level of octopuses.
    @return: Step during which all octopuses flash.
    """
    step = 0
    while len(np.transpose(np.nonzero(energy_levels))) != 0:
        energy_levels = energy_levels.__add__(1)
        flashes_queue = list(np.transpose(np.nonzero(energy_levels > 9)))
        flashes = set([tuple(f) for f in flashes_queue])
        while len(flashes_queue) > 0:
            current = flashes_queue.pop()
            neighbors = get_neighbors(energy_levels, current)
            for n in neighbors:
                if tuple(n) not in flashes:
                    energy_levels[n[0], n[1]] += 1
                    if energy_levels[n[0], n[1]] > 9:
                        flashes_queue.append(n)
                        flashes.add(tuple(n))
        for f in flashes:
            energy_levels[f[0], f[1]] = 0
        step += 1
    return step


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input("input.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

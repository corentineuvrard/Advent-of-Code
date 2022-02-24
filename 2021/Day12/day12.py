import timeit
from typing import DefaultDict, List
from collections import defaultdict


def parse_input(input_file: str) -> DefaultDict[str, List[str]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Dictionary representing the connections between caves.
    """
    connections = defaultdict(list)
    with open(input_file, "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            caves = line.split("-")
            if caves[0] != "start" and caves[0] != "end" and caves[1] != "start" and caves[1] != "end":
                connections[caves[0]].append(caves[1])
                connections[caves[1]].append(caves[0])
            elif caves[0] == "start" or caves[1] == "end":
                connections[caves[0]].append(caves[1])
            elif caves[0] == "end" or caves[1] == "start":
                connections[caves[1]].append(caves[0])
    return connections


def part1(connections: DefaultDict[str, List[str]]) -> int:
    """
    Solve part 1.
    @param connections: Dictionary representing the connections between caves.
    @return: Number of paths through the cave system that visit small caves at most once.
    """
    nb_paths = 0
    stack = [("start", set())]
    while stack:
        current, visited = stack.pop()
        if current == "end":
            nb_paths += 1
        else:
            if "a" < current[0] < "z":
                visited = visited.copy()
                visited.add(current)
            for cave in connections[current]:
                if cave not in visited:
                    stack.append((cave, visited))
    return nb_paths


def part2(connections: DefaultDict[str, List[str]]) -> int:
    """
    Solve part 2.
    @param connections: Dictionary representing the connections between caves.
    @return: Number of paths through the cave system that visit small caves at most twice.
    """
    nb_paths = 0
    stack = [("start", set(), False)]
    while stack:
        current, visited, double_visit = stack.pop()
        if current == "end":
            nb_paths += 1
        else:
            if "a" < current[0] < "z":
                visited = visited.copy()
                visited.add(current)
            for cave in connections[current]:
                if cave not in visited:
                    stack.append((cave, visited, double_visit))
                elif not double_visit:
                    stack.append((cave, visited, True))
    return nb_paths


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input("input.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

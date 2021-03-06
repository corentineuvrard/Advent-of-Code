from typing import Tuple, Dict
from collections import Counter


def parse_input(input_file: str) -> Tuple[str, Dict[str, str]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: A polymer template and a list of pair insertion rules.
    """
    polymer_template = None
    pair_insertion = dict()
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            line = line.split()
            if len(line) == 1:
                polymer_template = line[0]
            elif len(line) == 3:
                pair_insertion[line[0]] = line[2]
    return polymer_template, pair_insertion


def polymerize(manual: Tuple[str, Dict[str, str]], steps: int) -> int:
    """
    Apply a number of steps of pair insertion to the polymer template contained in the manual.
    @param manual: Manual containing a polymer template and a list of pair insertion rules.
    @param steps: Number of pair insertion to apply to the polymer template.
    @return: Subtraction of the quantity of the most common element and the quantity of the least common element in the
    final polymer.
    """
    polymer, pairs = manual
    pairs_counter = Counter([polymer[i:i + 2] for i in range(len(polymer) - 1)])
    for _ in range(steps):
        temp_counter = pairs_counter.copy()
        for pair in [key for key in pairs_counter.keys() if pairs_counter[key] > 0]:
            pairs_counter[pair] -= temp_counter[pair]
            pairs_counter[pair[0] + pairs[pair]] += temp_counter[pair]
            pairs_counter[pairs[pair] + pair[1]] += temp_counter[pair]
    elements = Counter(polymer[0])
    for pair in pairs_counter.keys():
        elements[pair[1]] += pairs_counter[pair]
    return max(elements.values()) - min(elements.values())


def part1(manual: Tuple[str, Dict[str, str]]) -> int:
    """
    Solve part 1.
    @param manual: Manual containing a polymer template and a list of pair insertion rules.
    @return: Result of the polymerization after applying 10 steps of pair insertion.
    """
    return polymerize(manual, 10)


def part2(manual: Tuple[str, Dict[str, str]]) -> int:
    """
    Solve part 2.
    @param manual: Manual containing a polymer template and a list of pair insertion rules.
    @return: Result of the polymerization after applying 40 steps of pair insertion.
    """
    return polymerize(manual, 40)


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

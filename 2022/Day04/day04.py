from typing import List, Tuple


def parse_input(input_file: str) -> List[List[Tuple[int, int]]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List representing the section assignments for each pair of Elves.
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()
        assignments = []
        for line in lines:
            pair = line[:-1].split(',')
            assignment = []
            for sections_range in pair:
                sections = sections_range.split('-')
                assignment.append((int(sections[0]), int(sections[1]),))
            assignments.append(assignment)
    return assignments


def part1(assignments: List[List[Tuple[int, int]]]) -> int:
    """
    Solve part 1.
    @param assignments: List representing the section assignments for each pair of Elves.
    @return: The number of assignment pairs where one range of section IDs contains the other.
    """
    nb_inclusions = 0
    for assignment in assignments:
        if (assignment[0][0] <= assignment[1][0] and assignment[0][1] >= assignment[1][1]
                or assignment[0][0] >= assignment[1][0] and assignment[0][1] <= assignment[1][1]):
            nb_inclusions += 1
    return nb_inclusions


def part2(assignments: List[List[Tuple[int, int]]]) -> int:
    """
    Solve part 2.
    @param assignments: List representing the section assignments for each pair of Elves.
    @return: The number of assignments pairs where ranges overlap.
    """
    nb_inclusions = 0
    for assignment in assignments:
        if (assignment[1][0] <= assignment[0][0] <= assignment[1][1]
                or assignment[1][0] <= assignment[0][1] <= assignment[1][1]
                or assignment[0][0] <= assignment[1][0] <= assignment[0][1]
                or assignment[0][0] <= assignment[1][1] <= assignment[0][1]):
            nb_inclusions += 1
    return nb_inclusions


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

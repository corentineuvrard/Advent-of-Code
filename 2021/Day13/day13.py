import numpy as np
from typing import Tuple, List


ALPHABET = {
    '###.#..####.#..##..####.': 'B',
    '.##.#..##...#...#..#.##.': 'C',
    '#####...###.#...#...####': 'E',
    '#####...###.#...#...#...': 'F',
    '.##.#..##...#.###..#.###': 'G',
    '#..##..######..##..##..#': 'H',
    '..##...#...#...##..#.##.': 'J',
    '#...#...#...#...#...####': 'L',
    '###.#..##..####.#...#...': 'P',
    '###.#..##..####.#.#.#..#': 'R',
    '#..##..##..##..##..#.##.': 'U',
    '####...#..#..#..#...####': 'Z'
}


def read_code(code: np.ndarray) -> str:
    """
    Read a code.
    @param code: Array representation of the code.
    @return: String representation of the code.
    """
    code_string = ''
    # There are 8 letters in a code
    for i in range(8):
        # Each letter is 4 characters large and letters are separated with a single character, hence a step of 5
        letter = code[:, (i * 5):(i * 5 + 4)]
        code_string += ALPHABET[''.join(letter.flatten())]
    return code_string


def parse_input(input_file: str) -> Tuple[np.ndarray, List[List[str]]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: The transparent paper marked with random dots and including instructions on how to fold it up.
    """
    instructions = []
    coordinates = []
    with open(input_file, "r") as f:
        lines = f.read().splitlines()
        width, height = 0, 0
        for line in lines:
            # Read the dots' coordinates
            if len(line.split()) == 1:
                coord = line.split(',')
                coordinates.append(coord)
            # Read the fold instructions
            elif len(line.split()) == 3:
                instruction = line.split()[2].split('=')
                instructions.append(instruction)
                # Deduce the width from the first fold along the x-axis
                if width == 0 and instruction[0] == 'x':
                    width = int(instruction[1]) * 2 + 1
                # Deduce the height from the first fold along the y-axis
                if height == 0 and instruction[0] == 'y':
                    height = int(instruction[1]) * 2 + 1
        dots = np.array([['.' for _ in range(width + 1)] for _ in range(height + 1)])
        for coord in coordinates:
            dots[int(coord[1])][int(coord[0])] = '#'
    return dots, instructions


def part1(transparent_paper: Tuple[np.ndarray, List[List[str]]]) -> int:
    """
    Solve part 1.
    @param transparent_paper: Paper marked with dots and including fold instructions.
    @return: Number of visible dots on the transparent paper after completing the first fold instruction.
    """
    dots, instructions = transparent_paper
    index = int(instructions[0][1])
    nb_dots = 0
    if instructions[0][0] == 'x':
        for i in range(1, index + 1):
            nb_dots += [dots[j, index - i] == '#' or dots[j, index + i] == '#' for j in range(len(dots))].count(True)
    else:
        for j in range(1, index + 1):
            nb_dots += [dots[index - j, i] == '#' or dots[index + j, i] == '#' for i in range(len(dots[j]))].count(True)
    return nb_dots


def part2(transparent_paper: Tuple[np.ndarray, List[List[str]]]) -> str:
    """
    Solve part 2.
    @param transparent_paper: Paper marked with dots and including fold instructions.
    @return: The code to activate the infrared thermal imaging camera system.
    """
    dots, instructions = transparent_paper
    for axis, index in instructions:
        index = int(index)
        if axis == 'x':
            for i in range(1, index + 1):
                for j in range(len(dots)):
                    dots[j, index - i] = dots[j, index + i] if dots[j, index + i] == '#' else dots[j, index - i]
            dots = dots[:, 0:index]
        else:
            for j in range(1, index + 1):
                for i in range(len(dots[0])):
                    dots[index - j, i] = dots[index + j, i] if dots[index + j, i] == '#' else dots[index - j, i]
            dots = dots[0:index, :]
    return read_code(dots)


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input("input.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

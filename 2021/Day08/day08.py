import timeit
from typing import List, Tuple


def pick(signal_patterns: List[str], size: int, sub_pattern: str = None, container: str = None) -> str:
    """
    Pick a signal pattern according to different parameters.
    @param signal_patterns: List of signal patterns.
    @param size: Size of the signal pattern to pick.
    @param sub_pattern: Signal pattern which is contained in the signal pattern to pick.
    @param container: Signal pattern which contains the signal pattern to pick.
    @return: Signal pattern matching the given parameters.
    """
    if sub_pattern:
        value = [sp for sp in signal_patterns if len(sp) == size
                 and all(list(map(lambda x: x in sp, sub_pattern)))][0]
    elif container:
        value = [sp for sp in signal_patterns if len(sp) == size
                 and all(list(map(lambda x: x in container, sp)))][0]
    else:
        value = [sp for sp in signal_patterns if len(sp) == size][0]
    signal_patterns.remove(value)
    return value


def parse_input(input_file: str) -> List[Tuple[List[str], List[str]]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List of notes with the signal patterns and the output values for each note.
    """
    with open(input_file, "r") as f:
        lines = f.readlines()
    return [(line.split("|")[0].split(), line.split("|")[1].split()) for line in lines]


def part1(notes: List[Tuple[List[str], List[str]]]) -> int:
    """
    Solve part 1.
    @param notes: List of notes with the signal patterns and the output values for each note.
    @return: Number of times the digits 1, 4, 7 and 8 appear in the output values.
    """
    nb_digits_of_interest = 0  # Digits of interest are digits that use a unique number of segments (1, 4, 7, 8).
    for note in notes:
        _, output_values = note
        for value in output_values:
            length = len(value)
            if length == 2 or length == 4 or length == 3 or length == 7:
                nb_digits_of_interest += 1
    return nb_digits_of_interest


def part2(notes: List[Tuple[List[str], List[str]]]) -> int:
    """
    Solve part 2.
    @param notes: List of notes with the signal patterns and the output values for each note.
    @return: Sum of all the output values after being decoded.
    """
    codes = []
    for note in notes:

        # Analyse the segments to determine for each digit which segments it uses.
        digits = [''] * 10
        digits[1] = pick(note[0], 2)
        digits[4] = pick(note[0], 4)
        digits[7] = pick(note[0], 3)
        digits[8] = pick(note[0], 7)
        digits[3] = pick(note[0], 5, digits[7])
        digits[9] = pick(note[0], 6, digits[4])
        digits[0] = pick(note[0], 6, digits[7])
        digits[6] = pick(note[0], 6)
        digits[5] = pick(note[0], 5, None, digits[6])
        digits[2] = pick(note[0], 5)

        # Analyse the output values to determine the code
        code = ''
        for i in range(4):
            code += [str(digit) for digit, sp in enumerate(digits) if len(sp) == len(note[1][i])
                     and all(list(map(lambda x: x in note[1][i], sp)))][0]
        codes.append(int(code))

    return sum(codes)


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input("input.txt")

    start1 = timeit.default_timer()

    print(part1(puzzle_input))

    start2 = timeit.default_timer()
    print(start2 - start1)

    print(part2(puzzle_input))

    end = timeit.default_timer()
    print(end - start2)


solve()

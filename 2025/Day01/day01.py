def parse_input(input_file: str) -> list[tuple[str, int]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Sequence of rotations.
    """
    with open(input_file, 'r') as f:
        rotations = []
        for line in f:
            rotations.append((line[0], int(line[1:])))
        return rotations


def part1(rotations: list[tuple[str, int]]) -> int:
    """
    Solve part 1.
    @param rotations: Sequence of rotations.
    @return: Number of times the dial is left pointing at 0 after any
        rotation in the sequence.
    """
    dial = 50
    nb_zeros = 0

    for rotation in rotations:
        if rotation[0] == 'L':
            dial = (dial - rotation[1]) % 100
        else:
            dial = (dial + rotation[1]) % 100
        if dial == 0:
            nb_zeros += 1

    return nb_zeros


def part2(rotations: list[tuple[str, int]]) -> int:
    """
    Solve part 2.
    @param rotations: Sequence of rotations.
    @return: Number of times any click causes the dial to point 0.
    """
    dial = 50
    nb_clicks = 0

    for rotation in rotations:
        nb_clicks += rotation[1] // 100
        remainder = rotation[1] % 100
        if rotation[0] == 'L':
            if dial <= remainder and dial != 0:
                nb_clicks += 1
            dial = (dial - remainder) % 100
        else:
            if dial + remainder >= 100 and dial != 0:
                nb_clicks += 1
            dial = (dial + remainder) % 100

    return nb_clicks


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
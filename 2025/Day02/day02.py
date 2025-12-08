def parse_input(input_file: str) -> list[tuple[int, int]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List of product ID ranges.
    """
    with open(input_file, 'r') as f:
        ranges = f.read().split(',')
        return [
            (int(start), int(end))
            for start, end in (id_range.split('-')
            for id_range in ranges)
        ]


def part1(ranges: list[tuple[int, int]]) -> int:
    """
    Solve part 1.
    @param ranges: List of product ID ranges.
    @return: Sum of all invalid IDs.
    """
    nb_invalid_ids = 0

    for start, end in ranges:
        for i in range(start, end + 1):
            num_str = str(i)
            if len(num_str) % 2 == 0:
                half = len(num_str) // 2
                if num_str[:half] == num_str[half:]:
                    nb_invalid_ids += i

    return nb_invalid_ids


def part2(ranges: list[tuple[int, int]]) -> int:
    """
    Solve part 2.
    @param ranges: List of product ID ranges.
    @return: Sum of all invalid IDs.
    """
    nb_invalid_ids = 0

    for start, end in ranges:
        for i in range(start, end + 1):
            num_str = str(i)
            for j in range(1, (len(num_str) // 2) + 1):
                factor = len(num_str) // j
                if j * factor != len(num_str):
                    continue
                if num_str[:j] * factor == num_str:
                    nb_invalid_ids += i
                    break

    return nb_invalid_ids


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
def parse_input(input_file: str) -> str:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: String representing the datastream buffer sent.
    """
    with open(input_file, 'r') as f:
        line = f.readline()
    return line


def part1(datastream_buffer: str) -> int:
    """
    Solve part 1.
    @param datastream_buffer: String representing the datastream buffer sent.
    @return: The number of characters that have to be read before the first start-of-packet marker is detected.
    """
    first_sop_marker = 0
    for i in range(len(datastream_buffer) - 4):
        if len(set(datastream_buffer[i:i + 4])) == 4:
            first_sop_marker = i + 4
            break
    return first_sop_marker


def part2(datastream_buffer: str) -> int:
    """
    Solve part 2.
    @param datastream_buffer: String representing the datastream buffer sent.
    @return: The number of characters that have to be read before the first start-of-message marker is detected.
    """
    first_som_marker = 0
    for i in range(len(datastream_buffer) - 14):
        if len(set(datastream_buffer[i:i + 14])) == 14:
            first_som_marker = i + 14
            break
    return first_som_marker


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

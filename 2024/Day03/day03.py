import re


def parse_input(input_file: str) -> str:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Memory of the computer.
    """
    with open(input_file, 'r') as f:
        memory = f.read()
    return memory


def part1(memory: str) -> int:
    """
    Solve part 1.
    @param memory: Memory of the computer.
    @return: Sum of all valid multiplications found in the memory.
    """
    total_sum = 0
    pattern = 'mul\((\d{1,3}),(\d{1,3})\)'
    multiplications = re.findall(pattern=pattern, string=memory)

    for n1, n2 in multiplications:
        total_sum += int(n1) * int(n2)

    return total_sum


def part2(memory: str) -> int:
    """
    Solve part 2.
    @param memory: Memory of the computer.
    @return: Sum of all valid multiplications found in the memory, handling special instructions.
    """
    total_sum = 0
    pattern = "mul\((\d{1,3}),(\d{1,3})\)|(do\(\)|don't\(\))"
    matches = re.findall(pattern=pattern, string=memory)
    process_flag = True

    for match in matches:
        if match[0] and match[1] and process_flag:
            total_sum += int(match[0]) * int(match[1])
        elif match[2]:
            process_flag = match[2] == 'do()'

    return total_sum


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
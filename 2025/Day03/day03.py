def parse_input(input_file: str) -> list[str]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Banks of batteries.
    """
    with open(input_file, 'r') as f:
        return [line.strip() for line in f]


def part1(banks: list[str]) -> int:
    """
    Solve part 1.
    @param banks: Banks of batteries.
    @return: Total output joltage.
    """
    joltage = 0

    for bank in banks:
        max1_id = bank.index(max(bank[:-1]))
        max2_id = bank.index(max(bank[max1_id + 1:]))
        bank_max = int(f"{bank[max1_id]}{bank[max2_id]}")
        joltage += int(bank_max)

    return joltage


def part2(banks: list[str]) -> int:
    """
    Solve part 2.
    @param banks: Banks of batteries.
    @return: Total output joltage.
    """
    joltage = 0

    for bank in banks:
        bank_max_indices = []
        bank_size = len(bank)
        for i in range(11, -1, -1):  # 12 digits in each bank's joltage
            right = bank_size - i
            if not bank_max_indices:
                max_index = bank.index(max(bank[:right]))
                bank_max_indices.append(max_index)
            else:
                left = bank_max_indices[-1] + 1
                max_index = (
                    left + bank[left:].index(
                        max(bank[bank_max_indices[-1] + 1:right])
                    )
                )
                bank_max_indices.append(max_index)

        bank_max = ''
        for bank_max_index in bank_max_indices:
            bank_max += bank[bank_max_index]
        bank_max = int(bank_max)
        joltage += bank_max

    return joltage


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
from math import prod


def parse_input(input_file: str) -> list[str]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Math worksheet of the youngest cephalopod. 
    """
    with open(input_file, 'r') as f:
        return [line.strip('\n') for line in f]


def part1(worksheet: list[str]) -> int:
    """
    Solve part 1.
    @param worksheet: Math worksheet of the youngest cephalopod.
    @return: Grand total found by adding together all of the answers to
        the individual problems.
    """
    worksheet = [line.split() for line in worksheet]

    rows, cols = len(worksheet), len(worksheet[0])
    grand_total = 0

    for c in range(cols):
        operator = worksheet[-1][c]
        numbers = [int(worksheet[r][c]) for r in range(rows - 1)]
        grand_total += calculate(numbers, operator)

    return grand_total


def part2(worksheet: list[str]) -> int:
    """
    Solve part 2.
    @param worksheet: Math worksheet of the youngest cephalopod.
    @return: Grand total found by adding together all of the answers to
        the individual problems.
    """
    worksheet = [list(line) for line in worksheet]

    rows, cols = len(worksheet), len(worksheet[0])
    grand_total = 0
    
    operator = '+'
    numbers = []

    for c in range(cols):
        col = [worksheet[r][c] for r in range(rows)]
        first_part = col[:-1]
        last_part = col[-1]
        
        if last_part != ' ':
            operator = last_part
            
        if any(character != ' ' for character in first_part):
            numbers.append(int(''.join(first_part)))
        else:
            grand_total += calculate(numbers, operator)
            numbers = []

    return grand_total + calculate(numbers, operator)


def calculate(numbers: list[int], operator: str) -> int:
    """
    Calculate the sum or the product of all numbers based on the given
    operator.
    :param numbers: List of numbers of a specific problem.
    :param operator: Operator used for the calculation ('+' or '*').
    :return: Result of the calculation of the given problem.
    """
    if operator == '+':
        return sum(numbers)
    return prod(numbers)


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
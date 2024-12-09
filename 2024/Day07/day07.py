from typing import List, Tuple


def parse_input(input_file: str) -> List[Tuple[int, List[int]]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List of tuples with test values and number lists representing calibration equations.
    """
    with open(input_file, 'r') as f:
        equations = []
        for line in f:
            split_line = line.split(': ')
            test_value = int(split_line[0])
            numbers = list(map(int, split_line[1].split()))
            equations.append((test_value, numbers))

    return equations


def is_valid(test_value: int, numbers: List[int], current_value: int = 0, allow_concatenate: bool = False) -> bool:
    """
    Check if any equation using numbers would be correct with the operators add, multiply, and optionally concatenate.
    @param test_value: Value to reach with all the numbers.
    @param numbers: Numbers to use to reach the test value.
    @param current_value: Current value to which numbers are added or multiplied.
    @param allow_concatenate: If True, allow concatenation of numbers.
    @return: Boolean indicating whether a valid equation can be formed.
    """
    if not numbers:
        return current_value == test_value

    # Prune recursion when the current_value exceeds the test_value,
    # assuming that all numbers are strictly positive (in the range [1, +inf])
    if current_value > test_value:
        return False

    # Recursive case
    next_number = numbers[0]
    remaining_numbers = numbers[1:]

    if allow_concatenate:
        # Concatenation logic (shifting the digits)
        concatenated_value = current_value * (10 ** len(str(next_number))) + next_number
        return (is_valid(test_value, remaining_numbers, current_value + next_number, allow_concatenate) or
                is_valid(test_value, remaining_numbers, current_value * next_number, allow_concatenate) or
                is_valid(test_value, remaining_numbers, concatenated_value, allow_concatenate))
    else:
        # Only add and multiply
        return (is_valid(test_value, remaining_numbers, current_value + next_number, allow_concatenate) or
                is_valid(test_value, remaining_numbers, current_value * next_number, allow_concatenate))


def part1(equations: List[Tuple[int, List[int]]]) -> int:
    """
    Solve part 1.
    @param equations: List of tuples with test values and number lists representing calibration equations.
    @return: Total calibration result which is the sum of the test values of the valid equations.
    """
    total_calibration = 0

    for test_value, numbers in equations:
        if is_valid(test_value, numbers, allow_concatenate=False):
            total_calibration += test_value

    return total_calibration


def part2(equations: List[Tuple[int, List[int]]]) -> int:
    """
    Solve part 2.
    @param equations: List of tuples with test values and number lists representing calibration equations.
    @return: Total calibration result which is the sum of the test values of the valid equations.
    """
    total_calibration = 0

    for test_value, numbers in equations:
        if is_valid(test_value, numbers, allow_concatenate=True):
            total_calibration += test_value

    return total_calibration


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
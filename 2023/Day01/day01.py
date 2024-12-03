import re
from typing import List


def parse_input(input_file: str) -> List[str]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List of calibration values.
    """
    with open(input_file, 'r') as f:
        calibration_document = [line for line in f]

    return calibration_document


def part1(calibration_document: List[str]) -> int:
    """
    Solve part 1.
    @param calibration_document: List of calibration values.
    @return: Sum of all calibration values.
    """
    sum_calibration_values = 0

    for line in calibration_document:
        digits = re.findall(pattern='\d', string=line)
        if digits:
            calibration_value = int(digits[0] + digits[-1])
            sum_calibration_values += calibration_value

    return sum_calibration_values


def part2(calibration_document: List[str]) -> int:
    """
    Solve part 2.
    @param calibration_document: List of calibration values.
    @return: Sum of all calibration values.
    """
    sum_calibration_values = 0

    digit_words = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }


    for line in calibration_document:

        # Search for the first digit
        first_digit = None
        for i in range(len(line)):
            if first_digit:
                break
            if line[i].isdigit():
                first_digit = line[i]
                break
            # Search for a digit word
            for j in range(3, 6):
                if line[i:i + j] in digit_words:
                    first_digit = digit_words[line[i:i + j]]
                    break

        # Search for the last digit
        last_digit = None
        for i in range(len(line) - 1, -1, -1):
            if last_digit:
                break
            if line[i].isdigit():
                last_digit = line[i]
                break
            # Search for a digit word
            for j in range(3, 6):
                if line[i - j + 1:i + 1] in digit_words:
                    last_digit = digit_words[line[i - j + 1:i + 1]]
                    break

        calibration_value = int(first_digit + last_digit)
        sum_calibration_values += calibration_value

    return sum_calibration_values


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
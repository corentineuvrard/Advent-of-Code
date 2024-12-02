from typing import List


def parse_input(input_file: str) -> List[List[int]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List of reports.
    """
    with open(input_file, 'r') as f:
        reports = []
        for line in f:
            reports.append([int(e) for e in line.split()])

    return reports


def is_safe(report: List[int]) -> bool:
    """
    Check if a report is safe.
    @param report: List of levels.
    @return: True if the report is safe. False, otherwise.
    """
    increasing_flag = None

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if increasing_flag is None:
            increasing_flag = diff > 0
        if increasing_flag:
            if diff < 1 or 3 < diff:
                return False
        else:
            if diff < -3 or -1 < diff:
                return False

    return True


def part1(reports: List[List[int]]) -> int:
    """
    Solve part 1.
    @param reports: List of reports.
    @return: Number of safe reports.
    """
    nb_safe_reports = len(reports)

    for report in reports:
        if not is_safe(report):
            nb_safe_reports -= 1

    return nb_safe_reports


def part2(reports: List[List[int]]) -> int:
    """
    Solve part 2.
    @param reports: List of reports
    @return: Number of safe reports.
    """
    unsafe_reports = []
    nb_tolerated_reports = 0

    for report in reports:
        if not is_safe(report):
            unsafe_reports.append(report)

    for report in unsafe_reports:
        for i in range(len(report)):
            if is_safe(report[:i] + report[i + 1:]):
                nb_tolerated_reports += 1
                break

    nb_safe_reports = len(reports) - len(unsafe_reports) + nb_tolerated_reports

    return nb_safe_reports


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
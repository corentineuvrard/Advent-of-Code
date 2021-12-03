from typing import List


def get_input() -> List[str]:
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return lines


def part1(diagnostic_report: List[str]) -> int:
    dr_columns = list(zip(*diagnostic_report))
    gamma_rate = ""
    epsilon_rate = ""
    for element in dr_columns:
        if element.count("0") > element.count("1"):
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    return gamma_rate * epsilon_rate


def part2(diagnostic_report: List[str]) -> int:
    def get_rating(element: str) -> int:
        dr_columns = list(zip(*diagnostic_report))
        indices = set(range(len(dr_columns[0])))
        index = 0
        if element == "oxygen_generator":
            bits = ["1", "0"]
        else:
            bits = ["0", "1"]
        while len(indices) > 1:
            remaining_numbers = [dr_columns[index][i] for i in indices]
            if remaining_numbers.count("0") > remaining_numbers.count("1"):
                non_matching_indices = set([i for i, e in enumerate(dr_columns[index]) if e == bits[0]])
            else:
                non_matching_indices = set([i for i, e in enumerate(dr_columns[index]) if e == bits[1]])
            indices -= non_matching_indices
            index += 1
        return int(diagnostic_report[indices.pop()], 2)
    return get_rating("oxygen_generator") * get_rating("co2_scrubber")


def solve():
    puzzle_input = get_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

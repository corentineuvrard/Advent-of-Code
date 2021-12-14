from typing import List


def parse_input(input_file: str) -> List[int]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List of endpoints representing vent segments.
    """
    with open(input_file, "r") as f:
        lines = f.readlines()
    return [int(n) for n in lines[0].split(",")]


def part1(fish: List[int]) -> int:
    """
    Solve part 1.
    @param fish: List of fish with each value representing the number of days until the fish creates a new fish.
    @return: Number of fish after 80 days.
    """
    days = 80
    nb_fish = len(fish)
    memo = {}

    i = 0
    while i < len(fish):
        if fish[i] not in memo:
            creation_days = []
            j = 0
            while fish[i] + 1 + j * 7 <= days:
                creation_days.append(fish[i] + 1 + j * 7)
                j += 1
            memo[fish[i]] = creation_days
        for creation_day in memo[fish[i]]:
            fish.append(creation_day + 8)
            nb_fish += 1
        i += 1
    return nb_fish


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input("input.txt")
    print(part1(puzzle_input))


solve()

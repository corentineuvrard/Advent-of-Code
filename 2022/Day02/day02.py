from typing import List


def parse_input(input_file: str) -> List[List[str]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List representing the rounds of the strategy guide.
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()
        rounds = []
        for line in lines:
            rounds.append([line[0], line[2]])
    return rounds


def part1(rounds: List[List[str]]) -> int:
    """
    Solve part 1.
    @param rounds: List representing the rounds of the strategy guide.
    @return: Total score obtained when following the strategy guide.
    """
    score = 0
    for r in rounds:
        match r:
            case ['A', 'X']:  # Player 1: Rock | Player 2: Rock
                score += 1 + 3
            case ['A', 'Y']:  # Player 1: Rock | Player 2: Paper
                score += 2 + 6
            case ['A', 'Z']:  # Player 1: Rock | Player 2: Scissors
                score += 3 + 0
            case ['B', 'X']:  # Player 1: Paper | Player 2: Rock
                score += 1 + 0
            case ['B', 'Y']:  # Player 1: Paper | Player 2: Paper
                score += 2 + 3
            case ['B', 'Z']:  # Player 1: Paper | Player 2: Scissors
                score += 3 + 6
            case ['C', 'X']:  # Player 1: Scissors | Player 2: Rock
                score += 1 + 6
            case ['C', 'Y']:  # Player 1: Scissors | Player 2: Paper
                score += 2 + 0
            case ['C', 'Z']:  # Player 1: Scissors | Player 2: Scissors
                score += 3 + 3
    return score


def part2(rounds: List[List[str]]) -> int:
    """
    Solve part 2.
    @param rounds: List representing the rounds of the strategy guide.
    @return: Total score obtained if everything goes according to the strategy guide.
    """
    score = 0
    for r in rounds:
        match r:
            case ['A', 'X']:  # Player 1: Rock | Player 2 needs to lose (Scissors)
                score += 0 + 3
            case ['A', 'Y']:  # Player 1: Rock | Player 2 needs to end the round in a draw (Rock)
                score += 3 + 1
            case ['A', 'Z']:  # Player 1: Rock | Player 2 needs to win (Paper)
                score += 6 + 2
            case ['B', 'X']:  # Player 1: Paper | Player 2 needs to lose (Rock)
                score += 0 + 1
            case ['B', 'Y']:  # Player 1: Paper | Player 2 needs to end the round in a draw (Paper)
                score += 3 + 2
            case ['B', 'Z']:  # Player 1: Paper | Player 2 needs to win (Scissors)
                score += 6 + 3
            case ['C', 'X']:  # Player 1: Scissors | Player 2 needs to lose (Paper)
                score += 0 + 2
            case ['C', 'Y']:  # Player 1: Scissors | Player 2 needs to end the round in a draw (Scissors)
                score += 3 + 3
            case ['C', 'Z']:  # Player 1: Scissors | Player 2 needs to win (Rock)
                score += 6 + 1
    return score


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

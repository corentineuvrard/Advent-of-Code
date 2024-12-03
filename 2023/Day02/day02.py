import re
from typing import List, Optional, Tuple


def parse_line(line: str) -> Optional[Tuple[int, List[List[Tuple[int, str]]]]]:
    """
    Parse a single line into a structured format.
    @param line: Single line in the format 'Game <number>: <details>'.
    @return: List where the first element is the game ID, and the subsequent elements are lists of tuples containing
        respective counts and colors. Return None if the line doesn't match the format.
    """
    match = re.match(pattern=r'Game (\d+): (.+)', string=line)
    if match:
        game_id = int(match.group(1))
        color_groups = match.group(2).split(';')

        # Parse each group into a list
        parsed_groups = []
        for group in color_groups:
            items = re.findall(pattern=r'(\d+) ([a-z]+)', string=group)
            parsed_group = [(int(count), color) for count, color in items]
            parsed_groups.append(parsed_group)

        return game_id, parsed_groups
    return None


def parse_input(input_file: str) -> List[Tuple[int, List[List[Tuple[int, str]]]]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List of games.
    """
    with open(input_file, 'r') as f:
        games = []

        for line in f:
            line = line.strip()
            if line:
                parsed_line = parse_line(line)
                if parsed_line:
                    games.append(parsed_line)

    return games


def part1(games: List[Tuple[int, List[List[Tuple[int, str]]]]]) -> int:
    """
    Solve part 1.
    @param games: List of games.
    @return: Sum of the IDs of possible games.
    """
    id_sum = 0
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}

    for game in games:
        game_id, color_groups = game
        id_sum += game_id
        game_possible = True

        for color_group in color_groups:
            if not game_possible:
                break
            for count, color in color_group:
                if count > max_cubes[color]:
                    game_possible = False
                    id_sum -= game_id
                    break

    return id_sum



def part2(games: List[Tuple[int, List[List[Tuple[int, str]]]]]) -> int:
    """
    Solve part 2.
    @param games: List of games.
    @return: Sum of the power of the given sets.
    """
    power_sum = 0

    for game in games:
        game_id, color_groups = game
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}

        for color_group in color_groups:
            for count, color in color_group:
                if count > min_cubes[color]:
                    min_cubes[color] = count

        power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
        power_sum += power

    return power_sum


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
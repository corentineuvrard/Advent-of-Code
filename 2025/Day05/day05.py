def parse_input(input_file: str) -> list[list]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Database consisting of a list of fresh ingredient ID ranges
        and a list of available ingredient IDs.
    """
    database= [[], []]
    is_ingredient = False

    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if is_ingredient:
                database[1].append(int(line))
            else:
                if len(line) == 0:
                    is_ingredient = True
                else:
                    start, end = line.split('-')
                    database[0].append((int(start), int(end)))

    return database


def part1(database: list[list]) -> int:
    """
    Solve part 1.
    @param database: Database consisting of a list of fresh ingredient
        ID ranges and a list of available ingredient IDs.
    @return: Number of available ingredient IDs that are fresh.
    """
    fresh_ids = 0

    for ingredient_id in database[1]:
        for start, end in database[0]:
            if start <= ingredient_id <= end:
                fresh_ids += 1
                break

    return fresh_ids


def part2(database: list[list]) -> int:
    """
    Solve part 2.
    @param database: Database consisting of a list of fresh ingredient
        ID ranges and a list of available ingredient IDs.
    @return: Number of ingredient IDs considered to be fresh.
    """
    fresh_ids = 0

    prev_range = ()
    sorted_ranges = sorted(database[0])

    for start, end in sorted_ranges:
        if prev_range:
            if start > prev_range[1]:
                fresh_ids += end + 1 - start
            else:
                if prev_range[1] < end:
                    fresh_ids += end - prev_range[1]
        else:
            fresh_ids += end + 1 - start
        prev_range = (start, end)

    return fresh_ids


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
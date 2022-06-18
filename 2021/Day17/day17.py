from typing import Tuple, List


def parse_input(input_file: str) -> Tuple[List[int], List[int]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Tuple representing the boundaries of the target area on both axes.
    """
    with open(input_file, 'r') as f:
        line = f.readlines()[0][15:]
        str_x, str_y = line.split(', y=')
        tx = [int(x) for x in str_x.split('..')]
        ty = [int(y) for y in str_y.split('..')]
        return tx, ty


def part1(target: Tuple[List[int], List[int]]) -> int:
    """
    Solve part 1.
    @param target: Boundaries of the target area on both axes.
    @return: Highest position the probe can reach on the y-axis while reaching the target area.
    """
    _, ty = target
    vy = abs(ty[0]) - 1
    return vy * (vy + 1) // 2


def part2(target: Tuple[List[int], List[int]]) -> int:
    """
    Solve part 2.
    @param target: Boundaries of the target area on both axes.
    @return: Number of distinct initial velocity values that cause the probe to be within the target area after any
    steps.
    """
    tx, ty = target
    nb_good_shots = 0

    # Find the minimum x value to start the search from
    min_x = 0
    while (min_x * (min_x + 1)) / 2 < tx[0]:
        min_x += 1

    for x in range(min_x, tx[1] + 1):
        for y in range(ty[0], abs(ty[0])):
            px, py = 0, 0
            dx, dy = x, y
            # Check all the positions of the probe
            while px < tx[0] or py > ty[1]:
                px += dx
                if dx > 0:
                    dx -= 1
                py += dy
                dy -= 1
            # Check if the probe reached the target area
            if px <= tx[1] and py >= ty[0]:
                nb_good_shots += 1

    return nb_good_shots


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input("input.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

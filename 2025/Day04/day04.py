import numpy as np
from scipy.signal import convolve2d


def parse_input(input_file: str) -> np.ndarray:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Diagram indicating where the rolls are located.
    """
    with open(input_file, 'r') as f:
        return np.array([list(line.strip()) for line in f])


def part1(grid: np.ndarray) -> int:
    """
    Solve part 1.
    @param grid: Diagram indicating where the rolls are located.
    @return: Number of rolls of paper that can be accessed by a
        forklift.
    """
    nb_rolls = 0

    ord_grid = np.vectorize(ord)(grid)

    kernel = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])

    neighbor_sum = convolve2d(
        ord_grid,
        kernel,
        mode="same",
        boundary="fill",
        fillvalue=0
    )  # type: np.ndarray

    h, w = grid.shape
    for r in range(h):
        for c in range(w):
            if grid[r][c] == '@':  # roll of paper
                # Roll located on an edge -> 5 neighbors
                if r in (0, h-1) or c in (0, w-1):
                    # Max sum on an edge:
                    # -> 4 * ord('@') + 1 * ord('.')
                    # => 4 * 64 + 1 * 46
                    # => 302
                    if neighbor_sum[r][c] < 302:
                        nb_rolls += 1
                # Roll located in the center -> 8 neighbors
                else:
                    # Max sum in the center:
                    # -> 4 * ord('@') + 4 * ord('.')
                    # => 4 * 64 + 4 * 46
                    # => 440
                    if neighbor_sum[r][c] < 440:
                        nb_rolls += 1

    return nb_rolls


def part2(grid: np.ndarray) -> int:
    """
    Solve part 2.
    @param grid: Diagram indicating where the rolls are located.
    @return: Number of rolls of paper that can be accessed by a
        forklift.
    """
    nb_rolls = 0

    prev = -1
    while nb_rolls != prev:
        prev = nb_rolls

        ord_grid = np.vectorize(ord)(grid)

        kernel = np.array([
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ])

        neighbor_sum = convolve2d(
            ord_grid,
            kernel,
            mode="same",
            boundary="fill",
            fillvalue=0
        )  # type: np.ndarray

        h, w = grid.shape
        for r in range(h):
            for c in range(w):
                if grid[r][c] == '@':  # roll of paper
                    # Roll located on an edge -> 5 neighbors
                    if r in (0, h-1) or c in (0, w-1):
                        # Max sum on an edge:
                        # -> 4 * ord('@') + 1 * ord('.')
                        # => 4 * 64 + 1 * 46
                        # => 302
                        if neighbor_sum[r][c] < 302:
                            nb_rolls += 1
                            grid[r][c] = '.'  # remove the roll in-place
                    # Roll located in the center -> 8 neighbors
                    else:
                        # Max sum in the center:
                        # -> 4 * ord('@') + 4 * ord('.')
                        # => 4 * 64 + 4 * 46
                        # => 440
                        if neighbor_sum[r][c] < 440:
                            nb_rolls += 1
                            grid[r][c] = '.'  # remove the roll in-place

    return nb_rolls


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
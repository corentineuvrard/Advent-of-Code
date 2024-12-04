from typing import List, Tuple


def parse_input(input_file: str) -> List[str]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Word search puzzle.
    """
    with open(input_file, 'r') as f:
        puzzle = [line.strip() for line in f]

    return puzzle


def find_word(matrix: List[str], coords: Tuple[int, int], word: str = 'XMAS') -> int:
    """
    Check if the given word can be found in the matrix at the given coordinates.
    @param matrix: Word search puzzle.
    @param coords: Coordinates in the matrix where the word starts.
    @param word: Word to find in the matrix.
    @return: Number of times the word is found at the given coordinates.
    """
    row, col = coords
    length = len(word)
    found = 0

    # Helper function to check if a word exists in a specific direction
    def is_word_found(delta_row: int, delta_col: int) -> bool:
        for i in range(length):
            new_row = row + i * delta_row
            new_col = col + i * delta_col
            # Check bounds
            if not (0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0])):
                return False
            # Check character match
            if matrix[new_row][new_col] != word[i]:
                return False
        return True

    # Directions to check
    directions = [
        (-1, 0),  # Up
        (-1, 1),  # Up-Right
        (0, 1),   # Right
        (1, 1),   # Down-Right
        (1, 0),   # Down
        (1, -1),  # Down-Left
        (0, -1),  # Left
        (-1, -1)  # Up-Left
    ]

    # Check all directions
    for d_row, d_col in directions:
        if is_word_found(d_row, d_col):
            found += 1

    return found


def part1(matrix: List[str]) -> int:
    """
    Solve part 1.
    @param matrix: Word search puzzle.
    @return: Number of times the word 'XMAS' is found in the matrix.
    """
    found = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'X':
                found += find_word(matrix, coords=(row, col))

    return found


def part2(matrix: List[str]) -> int:
    """
    Solve part 2.
    @param matrix: Word search puzzle.
    @return: Number of times an 'X-MAS' is found in the matrix.
    """
    found = 0

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[0]) - 1):
            if matrix[row][col] == 'A':
                # Define conditions for checking the desired pattern
                c1 = (matrix[row - 1][col + 1] == 'M' and matrix[row + 1][col - 1] == 'S')  # top-bottom / diagonal
                c2 = (matrix[row + 1][col - 1] == 'M' and matrix[row - 1][col + 1] == 'S')  # bottom-top / diagonal
                c3 = (matrix[row - 1][col - 1] == 'M' and matrix[row + 1][col + 1] == 'S')  # top-bottom \ diagonal
                c4 = (matrix[row + 1][col + 1] == 'M' and matrix[row - 1][col - 1] == 'S')  # bottom-top \ diagonal

                # If any combination of conditions is met, increment the counter
                if (c1 or c2) and (c3 or c4):
                    found += 1

    return found


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))

solve()
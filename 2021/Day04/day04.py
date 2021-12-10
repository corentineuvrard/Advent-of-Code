from typing import Tuple, List


class Board:
    """
    Class to represent a Bingo board.
    ...

    Attributes
    ----------
    id: int
        Number to identify the board.
    numbers: Dict[int, Tuple[int, int]]
        Numbers of the board with their coordinates on the board.
    rows: List[int]
        Number of marked numbers per row.
    columns: List[int]
        Number of marked numbers per column.
    marked_numbers: Set[int]
        Numbers of the board that have been marked.
    winning_number: int
        Number that completed a row or a column of the board.
    _nb_numbers_checked: int
        Number of numbers that have been checked on the board.

    Methods
    -------
    get_score():
        Get the score of the board by multiplying the sum of unmarked numbers by the winning number.
    is_win() -> bool:
        Verify that at least one row or one column of the board has 5 marked numbers.
    nb_numbers_checked() -> int:
        Get the number of numbers that have been checked on the board.
    play(draw: List[int]):
        Play bingo with the board until all numbers in a row or a column are marked.
    """
    def __init__(self, board_id, board_numbers):
        """
        Construct all the necessary attributes for the Board object.
        @param board_id: ID of the board.
        @param board_numbers: Numbers of the board.
        """
        self.id = board_id
        self.numbers = board_numbers
        self.rows = [0, 0, 0, 0, 0]
        self.columns = [0, 0, 0, 0, 0]
        self.marked_numbers = set()
        self.winning_number = None
        self._nb_numbers_checked = 0

    def get_score(self) -> int:
        """
        Get the score of the board by multiplying the sum of unmarked numbers by the winning number.
        @return: Score of the board. 0 if the board does not have any row or column with only marked numbers.
        """
        if self.winning_number:
            non_marked_numbers = [n for n in self.numbers if n not in self.marked_numbers]
            return self.winning_number * sum(non_marked_numbers)
        return 0

    @property
    def is_win(self) -> bool:
        """
        Verify that at least one row or one column of the board has 5 marked numbers.
        @return: Return True if a row or a column of the board is fully marked, False otherwise.
        """
        return 5 in self.rows or 5 in self.columns

    @property
    def nb_numbers_checked(self) -> int:
        """
        Get the number of numbers that have been checked on the board.
        @return: Number of numbers that have been checked on the board.
        """
        return self._nb_numbers_checked

    def play(self, draw: List[int]) -> None:
        """
        Play bingo with the board until all numbers in a row or a column are marked.
        @param draw: List of numbers to be drawn.
        """
        while not self.is_win:
            if draw[self._nb_numbers_checked] in self.numbers:
                self.marked_numbers.add(draw[self._nb_numbers_checked])
                coord_x, coord_y = self.numbers[draw[self._nb_numbers_checked]]
                self.columns[coord_x] += 1
                self.rows[coord_y] += 1
            self._nb_numbers_checked += 1
        self.winning_number = draw[self._nb_numbers_checked - 1]


def parse_input(input_file: str) -> Tuple[List[int], List[Board]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List of numbers to be drawn and list of Bingo boards.
    """
    with open(input_file, "r") as f:
        file = f.read().split("\n\n")
    draw = [int(n) for n in file[0].split(",")]
    boards = []
    for board_id, board_str in enumerate(file[1:]):
        numbers = {}
        for number_id, number_str in enumerate(board_str.split()):
            number = int(number_str)
            coord_x = number_id % 5
            coord_y = number_id // 5
            numbers[number] = (coord_x, coord_y)
        boards.append(Board(board_id, numbers))
    return draw, boards


def part1(bingo: Tuple[List[int], List[Board]]):
    """
    Solve part 1.
    @param bingo: List of numbers to be drawn and list of Bingo boards.
    @return: Score of the best board.
    """
    draw, boards = bingo
    best_board = [None, len(draw)]
    for id_board, board in enumerate(boards):
        board.play(draw)
        nb_numbers_checked = board.nb_numbers_checked
        if nb_numbers_checked < best_board[1]:
            best_board = [id_board, nb_numbers_checked]
    return boards[best_board[0]].get_score()


def part2(bingo: Tuple[List[int], List[Board]]):
    """
    Solve part 2.
    @param bingo: List of numbers to be drawn and list of Bingo boards.
    @return: Score of the worst board.
    """
    draw, boards = bingo
    worst_board = [None, 0]
    for id_board, board in enumerate(boards):
        board.play(draw)
        nb_numbers_checked = board.nb_numbers_checked
        if nb_numbers_checked > worst_board[1]:
            worst_board = [id_board, nb_numbers_checked]
    return boards[worst_board[0]].get_score()


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input("input.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

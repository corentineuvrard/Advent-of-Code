from typing import Tuple, Union, List
import numpy as np


def get_input() -> Tuple[Union[List[int], List[List[List[int]]]]]:
    with open("input.txt", "r") as f:
        lines = f.readlines()
    numbers = [int(n) for n in lines[0].split(",")]
    boards = []
    current_board = []
    for line in lines[2:]:
        if len(line) > 1:
            row = [int(n) for n in line.split()]
            current_board.append(row)
        else:
            boards.append(current_board)
            current_board = []
    boards.append(current_board)
    return numbers, np.array(boards)


def check_win(board_marks: List[List[bool]]) -> Tuple[int, bool]:
    win = False
    for row in board_marks:
        if row.count(True) == 5:
            win = True
    return win


def mark_board(board: List[List[int]], board_marks: List[List[bool]], numbers: List[int]):
    for i, row in enumerate(board):
        board_marks[i] = [numbers[j] in row for j in range(len(numbers))]


def get_win_info(numbers: List[int], boards: List[List[List[int]]], marks: List[List[List[int]]]) -> Tuple[int, int]:
    start_index = 0
    end_index = 5
    max_marks = 0
    while start_index < len(numbers):
        numbers_to_check = numbers[start_index:end_index]
        for b in range(len(boards)):
            for row in range(5):
                for col in range(5):
                    for current_number in numbers_to_check:
                        if boards[b][row][col] == current_number:
                            marks[b][row][col] = True
                    nb_marks_row = marks[b][row].count(True)
                    nb_marks_col = [row[col] for row in marks[b]].count(True)
                    if nb_marks_row == 5 or nb_marks_col == 5:
                        return b, current_number
                    else:
                        max_marks = max(max_marks, max(nb_marks_row, nb_marks_col))
        start_index = end_index
        end_index = start_index + 5 - max_marks


def part1(numbers: List[int], boards: List[List[List[int]]]) -> int:
    marks = [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]
    winning_board, winning_number = get_win_info(numbers, boards, marks)
    unmarked = [boards[winning_board][r][c] for r in range(5) for c in range(5) if not marks[winning_board][r][c]]
    return sum(unmarked) * winning_number


def get_loss_info(numbers: List[int], boards: List[List[List[int]]], marks: List[List[List[int]]]) -> Tuple[int, int]:
    start_index = 0
    end_index = 5
    max_marks = 0
    winning_boards = set()
    while len(winning_boards) < len(boards):
        numbers_to_check = numbers[start_index:end_index]
        for b in [board_id for board_id in range(len(boards)) if board_id not in winning_boards]:
            for row in range(5):
                for col in range(5):
                    for current_number in numbers_to_check:
                        if boards[b][row][col] == current_number:
                            marks[b][row][col] = True
                    nb_marks_row = marks[b][row].count(True)
                    nb_marks_col = [row[col] for row in marks[b]].count(True)
                    if nb_marks_row == 5 or nb_marks_col == 5:
                        print(b, current_number)
                        if len(winning_boards) == len(boards) - 1:
                            return b, current_number
                        else:
                            winning_boards.add(b)
                            break
                    else:
                        max_marks = max(max_marks, max(nb_marks_row, nb_marks_col))
        start_index = end_index
        end_index = start_index + 5 - max_marks


def part2(numbers: List[int], boards: List[List[List[int]]]) -> int:
    '''
    numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]

    boards = [[[22, 13, 17, 11, 0],
               [8, 2, 23, 4, 24],
               [21, 9, 14, 16, 7],
               [6, 10, 3, 18, 5],
               [1, 12, 20, 15, 19]],

              [[3, 15, 0, 2, 22],
               [9, 18, 13, 17, 5],
               [19, 8, 7, 25, 23],
               [20, 11, 10, 24, 4],
               [14, 21, 16, 12, 6]],

              [[14, 21, 17, 24, 4],
               [10, 16, 15, 9, 19],
               [18, 8, 23, 26, 20],
               [22, 11, 13, 6, 5],
               [2, 0, 12, 3, 7]]]
    '''
    marks = [[[False for i in range(5)] for j in range(5)] for k in range(len(boards))]
    last_board, last_number = get_loss_info(numbers, boards, marks)
    unmarked = [boards[last_board][r][c] for r in range(5) for c in range(5) if not marks[last_board][r][c]]
    return sum(unmarked) * last_number


def solve():
    numbers, boards = get_input()
    print(part1(numbers, boards))
    print(part2(numbers, boards))


solve()

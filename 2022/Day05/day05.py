from typing import Tuple, List
from collections import defaultdict, deque
from copy import deepcopy
import time


def parse_input(input_file: str) -> Tuple[defaultdict[int, deque], List[List[int]]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Tuple containing a dictionary of the stacks and the moves that have to be performed.
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()
        stacks = defaultdict(deque)
        moves = []
        for line in lines:
            if line[0] == 'm':
                moves.append([int(s) for s in line.split() if s.isdigit()])
            else:
                for i, s in enumerate(line):
                    if 'A' <= s <= 'Z':
                        key = i // 4 + 1
                        stacks[key].appendleft(s)
    return stacks, moves


def part1(input_tuple: Tuple[defaultdict[int, deque], List[List[int]]]) -> str:
    """
    Solve part 1.
    @param input_tuple: Tuple containing a dictionary of the stacks and the moves that have to be performed.
    @return: The crates that end up at the top of the stacks.
    """
    stacks, moves = input_tuple
    stacks = deepcopy(stacks)
    top_crates = ''
    for move in moves:
        for _ in range(move[0]):
            stacks[move[2]].append(stacks[move[1]].pop())
    for i in range(len(stacks)):
        top_crates += stacks[i + 1][-1]
    return top_crates


def part2(input_tuple: Tuple[defaultdict[int, deque], List[List[int]]]) -> str:
    """
    Solve part 2.
    @param input_tuple: Tuple containing a dictionary of the stacks and the moves that have to be performed.
    @return: The number of assignments pairs where ranges overlap.
    """
    stacks, moves = input_tuple
    stacks = deepcopy(stacks)
    top_crates = ''
    for move in moves:
        temp_stack = deque([])
        for _ in range(move[0]):
            temp_stack.appendleft(stacks[move[1]].pop())
        stacks[move[2]].extend(temp_stack)
    for i in range(len(stacks)):
        top_crates += stacks[i + 1][-1]
    return top_crates


def solve() -> None:
    """
    Solve the puzzle
    """
    t0 = time.perf_counter()
    puzzle_input = parse_input('input.txt')
    t1 = time.perf_counter()
    print(t1 - t0)
    print(part1(puzzle_input))
    t2 = time.perf_counter()
    print(t2 - t1)
    print(part2(puzzle_input))
    print(time.perf_counter() - t2)


solve()

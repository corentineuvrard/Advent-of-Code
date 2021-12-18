from typing import List


def parse_input(input_file: str) -> List[str]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List of chunks.
    """
    with open(input_file, "r") as f:
        content = f.read()
    return content.split()


def part1(chunks: List[str]) -> int:
    """
    Solve part 1.
    @param chunks: List of chunks.
    @return: Total syntax error score.
    """
    points = 0
    for chunk in chunks:
        brackets = []
        for bracket in chunk:
            if bracket in ['(', '[', '{', '<']:
                brackets.append(bracket)
            else:
                last_input = brackets.pop()
                if bracket == ')' and last_input != '(':
                    points += 3
                    break
                elif bracket == ']' and last_input != '[':
                    points += 57
                    break
                elif bracket == '}' and last_input != '{':
                    points += 1197
                    break
                elif bracket == '>' and last_input != '<':
                    points += 25137
                    break
    return points


def part2(chunks: List[str]) -> int:
    """
    Solve part 2.
    @param chunks: List of chunks.
    @return: Middle score.
    """
    scores = []
    points = {'(': 1, '[': 2, '{': 3, '<': 4}
    for chunk in chunks:
        score = 0
        brackets = []
        for bracket in chunk:
            if bracket in ['(', '[', '{', '<']:
                brackets.append(bracket)
            else:
                last_input = brackets.pop()
                if bracket == ')' and last_input != '(':
                    break
                elif bracket == ']' and last_input != '[':
                    break
                elif bracket == '}' and last_input != '{':
                    break
                elif bracket == '>' and last_input != '<':
                    break
        else:
            while len(brackets) > 0:
                score *= 5
                score += points[brackets.pop()]
            scores.append(score)
    scores.sort()
    return scores[(len(scores) - 1) // 2]


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input("input.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

def parse_input(input_file: str) -> list[list[str]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Diagram of the tachyon manifold.
    """
    with open(input_file, 'r') as f:
        return [list(line.strip()) for line in f]


def part1(diagram: list[list[str]]) -> int:
    """
    Solve part 1.
    @param diagram: Diagram of the tachyon manifold.
    @return: Number of times the beam will be split.
    """
    rows, cols = len(diagram), len(diagram[0])
    splitters = set()
    
    stack = [find_start(diagram)]
    while stack:
        row, col = stack.pop()
        if len(splitters) == 0:
            start_cols = [col]
        else:
            start_cols = [col - 1, col + 1]
        for c in start_cols:
            if 0 <= c < cols:
                for r in range(row, rows):
                    if diagram[r][c] == '^':
                        if (r, c) not in splitters:
                            stack.append((r, c))
                        splitters.add((r, c))
                        break
                        
    return len(splitters)


def part2(diagram: list[list[str]]) -> int:
    """
    Solve part 2.
    @param diagram: Diagram of the tachyon manifold.
    @return: Number of different timelines a single tachyon particle
        would end up on.
    """
    rows, cols = len(diagram), len(diagram[0])
    memo = {}
    
    def count_timeline(location: tuple[int, int]) -> int:
        r, c = location
        
        if r == rows:
            return 1
        
        if location in memo:
            return memo[location]

        left, right, down = (r, c - 1), (r, c + 1), (r + 1, c)
        if diagram[r][c] == '^':
            if c == 0:
                memo[location] = count_timeline(right)
            elif c == cols - 1:
                memo[location] = count_timeline(left)
            else:
                memo[location] = count_timeline(right) + count_timeline(left)
        else:
            memo[location] = count_timeline(down)
        return memo[location]
            
    return count_timeline(find_start(diagram))


def find_start(diagram: list[list[str]]) -> tuple[int, int]:
    """
    Find the location where the tachyon beam enters the manifold.
    :param diagram: Diagram of the tachyon manifold.
    :return: Coordinates of the start location of the tachyon beam.
    """
    rows, cols = len(diagram), len(diagram[0])
    for r in range(rows):
        for c in range(cols):
            if diagram[r][c] == 'S':
                return r, c
    raise ValueError("No start 'S' found in diagram.")


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
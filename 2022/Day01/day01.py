from typing import List


def parse_input(input_file: str) -> List[List[int]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List representing the calories of the food carried by the elves.
    """
    with open(input_file, 'r') as f:
        calories = []
        elf_calories = []
        for line in f:
            if line == '\n':
                calories.append(elf_calories)
                elf_calories = []
            else:
                elf_calories.append(int(line.strip()))
        calories.append(elf_calories)

    return calories


def part1(calories: List[List[int]]) -> int:
    """
    Solve part 1.
    @param calories: List representing the calories of the food carried by the elves.
    @return: Total calories carried by the elf carrying the most calories.
    """
    return max(list(map(sum, calories)))


def part2(calories: List[List[int]]) -> int:
    """
    Solve part 2.
    @param calories: List representing the calories of the food carried by the elves.
    @return: Total calories carried by the three elves carrying the most calories.
    """
    total_calories = list(map(sum, calories))
    total_calories.sort(reverse=True)
    return sum(total_calories[:3])


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

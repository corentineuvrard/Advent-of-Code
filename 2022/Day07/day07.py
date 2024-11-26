from typing import Dict, List, Union
import time


def parse_input(input_file: str) -> Dict[str, List]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Dictionary with directories as keys and their contents as values.
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()

    filesystem = dict()
    current_path = "/"
    stack = [current_path]

    for line in lines:
        line_elements = line.split()
        if line_elements[0] == "$":  # Command line
            if line_elements[1] == "cd":  # Change directory
                if line_elements[2] == "..":  # Move up
                    stack.pop()
                else:  # Move down
                    if line_elements[2] == "/":
                        current_path = line_elements[2]
                    else:
                        current_path = f"{stack[-1]}/{line_elements[2]}".strip("/")
                    stack.append(current_path)
                    filesystem[current_path] = []  # Initialize directory
        elif line_elements[0] == "dir":  # Directory
            filesystem[stack[-1]].append(line_elements[1])  # Add directory name
        else:  # File
            filesystem[stack[-1]].append([int(line_elements[0]), line_elements[1]])  # Add file with size and name

    return filesystem


def get_directory_size(directory: str, filesystem: Dict[str, List[Union[str, List[int]]]], memo: Dict[str, int]) -> int:
    """
    Recursively compute the size of a directory.
    @param directory: Directory to calculate size for.
    @param filesystem: Dictionary of directories and their contents.
    @param memo: Memoization dictionary for directory sizes.
    @return: Total size of the directory.
    """
    if directory in memo:
        return memo[directory]

    size = 0
    for item in filesystem[directory]:
        if isinstance(item, list):  # File
            size += item[0]
        else:  # Subdirectory
            subdirectory_path = f"{directory}/{item}".strip("/")
            size += get_directory_size(subdirectory_path, filesystem, memo)

    memo[directory] = size
    return size


def part1(filesystem: Dict[str, List[Union[str, List[int]]]]) -> int:
    """
    Solve part 1.
    @param filesystem: Dictionary of directories and their contents.
    @return: Sum of the total sizes of the directories with a total size of at most 100,000.
    """
    total_size = 0

    for directory in filesystem:
        directory_size = get_directory_size(directory, filesystem, dict())
        if directory_size <= 100_000:
            total_size += directory_size

    return total_size


def part2(filesystem: Dict[str, List[Union[str, List[int]]]]) -> int:
    """
    Solve part 2.
    @param filesystem: Dictionary of directories and their contents.
    @return:
    """
    memo = dict()
    used_space = get_directory_size(directory="/", filesystem=filesystem, memo=memo)
    unused_space = 70_000_000 - used_space
    min_space_to_free_up = 30_000_000 - unused_space

    file_size = used_space
    for _, size in memo.items():
        if min_space_to_free_up < size < file_size:
            file_size = size

    return file_size


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

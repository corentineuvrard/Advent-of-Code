from sortedcontainers import SortedDict
from typing import List


def parse_input(input_file: str) -> List[int]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List representing disk blocks.
    """
    with open(input_file, 'r') as f:
        disk_blocks = []
        for i, character in enumerate(f.readline()):
            for _ in range(int(character)):
                # File blocks
                if i % 2 == 0:
                    disk_blocks.append(i // 2)
                # Free space blocks
                else:
                    disk_blocks.append(-1)

    return disk_blocks


def part1(disk_blocks: List[int]) -> int:
    """
    Solve part 1.
    @param disk_blocks: List representing disk blocks.
    @return: Filesystem checksum.
    """
    blocks = disk_blocks.copy()

    left_index, right_index = 0, len(blocks) - 1

    while left_index < right_index:
        if blocks[left_index] != -1:
            left_index += 1
        elif blocks[right_index] == -1:
            right_index -= 1
        else:
            blocks[left_index] = blocks[right_index]
            blocks[right_index] = -1
            left_index += 1
            right_index -= 1

    checksum = sum(i * block for i, block in enumerate(blocks) if block != -1)

    return checksum


def part2(disk_blocks: List[int]) -> int:
    """
    Solve part 2.
    @param disk_blocks: List representing disk blocks.
    @return: Filesystem checksum.
    """
    blocks = disk_blocks.copy()
    n = len(blocks)

    # Dictionary to track free spaces:
    # key = starting index
    # value = size of the free space
    free_spaces = SortedDict()

    # Initialize free spaces from the disk state
    start = -1
    for i in range(n):
        if blocks[i] == -1:
            if start == -1:
                start = i  # Mark the start of a free space
        else:
            if start != -1:
                free_spaces[start] = i - start
                start = -1

    max_file_size = None  # Variable to keep track of the largest file size that couldn't be moved

    # Process files from right to left
    right_index = n - 1
    while right_index >= 0 and (len(free_spaces) == 0 or right_index >= next(iter(free_spaces))):
        # Skip free spaces (-1)
        if blocks[right_index] == -1:
            right_index = next((i for i in range(right_index, - 1, -1) if blocks[i] != -1), - 1)
            continue

        # Identify the current file and its size
        current_file_id = blocks[right_index]
        file_size = 1
        while right_index - file_size >= 0 and blocks[right_index - file_size] == current_file_id:
            file_size += 1

        # Skip the file if its size is greater than or equal to 'max_file_size'
        if max_file_size is not None and file_size >= max_file_size:
            right_index -= file_size
            continue

        # Try to find a place for this file in the free space dictionary
        for start, size in free_spaces.items():
            # Ensure files are only moved to the left
            if start >= right_index:
                break
            if size >= file_size:
                # If we find enough space, place the file at the beginning of the free space
                blocks[start:start + file_size] = [current_file_id] * file_size
                # Remove the file from its original location
                blocks[right_index - file_size + 1:right_index + 1] = [-1] * file_size

                # Remove the free space occupied by the moved file
                del free_spaces[start]

                # Update the free space dictionary if moving the file did not fill the free space entirely
                if size > file_size:
                    free_spaces[start + file_size] = size - file_size

                max_file_size = None
                break
        else:
            # If no space was found, set 'max_file_size'
            max_file_size = file_size

        # Move the right index back after attempting to move or skip the file
        right_index -= file_size

    checksum = sum(i * block for i, block in enumerate(blocks) if block != -1)

    return checksum


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
from typing import List


def parse_input(input_file: str) -> List[List[str]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List representing the rucksacks and the items they contain in each compartment.
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()
        rucksacks = []
        for line in lines:
            nb_items = len(line) - 1
            half = nb_items // 2
            rucksacks.append([line[:half], line[half:nb_items]])
    return rucksacks


def item_type_to_priority(item_type: str) -> int:
    """
    Convert an item type to a priority.
    @param item_type: Type of the item.
    @return: The priority corresponding to the given item type.
    """
    priority = ord(item_type) - 96
    if priority < 0:
        priority += 58
    return priority


def part1(rucksacks: List[List[str]]) -> int:
    """
    Solve part 1.
    @param rucksacks: List representing the rucksacks and the items they contain in each compartment.
    @return: The sum of the priorities of the item types that appear in both compartments of each rucksack.
    """
    priorities_sum = 0
    for rucksack in rucksacks:
        priorities_sum += item_type_to_priority([item for item in rucksack[0] if item in rucksack[1]][0])
    return priorities_sum


def part2(rucksacks: List[List[str]]) -> int:
    """
    Solve part 2.
    @param rucksacks: List representing the rucksacks and the items they contain in each compartment.
    @return: The sum of the priorities of the badge item types of each group of 3 Elves.
    """
    priorities_sum = 0
    for rucksack_id in range(0, len(rucksacks), 3):
        rucksack_1 = rucksacks[rucksack_id][0] + rucksacks[rucksack_id][1]
        rucksack_2 = rucksacks[rucksack_id + 1][0] + rucksacks[rucksack_id + 1][1]
        rucksack_3 = rucksacks[rucksack_id + 2][0] + rucksacks[rucksack_id + 2][1]
        badge_item_type = [item for item in rucksack_1 if item in rucksack_2 and item in rucksack_3][0]
        priorities_sum += item_type_to_priority(badge_item_type)
    return priorities_sum


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

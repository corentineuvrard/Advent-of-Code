from collections import defaultdict
from typing import Dict, List, Set, Tuple


def parse_input(input_file: str) -> Tuple[Dict[int, Set[int]], List[List[int]]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Tuple where the first element is a dictionary representing the page ordering rules,
             and the second element is a list of lists of integers representing the update pages.
    """
    with open(input_file, 'r') as f:
        page_ordering_rules = defaultdict(set)
        update_pages = []
        rules_flag = True

        for line in f:
            line = line.strip()
            if len(line) == 0:
                rules_flag = False
                continue

            if rules_flag:
                p1, p2 = [int(n) for n in line.split('|')]
                page_ordering_rules[p2].add(p1)
            else:
                update_pages.append([int(n) for n in line.split(',')])

    return page_ordering_rules, update_pages


def is_valid_update(update: List[int], rules: Dict[int, Set[int]]) -> bool:
    """
    Checks whether a sequence of update pages is valid based on certain dependency rules.
    A valid update ensures that every required page is produced before it's needed, following the specified rules.
    @param update: List representing the sequence of update pages.
    @param rules: Dictionary where each key is a page number and the corresponding value is a set of pages
                  that must be produced before that page can be produced.
    @return: True if the update sequence is valid, meaning all dependencies are satisfied before a page is updated.
             False otherwise.
    """
    produced_pages = set()
    pages_required = set()

    for page in update:
        if page in pages_required:
            return False

        if page in rules:
            # Add pages required by the current page (that are not yet produced) to the set of required pages
            pages_required.update(rules[page] - produced_pages)

        produced_pages.add(page)

    return True


def part1(manual: Tuple[Dict[int, Set[int]], List[List[int]]]) -> int:
    """
    Solve part 1.
    @param manual: Tuple consisting of a dictionary and a list. The dictionary defines the page ordering rules,
                   where each key is an integer representing a page and the value is a set of integers indicating pages
                   that must precede the key page. The list contains page updates, where each update is
                   a list of integers representing pages.
    @return: Sum of the middle pages from all valid page updates. A page update is valid if all required pages
             according to the ordering rules are produced before they are needed.
    """
    page_ordering_rules, update_pages = manual
    sum_middle_pages = 0

    for page_sequence in update_pages:
        if is_valid_update(page_sequence, page_ordering_rules):
            middle_page_index = len(page_sequence) // 2
            sum_middle_pages += page_sequence[middle_page_index]

    return sum_middle_pages


def reorder_update(update: List[int], rules: Dict[int, Set[int]]) -> List[int]:
    """
    Reorder the update sequence to satisfy the dependency rules.
    @param update: List representing the sequence of update pages to reorder.
    @param rules: Dictionary where each key is a page number and the corresponding value is a set of pages
                  that must be produced before that page can be produced.
    @return: Reordered list of pages that satisfies the dependency rules.
    """
    new_order = []

    # Create a dependency graph for the pages in the update
    dependency_graph = {page: set() for page in update}
    for page in update:
        if page in rules:
            dependency_graph[page] = rules[page].intersection(update)

    # Topological sorting using Kahn's Algorithm
    remaining_dependencies = {page: 0 for page in update}
    for page, dependencies in dependency_graph.items():
        for _ in dependencies:
            remaining_dependencies[page] += 1

    # Collect pages with no remaining dependencies
    no_dependency_pages = [page for page in update if remaining_dependencies[page] == 0]

    while no_dependency_pages:
        page = no_dependency_pages.pop()
        new_order.append(page)

        # Reduce the remaining dependencies count for dependent pages
        for dependent_page in update:
            if page in dependency_graph[dependent_page]:
                remaining_dependencies[dependent_page] -= 1
                if remaining_dependencies[dependent_page] == 0:
                    no_dependency_pages.append(dependent_page)

    return new_order

def part2(manual: Tuple[Dict[int, Set[int]], List[List[int]]]) -> int:
    """
    Solve part 2.
    @param manual: Tuple consisting of a dictionary and a list. The dictionary defines the page ordering rules,
                   where each key is an integer representing a page and the value is a set of integers indicating pages
                   that must precede the key page. The list contains page updates, where each update is
                   a list of integers representing pages.
    @return: Sum of the middle pages from all ordered invalid page updates.
    """
    page_ordering_rules, update_pages = manual
    sum_middle_pages = 0

    for page_sequence in update_pages:
        if not is_valid_update(page_sequence, page_ordering_rules):
            page_sequence = reorder_update(page_sequence, page_ordering_rules)
            middle_page_index = len(page_sequence) // 2
            sum_middle_pages += page_sequence[middle_page_index]

    return sum_middle_pages


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
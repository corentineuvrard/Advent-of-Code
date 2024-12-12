from collections import defaultdict
from typing import Dict, List, Tuple


def parse_input(input_file: str) -> Tuple[Tuple[int, int], Dict[str, List[Tuple[int, int]]]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: Tuple of the antennas map dimensions and a dictionary containing the antennas coordinates.
    """
    with open(input_file, 'r') as f:
        antennas_coords = defaultdict(list)
        for row, line in enumerate(f):
            for col, character in enumerate(line.strip()):
                if character != '.':
                    antennas_coords[character].append((row, col))
        height, width = row + 1, col + 1

    return (width, height), antennas_coords


def part1(antennas_map: Tuple[Tuple[int, int], Dict[str, List[Tuple[int, int]]]]) -> int:
    """
    Solve part 1.
    @param antennas_map: Tuple of the antennas map dimensions and a dictionary containing the antennas coordinates.
    @return: Number of unique locations within the bounds of the map that contain an antinode.
    """
    (width, height), antennas_coords = antennas_map

    # Store the antinodes coordinates in a set
    antinodes_coords = set()

    # Check each kind of antenna
    for antenna in antennas_coords:
        antenna_coords = antennas_coords[antenna]

        # Check all possible pairs of antennas
        for i in range(len(antenna_coords) - 1):
            antenna1_r, antenna1_c = antenna_coords[i]
            for j in range(i + 1, len(antenna_coords)):
                antenna2_r, antenna2_c = antenna_coords[j]

                # Calculate the distance between the antennas
                dr, dc = antenna2_r - antenna1_r, antenna2_c - antenna1_c

                # Calculate the positions of the antinodes so they align with the antennas
                first_new_r, first_new_c = antenna1_r - dr, antenna1_c - dc
                second_new_r, second_new_c = antenna2_r + dr, antenna2_c + dc

                # Ensure the antinodes coordinates are within the bounds of the map
                if (0 <= first_new_r < height) and (0 <= first_new_c < width):
                    antinodes_coords.add((first_new_r, first_new_c))
                if (0 <= second_new_r < height) and (0 <= second_new_c < width):
                    antinodes_coords.add((second_new_r, second_new_c))

    return len(antinodes_coords)


def part2(antennas_map: Tuple[Tuple[int, int], Dict[str, List[Tuple[int, int]]]]) -> int:
    """
    Solve part 2.
    @param antennas_map: Tuple of the antennas map dimensions and a dictionary containing the antennas coordinates.
    @return: Number of unique locations within the bounds of the map that contain an antinode when taking the effects
             of resonant harmonics.
    """
    (width, height), antennas_coords = antennas_map

    # Store the antinodes coordinates in a set
    antinodes_coords = set()

    # Check each kind of antenna
    for antenna in antennas_coords:
        antenna_coords = antennas_coords[antenna]

        # Check all possible pairs of antennas
        for i in range(len(antenna_coords) - 1):
            antenna1_r, antenna1_c = antenna_coords[i]

            # Add the antinode that appears on the first antenna
            antinodes_coords.add((antenna1_r, antenna1_c))
            for j in range(i + 1, len(antenna_coords)):
                antenna2_r, antenna2_c = antenna_coords[j]

                # Add the antinode that appears on the second antenna
                antinodes_coords.add((antenna2_r, antenna2_c))

                # Calculate the distance between the antennas
                dr, dc = antenna2_r - antenna1_r, antenna2_c - antenna1_c

                # Calculate the positions of the antinodes so they align with the antennas
                first_new_r, first_new_c = antenna1_r - dr, antenna1_c - dc
                second_new_r, second_new_c = antenna2_r + dr, antenna2_c + dc

                # Ensure the antinodes coordinates are within the bounds of the map
                while (0 <= first_new_r < height) and (0 <= first_new_c < width):
                    antinodes_coords.add((first_new_r, first_new_c))
                    first_new_r, first_new_c = first_new_r - dr, first_new_c - dc
                while (0 <= second_new_r < height) and (0 <= second_new_c < width):
                    antinodes_coords.add((second_new_r, second_new_c))
                    second_new_r, second_new_c = second_new_r + dr, second_new_c + dc

    return len(antinodes_coords)


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
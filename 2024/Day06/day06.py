from typing import List


def parse_input(input_file: str) -> List[List[str]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: 2D list of the lab map.
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()
        lab_map = [list(line.strip()) for line in lines]

    return lab_map


def part1(lab_map: List[List[str]]) -> int:
    """
    Solve part 1.
    @param lab_map: 2D list of the lab map.
    @return: Number of positions the guard visited.
    """
    # Get the dimensions of the lab map
    nb_rows, nb_cols = len(lab_map), len(lab_map[0])

    # Directions: up, right, down, left (clockwise)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_id = 0  # Start facing up (index 0 in directions)

    # Find the initial position of '^'
    row, col = 0, 0
    for r in range(nb_rows):
        for c in range(nb_cols):
            if lab_map[r][c] == '^':
                row, col = r, c

    # Track the visited locations with a set of tuples
    visited = set()

    while (0 <= row < nb_rows) and (0 <= col < nb_cols):
        # Mark the current position as visited
        visited.add((row, col))

        # Update the position
        new_row = row + directions[direction_id][0]
        new_col = col + directions[direction_id][1]

        # Check if the new position is out of bounds
        if (0 <= new_row < nb_rows) and (0 <= new_col < nb_cols):
            if lab_map[new_row][new_col] == '#':
                # Turn 90 degrees to the right when facing an obstruction
                direction_id = (direction_id + 1) % 4
            else:
                row, col = new_row, new_col
        else:
            break

    return len(visited)


def part2(lab_map: List[List[str]]) -> int:
    """
    Solve part 2.
    @param lab_map: 2D list of the lab map.
    @return: Number of new obstruction positions that would get the guard stuck in a loop.
    """
    # Get the dimensions of the lab map
    nb_rows, nb_cols = len(lab_map), len(lab_map[0])

    # Directions: up, right, down, left (clockwise)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_id = 0  # Start facing up (index 0 in directions)

    # Find the initial position of '^'
    row, col = 0, 0
    for r in range(nb_rows):
        for c in range(nb_cols):
            if lab_map[r][c] == '^':
                row, col = r, c

    # Track the visited positions along with the corresponding direction
    visited = {(row, col, direction_id)}  # Set of visited positions with direction
    tried = set()  # Set to track the new obstruction positions we try

    # Set to store positions where new obstructions cause the guard to get stuck in a loop
    obstructions = set()

    # Main loop: move the guard until he leaves the lab
    while (0 <= row < nb_rows) and (0 <= col < nb_cols):

        # Mark the current position with the corresponding direction as visited
        visited.add((row, col, direction_id))

        # Calculate the new position based on the current direction
        new_row = row + directions[direction_id][0]
        new_col = col + directions[direction_id][1]

        # Check if the new position is out of bounds
        if not ((0 <= new_row < nb_rows) and (0 <= new_col < nb_cols)):
            break

        # If the new position is an obstruction, turn the guard 90 degrees to the right
        if lab_map[new_row][new_col] == '#':
            direction_id = (direction_id + 1) % 4

        else:
            # If we haven't tried this position before, add a new obstruction
            if lab_map[new_row][new_col] != '^' and (new_row, new_col) not in tried:
                lab_map[new_row][new_col] = '#'
                tried.add((new_row, new_col))

                # Simulate the guard's path with the new obstruction in place
                s_visited = set()  # Track visited positions in the simulation
                s_row, s_col = row, col
                s_direction_id = direction_id

                # Simulate the path with the new obstruction
                while (0 <= s_row < nb_rows) and (0 <= s_col < nb_cols):
                    # Mark the current position in the simulation as visited
                    s_visited.add((s_row, s_col, s_direction_id))

                    # Calculate the next position in the simulation
                    new_s_row = s_row + directions[s_direction_id][0]
                    new_s_col = s_col + directions[s_direction_id][1]

                    # Create a state tuple (row, col, direction) for the current simulation position
                    simulation_state = (new_s_row, new_s_col, s_direction_id)

                    # Check if the new position in the simulation is out of bounds
                    if (0 <= new_s_row < nb_rows) and (0 <= new_s_col < nb_cols):
                        if lab_map[new_s_row][new_s_col] == '#':
                            # Turn 90 degrees to the right when facing an obstruction in the simulation
                            s_direction_id = (s_direction_id + 1) % 4
                        elif (simulation_state not in visited) and (simulation_state not in s_visited):
                            # Continue moving if this position has not been visited in the simulation or the main path
                            s_row, s_col = new_s_row, new_s_col
                        else:
                            # If we revisit a position with the same direction, it's a loop
                            obstructions.add((new_row, new_col))
                            break
                    else:
                        break

                # After simulation, remove the newly added obstruction to revert the map
                lab_map[new_row][new_col] = '.'

            # Move to the new position in the main loop
            row, col = new_row, new_col

    # Return the number of obstructions that caused the guard to get stuck in a loop
    return len(obstructions)



def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
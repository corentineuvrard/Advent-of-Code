from __future__ import annotations
from typing import List


class Point:
    """
    Class to represent a point.
    ...

    Attributes
    ----------
    x: int
        x coordinate of the point.
    y: int
        y coordinate of the point.

    Methods
    -------
    get_segment_points(point: Point, check_diagonals: bool = False) -> List[Point]:
        Return all the points of the segment formed by the current point and the given point.
        If check_diagonals is False, it only looks for horizontal and vertical segments.
        Otherwise, it also checks diagonals.
    """
    def __init__(self, x: int, y: int):
        """
        Construct a point with its coordinates.
        @param x: x coordinate of the point.
        @param y: y coordinate of the point.
        """
        self.x = x
        self.y = y

    def __eq__(self, point: Point) -> bool:
        """
        Compare the current point with a given point.
        @param point: Point to be compared with the current point.
        @return: Return True if the points have the same coordinates, False otherwise.
        """
        return self.x == point.x and self.y == point.y if point else False

    def __hash__(self) -> int:
        """
        Make the current point hashable, allowing it to be used as a key for a dictionary.
        @return: Hash value of the point.
        """
        return hash(repr(self))

    def __repr__(self) -> str:
        """
        Representation of a point.
        @return: A string representation of a point.
        """
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def get_segment_points(self, point: Point, check_diagonals: bool = False) -> List[Point]:
        """
        Get the points of the segment formed by the current point and the given point.
        @param point: Endpoint of the segment, the current point being the second endpoint of the segment.
        @param check_diagonals: If False, it only checks horizontal and vertical segments. If True, it also checks
        diagonals.
        @return: Return a list of the points on the segment.
        """
        if self.y == point.y:  # Horizontal
            min_x, max_x = min(self.x, point.x), max(self.x, point.x)
            return [Point(x, self.y) for x in range(min_x, max_x + 1)]
        elif self.x == point.x:  # Vertical
            min_y, max_y = min(self.y, point.y), max(self.y, point.y)
            return [Point(self.x, y) for y in range(min_y, max_y + 1)]
        elif check_diagonals:  # Diagonal
            min_x, max_x = min(self.x, point.x), max(self.x, point.x)
            min_y, max_y = min(self.y, point.y), max(self.y, point.y)
            segment_points = [self, point]
            if self.x == min_x and self.y == min_y:  # Bottom left to top right
                x, y = min_x + 1, min_y + 1
                while x != max_x:
                    segment_points.append(Point(x, y))
                    x, y = x + 1, y + 1
            elif self.x == min_x and self.y == max_y:  # Top left to bottom right
                x, y = min_x + 1, max_y - 1
                while x != max_x:
                    segment_points.append(Point(x, y))
                    x, y = x + 1, y - 1
            elif self.x == max_x and self.y == max_y:  # Top right to bottom left
                x, y = max_x - 1, max_y - 1
                while x != min_x:
                    segment_points.append(Point(x, y))
                    x, y = x - 1, y - 1
            elif self.x == max_x and self.y == min_y:  # Bottom right to top left
                x, y = max_x - 1, min_y + 1
                while x != min_x:
                    segment_points.append(Point(x, y))
                    x, y = x - 1, y + 1
            return segment_points
        else:
            return []


def parse_input(input_file: str) -> List[List[Point]]:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return: List of endpoints representing vent segments.
    """
    with open(input_file, "r") as f:
        lines = f.readlines()
    points = []
    for line in lines:
        segment = []
        for coord_str in line.split():
            coord = coord_str.split(",")
            if len(coord) == 2:
                coord_x, coord_y = int(coord[0]), int(coord[1])
                segment.append(Point(coord_x, coord_y))
        points.append(segment)
    return points


def part1(coordinates: List[List[Point]]) -> int:
    """
    Solve part 1.
    @param coordinates: List of endpoints representing vent segments.
    @return: Number of dangerous areas.
    """
    dangerous_areas = 0
    vents_map = dict()
    for coord in coordinates:
        start, end = coord[0], coord[1]
        vent_points = start.get_segment_points(end)
        for point in vent_points:
            vents_map[point] = vents_map[point] + 1 if point in vents_map else 1
            if vents_map[point] == 2:
                dangerous_areas += 1
    return dangerous_areas


def part2(coordinates: List[List[Point]]) -> int:
    """
    Solve part 2.
    @param coordinates: List of endpoints representing vent segments.
    @return: Number of dangerous areas.
    """
    dangerous_areas = 0
    vents_map = dict()
    for coord in coordinates:
        start, end = coord[0], coord[1]
        vent_points = start.get_segment_points(end, True)
        for point in vent_points:
            vents_map[point] = vents_map[point] + 1 if point in vents_map else 1
            if vents_map[point] == 2:
                dangerous_areas += 1
    return dangerous_areas


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input("input.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()

from typing import Text
from typing import List
from typing import Dict
from typing import Generator
from dataclasses import dataclass


def read_input_file(path: Text) -> Generator:
    with open(path, 'r') as input_file:
        for line in input_file:
            yield line.strip()


@dataclass
class Point:
    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Line:
    p1: Point
    p2: Point

    def is_horizontal(self) -> bool:
        return self.p1.x == self.p2.x

    def is_vertical(self) -> bool:
        return self.p1.y == self.p2.y

    def get_all_points(self) -> List[Point]:
        p1, p2 = self.p1, self.p2
        if not (self.is_vertical() or self.is_horizontal()):
            return self._get_points_of_diagonal(p1, p2)
        else:
            return self._get_points_of_horizontal_or_vertical(p1, p2)

    @staticmethod
    def _get_points_of_horizontal_or_vertical(p1, p2):
        points = []
        x_step = 1
        if p2.x < p1.x:
            x_step = -1

        y_step = 1
        if p2.y < p1.y:
            y_step = -1

        for x in range(p1.x, p2.x + x_step, x_step):
            for y in range(p1.y, p2.y + y_step, y_step):
                points.append(Point(x, y))
        return points

    @staticmethod
    def _get_points_of_diagonal(p1: Point, p2: Point) -> List[Point]:
        xs, ys = [], []

        step = 1
        if p2.x < p1.x:
            step = -1

        for x in range(p1.x, p2.x + step, step):
            xs.append(x)

        step = 1
        if p2.y < p1.y:
            step = -1

        for y in range(p1.y, p2.y + step, step):
            ys.append(y)

        points = [Point(x, y) for x, y in zip(xs, ys)]
        return points


def main():
    point_counts: Dict[Point, int] = {}
    for line in read_input_file("test_input.txt"):
        x1, y1, x2, y2 = [
            int(coord) for point in [point.split(',')
            for point in line.split(' -> ')] for coord in point
        ]
        line = Line(p1=Point(x1, y1), p2=Point(x2, y2))
        if not (line.is_vertical() or line.is_horizontal()):
            continue

        for point in line.get_all_points():
            if point not in point_counts:
                point_counts[point] = 1
            else:
                point_counts[point] += 1

    intersections = 0
    for key, value in point_counts.items():
        if value > 1:
            intersections += 1
    draw_map(point_counts)

    print(intersections)


def main_part_two():
    scores = get_point_scores()
    draw_map(scores)


def get_point_scores() -> Dict[Point, int]:
    point_counts: Dict[Point, int] = {}
    for line in read_input_file("input.txt"):
        x1, y1, x2, y2 = [
            int(coord) for point in [point.split(',')
            for point in line.split(' -> ')] for coord in point
        ]
        line = Line(p1=Point(x1, y1), p2=Point(x2, y2))

        for point in line.get_all_points():
            if point not in point_counts:
                point_counts[point] = 1
            else:
                point_counts[point] += 1

    intersections = 0
    for key, value in point_counts.items():
        if value > 1:
            intersections += 1

    print(intersections)
    return point_counts


def draw_map(point_scores: Dict[Point, int]) -> None:
    our_map = [['.' for _ in range(10)] for _ in range(10)]
    for point, value in point_scores.items():
        our_map[point.y][point.x] = str(value)
    
    for line in our_map:
        print(line)
        print()


if __name__ == "__main__":
    # main()
    main_part_two()

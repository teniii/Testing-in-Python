import itertools

from typing import List, Tuple

from limits import ANIMALS_MIN, ANIMALS_MAX, ZOOS_MIN, ZOOS_MAX, COORD_MIN, COORD_MAX


class OutOfBoundsException(Exception):
    """The provided number of elements is out of the accepted bounds"""


class WrongZooOrientationException(Exception):
    """The provided zoo cordinates don't start from the correct corner"""


class Animal:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def is_inside_fence(self, fence_start_x: int, fence_start_y: int, fence_end_x: int, fence_end_y: int):
        if fence_start_x > fence_end_x or fence_start_y > fence_end_y:
            raise WrongZooOrientationException(
                "Zoo coordinates start from bottom-left corner!")

        if fence_start_x > self.x or fence_end_x < self.x:
            return False
        elif fence_start_y > self.y or fence_end_y < self.y:
            return False
        return True


class Zoo:
    def __init__(self, x_start: int, y_start: int, x_end: int, y_end: int, animals: List[Animal]):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.animals = animals

    def count_inside_animals(self) -> int:
        return len([a for a in self.animals if a.is_inside_fence(self.x_start, self.y_start, self.x_end, self.y_end)])


def read_from_file():
    with open('intrare.txt', 'r') as file:
        lines = [l.strip() for l in file.readlines()]

    no_animals = int(lines[0])
    animal_coordinates = [(int(elem.split()[0]), int(elem.split()[1]))
                          for elem in lines[1:no_animals+1]]

    no_zoos = int(lines[no_animals+1])
    zoos_coordinates = [(int(elem.split()[0]), int(elem.split()[1]), int(elem.split()[2]), int(elem.split()[3]))
                        for elem in lines[no_animals+2:]]

    return no_animals, animal_coordinates, no_zoos, zoos_coordinates


def is_in_range(x: int, min_value: int, max_value: int) -> bool:
    return min_value <= x <= max_value


def solve_problem(no_animals: int, animals_coords: List[Tuple], no_zoos: int, zoos_coords: List[Tuple]) -> List[int]:
    # print(no_animals, animals_coords, no_zoos, zoos_coords)
    if no_animals == None or animals_coords == None or no_zoos == None or zoos_coords == None:
        raise OutOfBoundsException("Missing arguments!")

    if not is_in_range(no_animals, ANIMALS_MIN, ANIMALS_MAX):
        raise OutOfBoundsException("Number of animals not accepted!")

    if not is_in_range(no_zoos, ZOOS_MIN, ZOOS_MAX):
        raise OutOfBoundsException("Number of zoos not accepted!")

    all_coords = list(itertools.chain(*(animals_coords+zoos_coords)))
    for c in all_coords:
        if not is_in_range(c, COORD_MIN, COORD_MAX):
            raise Exception("Coordinate not accepted!")

    animals = [Animal(ac_x, ac_y) for ac_x, ac_y in animals_coords]
    animals_inside_list = [zoo.count_inside_animals()
                           for zoo in [Zoo(zc_x1, zc_y1, zc_x2, zc_y2, animals)
                                       for zc_x1, zc_y1, zc_x2, zc_y2 in zoos_coords]]

    return animals_inside_list


def main():
    no_animals, animals_coords, no_zoos, zoos_coords = read_from_file()

    print(solve_problem(no_animals, animals_coords, no_zoos, zoos_coords))


if __name__ == '__main__':
    main()

from typing import List


class Animal:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def is_inside_fence(self, fence_start_x: int, fence_start_y: int, fence_end_x: int, fence_end_y: int):
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


def main():
    _, animals_coords, _, zoos_coords = read_from_file()

    animals = [Animal(ac_x, ac_y) for ac_x, ac_y in animals_coords]
    animals_inside_list = [zoo.count_inside_animals()
                           for zoo in [Zoo(zc_x1, zc_y1, zc_x2, zc_y2, animals)
                                       for zc_x1, zc_y1, zc_x2, zc_y2 in zoos_coords]]

    print(animals_inside_list)


if __name__ == "__main__":
    main()

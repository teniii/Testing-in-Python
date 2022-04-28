# "Lasati-l"

from problem import solve_problem


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
    no_animals, animals_coords, no_zoos, zoos_coords = read_from_file()

    print(solve_problem(no_animals, animals_coords, no_zoos, zoos_coords))


if __name__ == '__main__':
    main()

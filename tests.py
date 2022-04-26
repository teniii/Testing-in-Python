import unittest

from problem import (
    Zoo, Animal,
    solve_problem,
    OutOfBoundsException, WrongZooOrientationException
)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertNotEqual(True, False)

    def test_init_animal(self):
        animal = Animal(3, 5)
        self.assertEqual(animal.x, 3)
        self.assertEqual(animal.y, 5)

    def test_init_zoo(self):
        zoo = Zoo(0, 0, 100, 100, [])
        self.assertEqual(zoo.x_start, 0)
        self.assertEqual(zoo.y_start, 0)
        self.assertEqual(zoo.x_end, 100)
        self.assertEqual(zoo.y_end, 100)

    def test_animals_inside(self):
        animal = Animal(100, 5)
        self.assertEqual(
            animal.is_inside_fence(
                fence_start_x=0,
                fence_end_x=1000,
                fence_start_y=0,
                fence_end_y=1000), True)

    # TODO for tests above: check if still needed
    ###############################################################################

    # Equivalence partitioning
    #
    # We've divided the problem into multiple classes, as follows:
    #   1 <= number of animals <= 5
    #   1 <= number of zoos <= 3
    #   -2000000000 <= any animal/zoo coord <= 2000000000
    #   x1 < x2 and y1 < y2 for zoos (they must start from the bottom left corner)

    def test_valid_problem(self):
        self.assertEqual(
            solve_problem(
                no_animals=5,
                animals_coords=[(0, 0), (1, 0), (2, 0), (0, 1), (1, 1)],
                no_zoos=3,
                zoos_coords=[(0, 0, 1000, 1000),
                             (-1000, -1000, 0, 0), (1, 0, 2, 2)]
            ), [5, 1, 3])

    def test_too_many_animals(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=234872478,
                animals_coords=[],
                no_zoos=2,
                zoos_coords=[]
            )

    def test_too_few_animals(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=0,
                animals_coords=[],
                no_zoos=2,
                zoos_coords=[]
            )

    def test_too_many_zoos(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=10,
                animals_coords=[],
                no_zoos=34587346758,
                zoos_coords=[]
            )

    def test_too_few_zoos(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=10,
                animals_coords=[],
                no_zoos=0,
                zoos_coords=[]
            )

    def test_coord_too_high(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=10,
                animals_coords=[(348765734324, 10), (1, 2)],
                no_zoos=5,
                zoos_coords=[(1, 2, 3, 4),  (1, 0, 2, 2)]
            )

    def test_coord_too_small(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=10,
                animals_coords=[(1, 14), (7, 2)],
                no_zoos=5,
                zoos_coords=[(-23784523786, 10, 4, 20), (1, 2, 3, 4)]
            )

    def test_wrong_zoo_orientation(self):
        with self.assertRaises(WrongZooOrientationException):
            solve_problem(
                no_animals=2,
                animals_coords=[(1, 14), (7, 2)],
                no_zoos=2,
                zoos_coords=[(-4, 10, 1, 2), (1, 2, 3, 4)]
            )

    ###############################################################################

    # Boundary value analysis
    #
    # We need to check the possible boundary values, as follows:
    #   animals: 0, 1, 5, 6
    #   zoos: 0, 1, 3, 4
    #   coords: -2000000001, -2000000000, 2000000000, 2000000001
    #   x1 > x2 and y1 > y2 for zoos

    def test_fail_animal_lower_boundary(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=0,
                animals_coords=[],
                no_zoos=2,
                zoos_coords=[]
            )

    def test_success_animal_lower_boundary(self):
        self.assertEqual(
            solve_problem(
                no_animals=1,
                animals_coords=[(500, 500)],
                no_zoos=2,
                zoos_coords=[(0, 0, 1000, 1000), (-1000, 0, -1000, 0)]
            ), [1, 0])

    def test_fail_animal_upper_boundary(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=6,
                animals_coords=[],
                no_zoos=2,
                zoos_coords=[]
            )

    def test_success_animal_upper_boundary(self):
        self.assertEqual(
            solve_problem(
                no_animals=5,
                animals_coords=[(0, 0), (1, 0), (2, 0), (0, 1), (1, 1)],
                no_zoos=1,
                zoos_coords=[(0, 0, 1000, 1000), (0, 0, 1, 1)]
            ), [5, 4])

    def test_fail_zoo_lower_boundary(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=1,
                animals_coords=[],
                no_zoos=0,
                zoos_coords=[]
            )

    def test_success_zoo_lower_boundary(self):
        self.assertEqual(
            solve_problem(
                no_animals=1,
                animals_coords=[(500, 500)],
                no_zoos=1,
                zoos_coords=[(0, 0, 1000, 1000)]
            ), [1])

    def test_fail_zoo_upper_boundary(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=2,
                animals_coords=[],
                no_zoos=4,
                zoos_coords=[]
            )

    def test_success_zoo_upper_boundary(self):
        self.assertEqual(
            solve_problem(
                no_animals=5,
                animals_coords=[(0, 0), (1, 0), (2, 0), (0, 1), (1, 1)],
                no_zoos=3,
                zoos_coords=[(0, 0, 1000, 1000), (0, 0, 1, 1), (0, 0, 1, 1)]
            ), [5, 4, 4])

    def test_fail_coords_lower_boundary(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=1,
                animals_coords=[(-2000000001, 15)],
                no_zoos=0,
                zoos_coords=[]
            )

    def test_success_coords_lower_boundary(self):
        self.assertEqual(
            solve_problem(
                no_animals=1,
                animals_coords=[(-2000000000, 15)],
                no_zoos=1,
                zoos_coords=[(-2000000000, 15, 0, 20)]
            ), [1])

    def test_fail_coords_upper_boundary(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=2,
                animals_coords=[(2000000001, 15)],
                no_zoos=4,
                zoos_coords=[]
            )

    def test_success_coords_upper_boundary(self):
        self.assertEqual(
            solve_problem(
                no_animals=5,
                animals_coords=[(2000000000, 15)],
                no_zoos=3,
                zoos_coords=[(0, 0, 2000000000, 17), (0, 0, 1, 1)]
            ), [1, 0])

    def test_fail_zoo_fence_x_axis_boundary(self):
        with self.assertRaises(WrongZooOrientationException):
            solve_problem(
                no_animals=1,
                animals_coords=[(1, 2)],
                no_zoos=2,
                zoos_coords=[(1, 2, 3, 4), (1, 2, 0, 4)]
            )

    def test_fail_zoo_fence_y_axis_boundary(self):
        with self.assertRaises(WrongZooOrientationException):
            solve_problem(
                no_animals=1,
                animals_coords=[(1, 2)],
                no_zoos=2,
                zoos_coords=[(1, 2, 3, 4), (1, 2, 3, 1)]
            )

    ###############################################################################

    # TODO
    # Category partitioning


if __name__ == '__main__':
    unittest.main()

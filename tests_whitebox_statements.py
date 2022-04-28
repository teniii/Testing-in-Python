import unittest

from problem import (
    solve_problem,
    OutOfBoundsException, WrongZooOrientationException
)


class MyTestCase(unittest.TestCase):
    def test_valid_problem(self):
        self.assertEqual(
            solve_problem(
                no_animals=4,
                animals_coords=[(0, 2), (2, 2), (4, 5), (6, 7)],
                no_zoos=2,
                zoos_coords=[(0, 0, 1000, 1000), (-1000, -1000, 0, 0)]
            ), [4, 0])

    def test_fail_bounds_animals(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=7,
                animals_coords=[(0, 0), (1, 0), (2, 0),
                                (0, 1), (1, 1), (0, 2), (0, 3)],
                no_zoos=2,
                zoos_coords=[(0, 0, 1000, 1000),
                             (-1000, -1000, 0, 0)]
            )

    def test_fail_bounds_zoos(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=3,
                animals_coords=[(0, 0), (1, 0), (2, 0)],
                no_zoos=342,
                zoos_coords=[(-20, -20, 0, 0)]
            )

    def test_wrong_zoo_orientation(self):
        with self.assertRaises(WrongZooOrientationException):
            solve_problem(
                no_animals=2,
                animals_coords=[(-2, 4), (12, 25)],
                no_zoos=2,
                zoos_coords=[(-4, 10, 1, 2), (11, 12, 13, 14)]
            )

    def test_fail_bounds_coords(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=2,
                animals_coords=[(2, 15), (14, 14)],
                no_zoos=2,
                zoos_coords=[(-7863735754, 10, 22, 245), (4, 5, 6, 7)]
            )

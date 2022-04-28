import unittest

from problem import (
    solve_problem,
    OutOfBoundsException, WrongZooOrientationException
)


class WhiteboxBranch(unittest.TestCase):
    def test_valid_values(self):
        self.assertEqual(
            solve_problem(
                no_animals=5,
                animals_coords=[(0, 0), (1, 0), (2, 0), (0, 1), (1, 1)],
                no_zoos=3,
                zoos_coords=[(0, 0, 1000, 1000),
                             (-1000, -1000, 0, 0), (1, 0, 2, 2)]
            ), [5, 1, 3])

    def test_number_of_animals_branch(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=6,
                animals_coords=[(0, 0), (1, 0), (2, 0),
                                (0, 1), (1, 1), (0, 2)],
                no_zoos=2,
                zoos_coords=[(0, 0, 1000, 1000),
                             (-1000, -1000, 0, 0)]
            )

    def test_number_of_zoos_branch(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=2,
                animals_coords=[(0, 0), (1, 0)],
                no_zoos=5,
                zoos_coords=[(0, 0, 1000, 1000),
                             (-1000, -1000, 0, 0),
                             (2000, 2000, 3000, 3000),
                             (-3000, -3000, 2000, 2000),
                             (-4000, -4000, 3000, 3000)]
            )

    def test_wrong_coord_height(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=2,
                animals_coords=[(11111111111111, 10), (1, 2)],
                no_zoos=2,
                zoos_coords=[(1, 2, 3, 4),  (1, 0, 2, 2)]
            )

    def test_zoo_orientation(self):
        with self.assertRaises(WrongZooOrientationException):
            solve_problem(
                no_animals=2,
                animals_coords=[(1, 14), (7, 2)],
                no_zoos=3,
                zoos_coords=[(-4, 10, 1, 2), (1, 2, 3, 4), (1, 2, 3, 4)]
            )

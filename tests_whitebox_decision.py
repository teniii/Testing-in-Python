import unittest

from problem import (
    Zoo, Animal,
    solve_problem,
    is_in_range,
    OutOfBoundsException, WrongZooOrientationException
)

from limits import COORD_MIN, COORD_MAX


class WhiteboxDecision(unittest.TestCase):
    # ===||||||===
    # Animal tests
    # ===||||||===

    def test_is_inside_fence_decision_1_true(self):
        animal = Animal(1, 1)
        with self.assertRaises(WrongZooOrientationException):
            animal.is_inside_fence(100, 100, 0, 0)

    def test_is_inside_fence_decision_2_true(self):
        animal = Animal(1, 1)
        self.assertFalse(animal.is_inside_fence(-100, -100, 0, 0))

    def test_is_inside_fence_decision_3_true(self):
        animal = Animal(1, 1)
        self.assertFalse(animal.is_inside_fence(0, -100, 100, 0))

    def test_is_inside_fence_decision_3_false(self):
        animal = Animal(-50, -50)

        self.assertTrue(animal.is_inside_fence(-100, -100, 0, 0))

    # ===||||||===
    # Zoo tests
    # ===||||||===

    def test_count_inside_animals_decision_false(self):
        animal = Animal(-10, -10)
        zoo = Zoo(0, 0, 100, 100, [animal])
        self.assertEqual(zoo.count_inside_animals(), 0)

    def test_count_inside_animals_decision_true(self):
        animal = Animal(10, 10)
        zoo = Zoo(0, 0, 100, 100, [animal])
        self.assertEqual(zoo.count_inside_animals(), 1)

    # ===||||||===
    # is_in_range tests
    # ===||||||===

    def test_is_in_range_decision_false(self):
        self.assertFalse(is_in_range(x=0, min_value=10, max_value=100))

    def test_is_in_range_decision_true(self):
        self.assertTrue(is_in_range(x=50, min_value=10, max_value=100))

    # ===||||||===
    # solve_problem tests
    # ===||||||===

    def test_solve_problem_decision_1_true(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(0, [], 0, [])

    def test_solve_problem_decision_2_true(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(0, [], 0, [])

    def test_solve_problem_decision_3_true(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(1, [(2 * COORD_MIN, 2 * COORD_MAX)], 0, [])

    def test_solve_problme_decision_3_false(self):
        animals_coords = [(1, 1), (30, 30), (80, 80)]
        zoo_coords = [(0, 0, 100, 100)]
        self.assertEqual(solve_problem(
            len(animals_coords),
            animals_coords,
            len(zoo_coords),
            zoo_coords
        ), [3])


if __name__ == '__main__':
    unittest.main()

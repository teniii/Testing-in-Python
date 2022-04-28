import unittest

from problem import (
    Zoo, Animal,
    solve_problem, is_in_range,
    OutOfBoundsException, WrongZooOrientationException
)

from limits import COORD_MAX, COORD_MIN


class WhiteboxStatement(unittest.TestCase):
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


class WhiteboxCondition(unittest.TestCase):
    def test_sp_if_is_in_range_animal_true(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(0, [], 0, [])

    def test_sp_if_is_in_range_zoo_true(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(2, [(0, 0), (1, 0)], 0, [])

    def test_sp_if_is_in_range_all_coords_true(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(1, [(7 * COORD_MIN, 7 * COORD_MAX)],
                          1, [(0, 0, 1000, 1000), (-1000, -1000, 0, 0)])

    def test_sp_if_is_in_range_all_coords_false(self):
        animals_coords = [(1, 1), (30, 30), (80, 80)]
        zoo_coords = [(0, 0, 100, 100)]
        self.assertEqual(solve_problem(
            len(animals_coords),
            animals_coords,
            len(zoo_coords),
            zoo_coords
        ), [3])

    # ===||||||===
    # min_value <= x
    # ===||||||===

    def test_if_is_in_range_min_false(self):
        self.assertFalse(is_in_range(10, 11, 20))

    def test_if_is_in_range_min_true(self):
        self.assertTrue(is_in_range(10, 0, 20))
    # ===||||||===
    # x <= max_value
    # ===||||||===

    def test_if_is_in_range_max_false(self):
        self.assertFalse(is_in_range(10, 0, 9))

    def test_if_is_in_range_max_true(self):
        self.assertTrue(is_in_range(10, 0, 10))

    def test_zoo_count_is_inside_fence_true(self):
        animal = Animal(10, 10)
        zoo = Zoo(0, 0, 100, 100, [animal])
        self.assertEqual(zoo.count_inside_animals(), 1)

    def test_zoo_count_is_inside_fence_false(self):
        animal = Animal(-10, -10)
        zoo = Zoo(0, 0, 100, 100, [animal])
        self.assertEqual(zoo.count_inside_animals(), 0)

    # ===||||||===
    # fence_start_x >= fence_end_x
    # ===||||||===

    def test_animal_is_inside_fence_x_true(self):
        animal = Animal(1, 1)
        with self.assertRaises(WrongZooOrientationException):
            animal.is_inside_fence(10, 0, 0, 10)

    def test_animal_is_inside_fence_x_false(self):
        animal = Animal(2, 2)
        self.assertFalse(animal.is_inside_fence(0, 0, 1, 1))

    # ===||||||===
    # fence_start_y >= fence_end_y
    # ===||||||===

    def test_animal_is_inside_fence_y_true(self):
        animal = Animal(1, 1)
        with self.assertRaises(WrongZooOrientationException):
            animal.is_inside_fence(0, 10, 10, 0)

    def test_animal_is_inside_fence_y_false(self):
        animal = Animal(2, 2)
        self.assertFalse(animal.is_inside_fence(0, 0, 1, 1))

    # ===||||||===
    # fence_start_x > self.x
    # ===||||||===

    def test_animal_is_inside_fence_start_x_true(self):
        animal = Animal(1, 1)
        self.assertFalse(animal.is_inside_fence(10, 0, 20, 10))

    def test_animal_is_inside_fence_start_x_false(self):
        animal = Animal(1, 1)
        self.assertTrue(animal.is_inside_fence(0, 0, 10, 10))

    # ===||||||===
    # fence_end_x < self.x
    # ===||||||===

    def test_animal_is_inside_fence_end_x_true(self):
        animal = Animal(1, 1)
        self.assertFalse(animal.is_inside_fence(-100, 0, 0, 10))

    def test_animal_is_inside_fence_end_x_false(self):
        animal = Animal(1, 1)
        self.assertTrue(animal.is_inside_fence(0, 0, 10, 10))

    # ===||||||===
    # fence_start_y > self.y
    # ===||||||===

    def test_animal_is_inside_fence_start_y_true(self):
        animal = Animal(1, 1)
        self.assertFalse(animal.is_inside_fence(0, 10, 10, 20))

    def test_animal_is_inside_fence_start_y_false(self):
        animal = Animal(1, 1)
        self.assertTrue(animal.is_inside_fence(0, 0, 10, 10))

    # ===||||||===
    # fence_end_y < self.y
    # ===||||||===

    def test_animal_is_inside_fence_end_y_true(self):
        animal = Animal(1, 1)
        self.assertFalse(animal.is_inside_fence(0, -100, 10, 0))

    def test_animal_is_inside_fence_end_y_false(self):
        animal = Animal(1, 1)
        self.assertTrue(animal.is_inside_fence(0, 0, 10, 10))


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

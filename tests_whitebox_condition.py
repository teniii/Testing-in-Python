import unittest

from problem import (
    Zoo, Animal,
    solve_problem,
    is_in_range,
    OutOfBoundsException, WrongZooOrientationException
)

from limits import COORD_MAX, COORD_MIN


class WhiteboxCondition(unittest.TestCase):

    def test_valid_problem(self):
        self.assertEqual(
            solve_problem(
                no_animals=5,
                animals_coords=[(0, 0), (1, 0), (2, 0), (0, 1), (1, 1)],
                no_zoos=3,
                zoos_coords=[(0, 0, 1000, 1000),
                             (-1000, -1000, 0, 0), (1, 0, 2, 2)]
            ), [5, 1, 3])

    def test_sp_if_is_in_range_animal_false(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(2, [(0, 0), (1, 0)], 0, [])

    def test_sp_if_is_in_range_animal_true(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(0, [], 0, [])

    def test_sp_if_is_in_range_zoo_true(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(2, [(0, 0), (1, 0)], 0, [])

    def test_sp_if_is_in_range_zoo_false(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(2, [(0, 0), (1, 0)], 6, [
                          (0, 0, 1000, 1000), (-1000, -1000, 0, 0)])

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


if __name__ == '__main__':
    unittest.main()

import unittest

from problem import Zoo, Animal, solve_problem, OutOfBoundsException


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

    def test_too_many_animals(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(387645332423, [], 2, [])


if __name__ == '__main__':
    unittest.main()

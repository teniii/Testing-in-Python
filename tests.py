import unittest

from problem import Zoo, Animal, solve_problem


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

    def test_wrong_zoo(self):
        # with self.assertRaises(solve_problem(100000000, [], 2, [])) as cm:
        #
        # the_exception = cm.exception
        # self.assertEqual(the_exception.error_code, 3)

        # self.assertEqual(Exception("Number of animals not accepted!"),
        #                  solve_problem(10000000, [], 2, []))
        self.assertRaises(
            Exception, lambda: solve_problem(10000000, [], 2))

    # def test_wrong_zoo(self):
    #     Zoo(100, 100, 0, 0, [])
    #     with self.assertRaises() as cm:

    def test_animals_inside(self):
        animal = Animal(100, 5)
        self.assertEqual(
            animal.is_inside_fence(
                fence_start_x=0,
                fence_end_x=1000,
                fence_start_y=0,
                fence_end_y=1000), True)


if __name__ == '__main__':
    unittest.main()

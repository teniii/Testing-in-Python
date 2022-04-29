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
                no_animals=7,
                animals_coords=[(0, 0), (1, 0), (2, 0),
                                (0, 1), (1, 1), (0, 2), (0, 3)],
                no_zoos=2,
                zoos_coords=[(0, 0, 1000, 1000),
                             (-1000, -1000, 0, 0)]
            )

    def test_too_few_animals(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=0,
                animals_coords=[],
                no_zoos=2,
                zoos_coords=[(0, 0, 1000, 1000),
                             (-1000, -1000, 0, 0)]
            )

    def test_too_many_zoos(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=2,
                animals_coords=[(0, 0), (1, 0)],
                no_zoos=5,
                zoos_coords=[(0, 0, 1000, 1000),
                             (-1000, -1000, 0, 0),
                             (2000, 2000, 3000, 3000),
                             (-3000, -3000, 2000, 2000),
                             (2000, 2000, 3000, 3000), ]
            )

    def test_too_few_zoos(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=2,
                animals_coords=[(0, 0), (1, 0)],
                no_zoos=-1,
                zoos_coords=[]
            )

    def test_coord_too_high(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=2,
                animals_coords=[(348765734324, 10), (1, 2)],
                no_zoos=2,
                zoos_coords=[(1, 2, 3, 4),  (1, 0, 2, 2)]
            )

    def test_coord_too_small(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=2,
                animals_coords=[(1, 14), (7, 2)],
                no_zoos=2,
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
    #   x1 = x2 and y1 = y2 and x1+1 = x2 and y1+1 = y2
    #
    # We will name success boundaries  as follow:
    # "1" means lower boundary and "2" means upper boundary
    #   animals = n
    #   zoos = z
    #   coords = c

    def test_fail_animal_lower_boundary(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=0,
                animals_coords=[],
                no_zoos=2,
                zoos_coords=[(0, 0, 1000, 1000),
                             (-1000, -1000, 0, 0)]
            )

    def test_fail_animal_upper_boundary(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=6,
                animals_coords=[(500, 500), (501, 500), (502, 500),
                                (503, 500), (504, 500), (505, 500)],
                no_zoos=2,
                zoos_coords=[(0, 0, 1000, 1000), (-1000, 0, -900, 0)]
            )

    def test_fail_zoo_lower_boundary(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=1,
                animals_coords=[(0, 0)],
                no_zoos=0,
                zoos_coords=[]
            )

    def test_fail_zoo_upper_boundary(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=2,
                animals_coords=[(500, 500), (501, 500)],
                no_zoos=4,
                zoos_coords=[(0, 0, 1000, 1000), (0, 0, 1000, 1000),
                             (0, 0, 1000, 1000), (0, 0, 1000, 1000)]
            )

    def test_fail_coords_lower_boundary(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=1,
                animals_coords=[(-2000000001, 15)],
                no_zoos=1,
                zoos_coords=[(0, 0, 1000, 1000)]
            )

    def test_fail_coords_upper_boundary(self):
        with self.assertRaises(OutOfBoundsException):
            solve_problem(
                no_animals=1,
                animals_coords=[(2000000001, 15)],
                no_zoos=2,
                zoos_coords=[(0, 0, 1000, 1000), (0, 0, 1000, 1000)]
            )

    def test_wrong_zoo_orientation_x_equals(self):
        with self.assertRaises(WrongZooOrientationException):
            solve_problem(
                no_animals=2,
                animals_coords=[(1, 14), (7, 2)],
                no_zoos=2,
                zoos_coords=[(-4, 10, -4, 20), (1, 2, 3, 4)]
            )

    def test_wrong_zoo_orientation_y_equals(self):
        with self.assertRaises(WrongZooOrientationException):
            solve_problem(
                no_animals=2,
                animals_coords=[(1, 14), (7, 2)],
                no_zoos=2,
                zoos_coords=[(-4, 10, 2, 10), (1, 2, 3, 4)]
            )

    def test_n1z1c1x(self):
        self.assertEqual(
            solve_problem(
                no_animals=1,
                animals_coords=[(-2000000000, 15)],
                no_zoos=1,
                zoos_coords=[(0, 0, 1, 17)]
            ), [0])

    def test_n1z1c1y(self):
        self.assertEqual(
            solve_problem(
                no_animals=1,
                animals_coords=[(-2000000000, 15)],
                no_zoos=1,
                zoos_coords=[(0, 0, 5, 1)]
            ), [0])

    def test_n1z1c2x(self):
        self.assertEqual(
            solve_problem(
                no_animals=1,
                animals_coords=[(2000000000, 15)],
                no_zoos=1,
                zoos_coords=[(0, 0, 1, 5)]
            ), [0])

    def test_n1z1c2y(self):
        self.assertEqual(
            solve_problem(
                no_animals=1,
                animals_coords=[(2000000000, 15)],
                no_zoos=1,
                zoos_coords=[(0, 0, 5, 1)]
            ), [0])

    def test_n1z2c1x(self):
        self.assertEqual(
            solve_problem(
                no_animals=1,
                animals_coords=[(-2000000000, 15)],
                no_zoos=3,
                zoos_coords=[(0, 0, 1, 500), (0, 0, 50, 500), (20, 0, 21, 500)]
            ), [0,0,0])

    def test_n1z2c1y(self):
        self.assertEqual(
            solve_problem(
                no_animals=1,
                animals_coords=[(-2000000000, 15)],
                no_zoos=3,
                zoos_coords=[(0, 499, 50, 500), (0, 0, 50, 500), (30, 100, 45, 101)]
            ), [0,0,0])

    def test_n1z2c2x(self):
        self.assertEqual(
            solve_problem(
                no_animals=1,
                animals_coords=[(2000000000, 15)],
                no_zoos=3,
                zoos_coords=[(0, 0, 1, 500), (0, 0, 50, 500), (20, 0, 21, 500)]
            ), [0,0,0])

    def test_n1z2c2y(self):
        self.assertEqual(
            solve_problem(
                no_animals=1,
                animals_coords=[(2000000000, 15)],
                no_zoos=3,
                zoos_coords=[(0, 10, 2000000000, 500), (0, 0, 50, 500), (30, 100, 45, 101)]
            ), [1,0,0])

    def test_n2z1c1x(self):
        self.assertEqual(
            solve_problem(
                no_animals=3,
                animals_coords=[(-2000000000, 15),(0, -2000000000),(-2000000000, -2000000000)],
                no_zoos=1,
                zoos_coords=[(0, 0, 1, 500)]
            ), [0])

    def test_n2z1c1y(self):
        self.assertEqual(
            solve_problem(
                no_animals=3,
                animals_coords=[(-2000000000, 15),(0, -2000000000),(-2000000000, -2000000000)],
                no_zoos=1,
                zoos_coords=[(0, 15, 50, 16)]
            ), [0])

    def test_n2z1c2x(self):
        self.assertEqual(
            solve_problem(
                no_animals=3,
                animals_coords=[(2000000000, 15),(0, 2000000000),(2000000000, 2000000000)],
                no_zoos=1,
                zoos_coords=[(0, 0, 1, 500)]
            ), [0])

    def test_n2z1c2y(self):
        self.assertEqual(
            solve_problem(
                no_animals=3,
                animals_coords=[(2000000000, 15),(0, 2000000000),(2000000000, 2000000000)],
                no_zoos=1,
                zoos_coords=[(0, 15, 2000000000, 16)]
            ), [1])

    def test_n2z2c1x(self):
        self.assertEqual(
            solve_problem(
                no_animals=3,
                animals_coords=[(-2000000000, 15),(0, -2000000000),(-2000000000, -2000000000)],
                no_zoos=3,
                zoos_coords=[(0, 10, 1, 500), (0, 0, 50, 500), (30, 100, 45, 200)]
            ), [0,0,0])

    def test_n2z2c1y(self):
        self.assertEqual(
            solve_problem(
                no_animals=3,
                animals_coords=[(-2000000000, 15),(0, -2000000000),(-2000000000, -2000000000)],
                no_zoos=3,
                zoos_coords=[(0, 10, 50, 500), (0, 0, 50, 500), (30, 100, 45, 101)]
            ), [0,0,0])

    def test_n2z2c2x(self):
        self.assertEqual(
            solve_problem(
                no_animals=3,
                animals_coords=[(2000000000, 15),(0, 2000000000),(2000000000, 2000000000)],
                no_zoos=3,
                zoos_coords=[(0, 10, 1, 500), (0, 0, 50, 500), (30, 100, 45, 200)]
            ), [0,0,0])

    def test_n2z2c2y(self):
        self.assertEqual(
            solve_problem(
                no_animals=3,
                animals_coords=[(2000000000, 15),(0, 2000000000),(2000000000, 2000000000)],
                no_zoos=3,
                zoos_coords=[(0, 10, 10, 500), (0, 0, 50, 500), (30, 100, 45, 101)]
            ), [0,0,0])



###############################################################################
# Category partitioning
#
# Divided categories
#   no_animals (n):
#       1) n < 0
#       2) n = 0
#       3) n = 1
#       4) n = 2..4
#       5) n = 5
#       6) n = 6
#       7) n > 6
#
#   zoos (z):
#       1) z < 0
#       2) z = 0
#       3) z = 1
#       4) z = 2
#       5) z = 3
#       6) z = 4
#       7) z > 4
#
#   coords (c): (Facem pentru fiecare obiect animal/zoo sau la modul general?)
#       1) c < -2000000001
#       2) c = -2000000001
#       3) c = -2000000000
#       4) c = -1999999999....1999999999
#       5) c = 2000000000
#       6) c = 2000000001
#       7) c > 2000000001
#
#   respect_coords_order (r):
#       1) x1 > x2 && y1 > y2
#       2) x1 > x2 && y1 = y2
#       3) x1 > x2 && y1 < y2
#       4) x1 = x2 && y1 > y2
#       5) x1 = x2 && y1 = y2
#       6) x1 = x2 && y1 < y2
#       7) x1 < x2 && y1 > y2
#       8) x1 < x2 && y1 = y2
#       9) x1 < x2 && y1 < y2
#
#   output (o):
#       1) List
#
# Cases (by removing the sensless ones)
#
#   n1 n2 n6 n7
#   z1 z2 z6 z7
#   c1 c2 c6 c7
#   r1 r2 r3 r4 r5 r6 r7 r8
#
#   n3z3c3r9o1 n3z3c4r9o1 n3z3c5r9o1 n3z4c3r9o1 n3z4c4r9o1 n3z4c5r9o1 n3z5c3r9o1 n3z5c4r9o1 n3z5c5r9o1
#   n4z3c3r9o1 n4z3c4r9o1 n4z3c5r9o1 n4z4c3r9o1 n4z4c4r9o1 n4z4c5r9o1 n4z5c3r9o1 n4z5c4r9o1 n4z5c5r9o1
#   n5z3c3r9o1 n5z3c4r9o1 n5z3c5r9o1 n5z4c3r9o1 n5z4c4r9o1 n5z4c5r9o1 n5z5c3r9o1 n5z5c4r9o1 n5z5c5r9o1
#
# By removing the ones we did in the previosly methods:
#
#   n3z3c4r9o1 n3z4c3r9o1 n3z4c4r9o1 n3z4c5r9o1 n3z5c4r9o1
#   n4z3c3r9o1 n4z3c4r9o1 n4z3c5r9o1 n4z4c3r9o1 n4z4c4r9o1 n4z4c5r9o1 n4z5c3r9o1 n4z5c4r9o1 n4z5c5r9o1
#   n5z3c4r9o1 n5z4c3r9o1 n5z4c4r9o1 n5z4c5r9o1 n5z5c4r9o1
#
    def test_success_n3z3c4(self):
        self.assertEqual(
            solve_problem(
                no_animals=1,
                animals_coords=[(190, 15)],
                no_zoos=1,
                zoos_coords=[(0, 0, 500, 17)]
            ), [1])

    def test_success_n3z4c3(self):
        self.assertEqual(
            solve_problem(
                no_animals=1,
                animals_coords=[(-2000000000, 15)],
                no_zoos=2,
                zoos_coords=[(0, 0, 500, 17), (-2000000000, 0, 500, 17)]
            ), [0, 1])

    def test_success_n3z4c4(self):
        self.assertEqual(
            solve_problem(
                no_animals=1,
                animals_coords=[(190, 15)],
                no_zoos=2,
                zoos_coords=[(0, 0, 500, 17), (190, 0, 500, 17)]
            ), [1, 1])

    def test_success_n3z4c5(self):
        self.assertEqual(
            solve_problem(
                no_animals=1,
                animals_coords=[(2000000000, 15)],
                no_zoos=2,
                zoos_coords=[(0, 0, 500, 17), (0, 0, 2000000000, 17)]
            ), [0, 1])

    def test_success_n3z5c4(self):
        self.assertEqual(
            solve_problem(
                no_animals=1,
                animals_coords=[(-650, 15)],
                no_zoos=2,
                zoos_coords=[(0, 0, 500, 17), (-650, 0, 0, 17)]
            ), [0, 1])

    def test_success_n4z3c3(self):
        self.assertEqual(
            solve_problem(
                no_animals=2,
                animals_coords=[(0, 15), (5, 25)],
                no_zoos=1,
                zoos_coords=[(-2000000000, 0, 500, 17)]
            ), [1])

    def test_success_n4z3c4(self):
        self.assertEqual(
            solve_problem(
                no_animals=2,
                animals_coords=[(0, 15), (5, 25)],
                no_zoos=1,
                zoos_coords=[(10, 0, 500, 17)]
            ), [0])

    def test_success_n4z3c5(self):
        self.assertEqual(
            solve_problem(
                no_animals=2,
                animals_coords=[(0, 15), (5, 25)],
                no_zoos=1,
                zoos_coords=[(0, 0, 2000000000, 2000000000)]
            ), [2])

    def test_success_n4z4c3(self):
        self.assertEqual(
            solve_problem(
                no_animals=2,
                animals_coords=[(0, 15), (5, 25)],
                no_zoos=2,
                zoos_coords=[(-2000000000, -2000000000, 15, 0),
                             (-2000000000, 0, 10, 60)]
            ), [0, 2])

    def test_success_n4z4c4(self):
        self.assertEqual(
            solve_problem(
                no_animals=2,
                animals_coords=[(0, 15), (5, 25)],
                no_zoos=2,
                zoos_coords=[(-50, -20, 15, 0), (-20, 0, 10, 60)]
            ), [0, 2])

    def test_success_n4z4c5(self):
        self.assertEqual(
            solve_problem(
                no_animals=2,
                animals_coords=[(0, 15), (5, 25)],
                no_zoos=2,
                zoos_coords=[(-50, -20, 2000000000, 2000000000),
                             (-20, 0, 10, 2000000000)]
            ), [2, 2])

    def test_success_n4z5c3(self):
        self.assertEqual(
            solve_problem(
                no_animals=2,
                animals_coords=[(-2000000000, 15), (5, 25)],
                no_zoos=3,
                zoos_coords=[(-2000000000, -2000000000, 0, 0),
                             (-2000000000, 0, 0, 500), (-50, -2000000000, 20, 700)]
            ), [0, 1, 1])

    def test_success_n4z5c4(self):
        self.assertEqual(
            solve_problem(
                no_animals=2,
                animals_coords=[(0, 15), (5, 25)],
                no_zoos=3,
                zoos_coords=[(-60, -60, 0, 0), (-800, 0, 0, 500),
                             (-50, -70, 20, 700)]
            ), [0, 1, 2])

    def test_success_n4z5c5(self):
        self.assertEqual(
            solve_problem(
                no_animals=2,
                animals_coords=[(0, 2000000000), (2000000000, 25)],
                no_zoos=3,
                zoos_coords=[(-50, -20, 2000000000, 2000000000),
                             (-20, 0, 10, 2000000000), (-20, 0, 2000000000, 10)]
            ), [2, 1, 0])

    def test_success_n5z3c4(self):
        self.assertEqual(
            solve_problem(
                no_animals=5,
                animals_coords=[(0, 20), (5, 25), (2, 15), (15, 55), (0, 40)],
                no_zoos=1,
                zoos_coords=[(-20, 0, 0, 20)]
            ), [1])

    def test_success_n5z4c3(self):
        self.assertEqual(
            solve_problem(
                no_animals=5,
                animals_coords=[(-2000000000, 20),
                                (5, -2000000000), (2, 15), (15, 55), (0, 40)],
                no_zoos=2,
                zoos_coords=[(-2000000000, 0, 0, 50),
                             (-50, -2000000000, 0, 50)]
            ), [2, 1])

    def test_success_n5z4c4(self):
        self.assertEqual(
            solve_problem(
                no_animals=5,
                animals_coords=[(190, 20),
                                (5, -190), (2, 15), (15, 55), (0, 40)],
                no_zoos=2,
                zoos_coords=[(0, 0, 190, 50),
                             (-50, -500, 0, 50)]
            ), [3, 1])

    def test_success_n5z4c5(self):
        self.assertEqual(
            solve_problem(
                no_animals=5,
                animals_coords=[(20, 2000000000), (2000000000,
                                                   40), (2, 15), (15, 55), (0, 40)],
                no_zoos=2,
                zoos_coords=[(-20, 0, 2000000000, 50),
                             (-50, 30, 0, 2000000000)]
            ), [3, 1])

    def test_success_n5z5c4(self):
        self.assertEqual(
            solve_problem(
                no_animals=5,
                animals_coords=[(20, 170), (170, 40), (2, 15), (15, 55), (0, 40)],
                no_zoos=3,
                zoos_coords=[(-20, 0, 170, 50),
                             (-50, 30, 0, 40),(-20, 0, 40, 50)]
            ), [3, 1, 2])


if __name__ == '__main__':
    unittest.main()

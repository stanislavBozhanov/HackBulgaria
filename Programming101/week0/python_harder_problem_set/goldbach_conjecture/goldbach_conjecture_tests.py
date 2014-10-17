import unittest
from goldbach_conjecture import goldbach


class GoldbachConjectureTests(unittest.TestCase):

    def test_if_input_is_less_than_four(self):
        self.assertRaises(ValueError, goldbach, (2))
        self.assertRaises(ValueError, goldbach, (1))
        self.assertRaises(ValueError, goldbach, (0))
        self.assertRaises(ValueError, goldbach, (-1))

    def test_if_number_is_even(self):
        self.assertRaises(ValueError, goldbach, (7))

    def test_for_with_correct_input(self):
        self.assertEqual([(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)], goldbach(100))
        self.assertEquals([(2, 2)], goldbach(4))
        self.assertEqual([(3, 3)], goldbach(6))
        self.assertEqual([(3, 5)], goldbach(8))
        self.assertEqual([(3, 7), (5, 5)], goldbach(10))

if __name__ == '__main__':
    unittest.main()

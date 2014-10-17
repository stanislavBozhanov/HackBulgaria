import unittest
from fibonacci_lists import nth_fib_lists


class FibonacciListsTests(unittest.TestCase):

    def test_zero_list_choice(self):
        self.assertEqual([], nth_fib_lists([1], [2], 0))

    def test_first_fibonacci_list(self):
        self.assertEqual([1], nth_fib_lists([1], [2], 1))

    def test_second_fibonacci_list(self):
        self.assertEqual([2], nth_fib_lists([1], [2], 2))

    def test_for_bigger_fibonacci_lists(self):
        self.assertEqual([1, 2, 1, 3], nth_fib_lists([1, 2], [1, 3], 3))
        self.assertEqual([1, 2, 3, 1, 2, 3], nth_fib_lists([], [1, 2, 3], 4))
        self.assertEqual([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3], nth_fib_lists([], [1, 2, 3], 6))
        self.assertEqual([], nth_fib_lists([], [], 100))


if __name__ == '__main__':
    unittest.main()

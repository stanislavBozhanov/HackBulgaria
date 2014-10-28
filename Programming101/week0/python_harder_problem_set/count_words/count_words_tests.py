import unittest
from count_words import count_words


class TestCountWords(unittest.TestCase):

    def test_output(self):
        self.assertEqual(count_words(["apple", "banana", "apple", "pie"]), {'apple': 2, 'pie': 1, 'banana': 1})
        self.assertEqual(count_words(["python", "python", "python", "ruby"]), {'ruby': 1, 'python': 3})
        self.assertEqual(count_words([]), {})

if __name__ == '__main__':
    unittest.main()

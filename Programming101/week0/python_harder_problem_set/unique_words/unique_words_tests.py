import unittest
from unique_words import unique_words_count


class UniqueWordsTests(unittest.TestCase):
    def test_for_correct_output(self):
        self.assertEqual(3, unique_words_count(["apple", "banana", "apple", "pie"]))
        self.assertEqual(2, unique_words_count(["python", "python", "python", "ruby"]))
        self.assertEqual(1, unique_words_count(["HELLO!"] * 10))
        self.assertEqual(0, unique_words_count([] * 100))
        self.assertEqual(2, unique_words_count(["Hi", "hi"]))

if __name__ == '__main__':
    unittest.main()

import unittest
from sudoku_solved import sudoku_solved


class SudokuSolvedTests(unittest.TestCase):
    def test_(self):
        self.assertFalse(sudoku_solved([
                         [4, 2, 1, 7, 9, 8, 6, 5, 3],
                         [6, 7, 3, 5, 2, 1, 4, 8, 9],
                         [9, 5, 8, 3, 6, 4, 2, 1, 7],
                         [1, 8, 2, 9, 5, 7, 3, 6, 4],
                         [3, 4, 9, 8, 4, 6, 1, 7, 5],
                         [5, 6, 7, 1, 3, 2, 9, 2, 8],
                         [2, 3, 6, 4, 8, 5, 7, 9, 1],
                         [7, 9, 5, 6, 1, 3, 8, 4, 2],
                         [8, 1, 4, 2, 7, 9, 5, 3, 6]]))
        self.assertTrue(sudoku_solved([
                        [4, 5, 2, 3, 8, 9, 7, 1, 6],
                        [3, 8, 7, 4, 6, 1, 2, 9, 5],
                        [6, 1, 9, 2, 5, 7, 3, 4, 8],
                        [9, 3, 5, 1, 2, 6, 8, 7, 4],
                        [7, 6, 4, 9, 3, 8, 5, 2, 1],
                        [1, 2, 8, 5, 7, 4, 6, 3, 9],
                        [5, 7, 1, 8, 9, 2, 4, 6, 3],
                        [8, 9, 6, 7, 4, 3, 1, 5, 2],
                        [2, 4, 3, 6, 1, 5, 9, 8, 7]]))

if __name__ == '__main__':
    unittest.main()

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

if __name__ == '__main__':
    unittest.main()

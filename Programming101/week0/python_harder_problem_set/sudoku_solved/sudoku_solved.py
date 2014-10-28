def row_sum_ok(matrix):
    SUDOKU_SUM = 45
    correct = True
    for row in matrix:
        if sum(row) != SUDOKU_SUM or len(row) != len(set(row)):
            correct = False
            break
    return correct


def col_sum_ok(matrix):
    SUDOKU_SUM = 45
    correct = True
    transpose_matrix = zip(*matrix)
    for row in transpose_matrix:
        if sum(row) != SUDOKU_SUM or len(row) != len(set(row)):
            correct = False
            break
    return correct


def box_sum_ok(matrix):
    SUDOKU_SUM = 45
    boxedsud = []
    correct = True
    for li, line in enumerate(matrix):
        for box in range(3):
            if not li % 3:
                boxedsud.append([])    # build a new box every 3 lines
            boxedsud[box + li//3*3].extend(line[box*3:box*3+3])
    for row in boxedsud:
        if sum(row) != SUDOKU_SUM or len(row) != len(set(row)):
            correct = False
            break
    return correct


def sudoku_solved(matrix):
    return box_sum_ok(matrix) and col_sum_ok(matrix) and row_sum_ok(matrix)

if __name__ == '__main__':
    sudoku_solved()

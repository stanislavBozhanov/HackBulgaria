def sudoku_solved(matrix):
    sudoku_sum = 45
    left_diag = []
    right_diag = []
    # Decalring a list of zeros for colomn values
    col = []
    for i in range(len(matrix)):
        col.append(0)
    solved = True
    right_diag_c = len(matrix) - 1
    for r in range(len(matrix)):
        if sum(matrix[r]) != sudoku_sum or len(matrix[r]) != len(set(matrix[r])):
            return False
        right_diag.append(matrix[r][right_diag_c])
        right_diag_c -= 1
        for c in range(len(matrix)):
            if r == c:
                left_diag.append(matrix[r][c])
            if matrix[r][c] in col[c]:
                return False
            else:
                col[c] += matrix[r][c]
    for el in col:
        if el != sudoku_sum:
            solved = False
    if len(left_diag) != len(set(left_diag)):
        return False
    if len(right_diag) != len(set(right_diag)):
        return False
    return solved

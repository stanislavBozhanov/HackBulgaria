def magic_square(matrix):
    magic_number = sum(matrix[0])
    left_diag = 0
    right_diag = 0
    # Decalring a list of zeros for colomn values
    col = []
    for i in range(len(matrix)):
        col.append(0)
    is_magic = True
    right_diag_c = len(matrix) - 1
    for r in range(len(matrix)):
        if sum(matrix[r]) != magic_number:
            is_magic = False
        right_diag += matrix[r][right_diag_c]
        right_diag_c -= 1
        for c in range(len(matrix)):
            if r == c:
                left_diag += matrix[r][c]
            col[c] += matrix[r][c]
    for el in col:
        if el != magic_number:
            is_magic = False
    return is_magic

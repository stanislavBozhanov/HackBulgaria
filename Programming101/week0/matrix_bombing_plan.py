from sum_matrix import sum_matrix


def matrix_bombing_plan(m):
    #rols, cols = len(m), len(m[0])
    temp_m = m
    for r in range(len(m)):
        for c in range(len(m[0])):
            if r - 1 >= 0 and c - 1 >= 0:
                temp_m[r - 1][c - 1] -= temp_m[r][c] :      
import copy


def init_battlefiled(size):
    result_dict = {}
    for r in range(size[0]):
        for c in range(size[1]):
            result_dict[(r, c)] = 0
    return result_dict


def get_size(m):
    r, c = len(m), len(m[0])
    size = (r, c)
    return size


def fileds_exist(rc, sz):
    if rc[0] >= 0 and rc[0] <= sz[0] - 1 and rc[1] >= 0 and rc[1] <= sz[1] - 1:
        return True
    return False


def sum_matrix(temp_m):
    total_sum = 0
    for row in temp_m:
        total_sum += sum(row)
    return total_sum


def bomb(m, field):
    size = get_size(m)
    temp_xy = [(-1, -1), (0, -1), (1, -1),
               (-1, 0), (1, 0),
               (-1, 1), (0, 1), (1, 1)]
    for item in temp_xy:
        cur_field = (field[0] + item[0], field[1] + item[1])
        r1 = cur_field[0]
        c1 = cur_field[1]
        r2 = field[0]
        c2 = field[1]
        if fileds_exist(cur_field, size):
            m[r1][c1] = m[r1][c1] - m[r2][c2]
            if m[r1][c1] < 0:
                m[r1][c1] = 0
    return m


def matrix_bombing_plan(m):
    size = get_size(m)
    plan = init_battlefiled(size)
    for r in range(size[0]):
        for c in range(size[1]):
            field = (r, c)
            temp_m = bomb(copy.deepcopy(m), field)
            total_sum = sum_matrix(temp_m)
            plan[field] = total_sum
    return plan


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    size = get_size(m)
    result = matrix_bombing_plan(m)

    for r in range(size[0]):
        for c in range(size[1]):
            print((r, c), ":", result[r, c])


if __name__ == '__main__':
    main()

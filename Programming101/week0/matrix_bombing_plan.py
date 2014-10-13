def init_battlefiled(size):
    result_dict = {}
    for x in range(size[0]):
        for y in range(size[1]):
            result_dict[(x, y)] = 0
    return result_dict


def print_result(m_dict):
    for field in m_dict:
        print(field, ":", m_dict[field])


def get_size(m):
    x, y = len(m[0]), len(m)
    size = (x, y)
    return size


def fileds_exist(xy, sz):
    if xy[0] >= 0 and xy[0] <= sz[0] - 1 and xy[1] >= 0 and xy[1] <= sz[1] - 1:
        return True
    return False


def sum_matrix(temp_m):
    total_sum = 0
    for row in temp_m:
        total_sum += sum(row)
    return total_sum


def bomb(m, field):
    size = get_size(m)
    temp_m = m
    temp_xy = [(-1, -1), (0, -1), (1, -1),
               (-1, 0), (1, 0),
               (-1, 1), (0, 1), (1, 1)]
    for item in temp_xy:
        cur_field = (field[0] + item[0], field[1] + item[1])
        y1 = cur_field[0]
        x1 = cur_field[1]
        y2 = field[0]
        x2 = field[1]
        if fileds_exist(cur_field, size):
            temp_m[x1][y1] = temp_m[x1][y1] - temp_m[x2][y2]
            if temp_m[x1][y1] < 0:
                temp_m[x1][y1] = 0
    return temp_m


def matrix_bombing_plan(m):
    size = get_size(m)
    plan = init_battlefiled(size)
    for field in plan:
        temp_m = bomb(m, field)
        total_sum = sum_matrix(temp_m)
        plan[field] = total_sum


if __name__ == '__main__':
    print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

def sum_matrix(temp_m):
    total_sum = 0
    for row in temp_m:
        total_sum += sum(row)
    return total_sum


def main():
    print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))


if __name__ == '__main__':
    main()

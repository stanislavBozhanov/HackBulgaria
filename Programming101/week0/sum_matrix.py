def sum_matrix(m):
    sum_ = 0
    for list_ in m:
        sum_ += sum(list_)
    return sum_


def main():
    print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))


if __name__ == '__main__':
    main()

def is_number_balanced(n):
    n = str(n)
    left_sum = 0
    right_sum = 0
    for dig in range(0, (len(n) // 2)):
        left_sum += int(n[dig])
        right_sum += int(n[-dig-1])
    return left_sum == right_sum


def main():
    print(is_number_balanced(9))
    print(is_number_balanced(11))
    print(is_number_balanced(13))
    print(is_number_balanced(121))
    print(is_number_balanced(4518))
    print(is_number_balanced(28471))
    print(is_number_balanced(1238033))


if __name__ == '__main__':
    main()

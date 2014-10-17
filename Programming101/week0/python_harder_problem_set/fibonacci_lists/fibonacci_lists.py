def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    elif n == 2:
        return listB
    elif n < 1:
        return []
    else:
        for i in range(n - 2):
            temp = listA + listB
            listA = listB
            listB = temp
        return listB


def main():
    print(nth_fib_lists([1], [2], 2))
    print(nth_fib_lists([1], [2], 2))
    print(nth_fib_lists([1, 2], [1, 3], 3))
    print(nth_fib_lists([], [1, 2, 3], 6))
    print(nth_fib_lists([0], [0], 100))


if __name__ == '__main__':
    main()

def nth_fibonacci(n):
    a, b = 1, 1
    if n == 1 or n == 2:
        return a
    for number in range(n-2):
        temp = b
        b = a + b
        a = temp
    return b


def main():

    print(nth_fibonacci(1))
    print(nth_fibonacci(2))
    print(nth_fibonacci(3))
    print(nth_fibonacci(10))


if __name__ == '__main__':
    main()

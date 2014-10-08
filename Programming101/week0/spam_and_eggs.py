def prepare_meal(number):
    n = 0
    while number % 3 == 0:
        n += 1
        number //= 3

    if n > 0 and number % 5 != 0:
        return 'spam ' * n
    elif n > 0 and number % 5 == 0:
        return 'spam ' * n + 'and eggs'
    elif n == 0 and number % 5 == 0:
        return 'eggs'
    else:
        return ''


def main():
    print(prepare_meal(3))
    print(prepare_meal(27))
    print(prepare_meal(7))
    print(prepare_meal(5))
    print(prepare_meal(15))
    print(prepare_meal(45))


if __name__ == '__main__':
    main()

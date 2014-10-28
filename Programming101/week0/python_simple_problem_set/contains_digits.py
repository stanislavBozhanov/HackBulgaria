from contains_digit import contains_digit


def contains_digits(number, digits):
    result = True
    for dig in digits:
        if not contains_digit(number, dig):
            return False
    return result


def main():
    print(contains_digits(402123, [0, 3, 4]))
    print(contains_digits(666, [6, 4]))
    print(contains_digits(123456789, [1, 2, 3, 0]))
    print(contains_digits(456, []))

if __name__ == '__main__':
    main()

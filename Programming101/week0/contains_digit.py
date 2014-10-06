def contains_digit(number, digit):
    arr = [ch for ch in str(number)]
    for ch in arr:
        if ch == str(digit):
            return True
    return False


def main():
    print(contains_digit(123, 4))
    print(contains_digit(42, 2))
    print(contains_digit(1000, 0))
    print(contains_digit(12346789, 5))

if __name__ == '__main__':
    main()

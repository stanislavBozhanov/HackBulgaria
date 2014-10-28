def sum_of_digits(n):
    sum_ = 0
    n = abs(n)
    while(n > 0):
        sum_ += n % 10
        n //= 10
    return sum_


def main():
    print(sum_of_digits(1325132435356))
    print(sum_of_digits(123))
    print(sum_of_digits(6))
    print(sum_of_digits(-10))

if __name__ == '__main__':
    main()

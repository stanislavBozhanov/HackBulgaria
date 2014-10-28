def sum_of_divisors(n):
    _sum = 0
    for number in range(1, n+1):
        if n % number == 0:
            _sum += number
    return _sum


def main():
    print(sum_of_divisors(8))
    print(sum_of_divisors(7))
    print(sum_of_divisors(1))
    print(sum_of_divisors(1000))

if __name__ == '__main__':
    main()

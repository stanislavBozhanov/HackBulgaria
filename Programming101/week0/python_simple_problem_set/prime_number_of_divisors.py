from is_prime import is_prime


def number_of_divisors(n):
    count = 0
    for number in range(1, n+1):
        if n % number == 0:
            count += 1
    return count


def prime_number_of_divisors(n):
    return is_prime(number_of_divisors(n))


def main():
    print(prime_number_of_divisors(7))
    print(prime_number_of_divisors(8))
    print(prime_number_of_divisors(9))

if __name__ == '__main__':
    main()

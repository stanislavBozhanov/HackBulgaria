def is_prime(n):
    prime = True
    if n < 2:
        return False
    for number in range(2, n-1):
        if n % number == 0:
            prime = False
    return prime


def main():
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(8))
    print(is_prime(11))
    print(is_prime(-10))
    print(is_prime(97))
    print(is_prime(101))

if __name__ == '__main__':
    main()

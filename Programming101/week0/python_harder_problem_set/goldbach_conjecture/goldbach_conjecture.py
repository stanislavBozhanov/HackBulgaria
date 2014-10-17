#Reused function is_prime from simple problem set


def is_prime(n):
    prime = True
    if n < 2:
        return False
    for number in range(2, n-1):
        if n % number == 0:
            prime = False
    return prime


def goldbach(n):
    result = []
    if n <= 2:
        raise ValueError('Input must be greater than 2')
    if n % 2 != 0:
        raise ValueError('Input must be an even integer')
    for number in range(2, n // 2 + 1):
        if is_prime(number) and is_prime(n - number):
            result.append((number, n - number))
    return result

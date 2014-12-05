def devisors(n):
    result = []
    current = 1

    while current <= n:
        if n % current == 0:
            result.append(current)
        current += 1

    return result


def is_prime(n):
    return n + 1 == sum(devisors)

if __name__ == '__main__':
    is_prime()

def number_to_list(n):
    result = []
    while n > 0:
        result.append(n % 10)
        n //= 10
    result.reverse()
    return result


def main():
    print(number_to_list(123))
    print(number_to_list(99999))
    print(number_to_list(123023))


if __name__ == '__main__':
    main()

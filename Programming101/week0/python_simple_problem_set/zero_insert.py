def zero_insert(n):
    n = str(n)
    dig = len(n) - 1
    while dig > 0:
        if n[dig] == n[dig - 1]:
            n = n[:dig] + '0' + n[dig:]
        elif (int(n[dig]) + int(n[dig - 1])) % 10 == 0:
            n = n[:dig] + '0' + n[dig:]
        dig -= 1
    return int(n)


def main():
    print(zero_insert(116457))
    print(zero_insert(55555555))
    print(zero_insert(6446))


if __name__ == '__main__':
    main()

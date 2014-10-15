def is_an_bn(word):
    if len(word) == 0:
        return True
    return word == 'a' * (len(word) // 2) + 'b' * (len(word) // 2)


def main():
    print(is_an_bn(""))
    print(is_an_bn("rado"))
    print(is_an_bn("aaabb"))
    print(is_an_bn("aaabbb"))
    print(is_an_bn("aabbaabb"))
    print(is_an_bn("bbbaaa"))
    print(is_an_bn("aaaaabbbbb"))


if __name__ == '__main__':
    main()


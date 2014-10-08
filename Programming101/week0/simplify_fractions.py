def simplify_fraction(fraction):
    nom, denom = fraction[0], fraction[1]
    for num in range(min(nom, denom), 1, -1):
        if nom % num == 0 and denom % num == 0:
            nom //= num
            denom //= num
    return (nom, denom)


def main():
    print(simplify_fraction((3, 9)))
    print(simplify_fraction((1, 7)))
    print(simplify_fraction((4, 10)))
    print(simplify_fraction((63, 462)))


if __name__ == '__main__':
    main()

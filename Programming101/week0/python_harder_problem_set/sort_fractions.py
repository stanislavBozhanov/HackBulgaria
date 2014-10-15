def sort_fractions(fractions):
    frac_list = []
    result = []
    for fraction in fractions:
        value = fraction[0] / fraction[1]
        frac_list.append([value, fraction])
    frac_list.sort()
    for x in frac_list:
        result.append(x[1])
    return result


def main():
    print(sort_fractions([(2, 3), (1, 2)]))
    print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
    print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))


if __name__ == '__main__':
    main()

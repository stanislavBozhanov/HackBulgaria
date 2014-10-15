def is_increasing(seq):
    increasing = True
    for i in range(len(seq) - 1):
        if seq[i] >= seq[i+1]:
            increasing = False
    return increasing


def main():
    print(is_increasing([1, 2, 3, 4, 5]))
    print(is_increasing([1]))
    print(is_increasing([5, 6, -10]))
    print(is_increasing([1, 1, 1, 1]))


if __name__ == '__main__':
    main()

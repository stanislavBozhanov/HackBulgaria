def is_decreasing(seq):
    decreasing = True
    for i in range(len(seq) - 1):
        if seq[i] <= seq[i+1]:
            decreasing = False
    return decreasing


def main():
    print(is_decreasing([5, 4, 3, 2, 1]))
    print(is_decreasing([1, 2, 3]))
    print(is_decreasing([100, 50, 20]))
    print(is_decreasing([1, 1, 1, 1]))


if __name__ == '__main__':
    main()

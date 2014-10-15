def biggest_difference(arr):
    result = min(arr) - max(arr)
    return result


def main():
    print(biggest_difference([1, 2]))
    print(biggest_difference([1, 2, 3, 4, 5]))
    print(biggest_difference([-10, -9, -1]))
    print(biggest_difference(range(100)))


if __name__ == '__main__':
    main()

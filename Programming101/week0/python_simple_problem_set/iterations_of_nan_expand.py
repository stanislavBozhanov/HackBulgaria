from nan_expand import nan_expand


def iterations_of_nan_expand(expanded):
    times = expanded.count('Not')
    if nan_expand(times) == expanded:
        return times
    return False


def main():
    print(iterations_of_nan_expand(""))
    print(iterations_of_nan_expand("Not a NaN"))
    print(iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
    print(iterations_of_nan_expand("Show these people!"))


if __name__ == '__main__':
    main()

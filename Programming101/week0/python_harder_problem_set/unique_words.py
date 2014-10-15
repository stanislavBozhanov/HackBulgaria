from count_words import count_words


def unique_words_count(arr):
    unique = 0
    words = count_words(arr)
    for word in words:
        unique += 1
    return unique


def main():
    print(unique_words_count(["apple", "banana", "apple", "pie"]))
    print(unique_words_count(["python", "python", "python", "ruby"]))
    print(unique_words_count(["HELLO!"] * 10))


if __name__ == '__main__':
    main()

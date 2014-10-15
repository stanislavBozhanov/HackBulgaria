from count_substrings import count_substrings


def count_vowels(str_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    result = 0
    for ch in vowels:
        result += count_substrings(str_, ch)
    return result


def main():
    print(count_vowels("Python"))
    print(count_vowels("Theistareykjarbunga"))
    print(count_vowels("grrrrgh!"))
    print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
    print(count_vowels("A nice day to code!"))


if __name__ == '__main__':
    main()

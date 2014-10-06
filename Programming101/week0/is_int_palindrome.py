def is_int_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False


def main():
    print(is_int_palindrome(1))
    print(is_int_palindrome(42))
    print(is_int_palindrome(100001))
    print(is_int_palindrome(999))
    print(is_int_palindrome(123))

if __name__ == '__main__':
    main()

from fibonacci_lists import nth_fib_lists


def member_of_nth_fib_lists(listA, listB, needle):
    lengh = 0
    member = 1
    while lengh <= len(needle):
        lengh = len(nth_fib_lists(listA, listB, member))
        if nth_fib_lists(listA, listB, member) == needle:
            return True
        member += 1
    return False


def main():
    print(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
    print(member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]))
    print(member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2]))
    print(member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]))


if __name__ == '__main__':
    main()

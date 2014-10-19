def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    elif n == 2:
        return listB
    elif n < 1:
        return []
    else:
        for i in range(n - 2):
            temp = listA + listB
            listA = listB
            listB = temp
        return listB


def member_of_nth_fib_lists(listA, listB, needle):
    lengh = 0
    member = 1
    while lengh <= len(needle):
        lengh = len(nth_fib_lists(listA, listB, member))
        if nth_fib_lists(listA, listB, member) == needle:
            return True
        member += 1
    return False

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

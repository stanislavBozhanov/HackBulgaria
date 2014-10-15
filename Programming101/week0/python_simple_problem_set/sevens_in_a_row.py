def sevens_in_a_row(arr, n):
    result = False
    for i in range(len(arr) - n):
        if arr[i] == 7:
            result = True
            for j in range(i+1, i+n):
                if arr[j] != 7:
                    result = False
            if result:
                break
    return result


def main():
    print(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))
    print(sevens_in_a_row([1, 7, 1, 7, 7], 4))
    print(sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 3))
    print(sevens_in_a_row([7, 2, 1, 6, 2], 1))

if __name__ == '__main__':
    main()

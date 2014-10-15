import sys


def main():
    file = open(sys.argv[1], 'r')

    content = file.read()

    numbers = content.split(' ')
    summ = 0
    for num in numbers:
        summ += int(num)
    print(summ)

if __name__ == '__main__':
    main()

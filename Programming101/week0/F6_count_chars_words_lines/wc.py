import sys
import re


def wc(command, filename):
    txt_file = open(filename, 'r')
    content = txt_file.read()
    if command == 'chars':
        return len(content)
    elif command == 'words':
        words = re.split(' |\n\n', content)
        return len(words)
    elif command == 'lines':
        lines = content.split('\n')
        return len(lines)
    else:
        return 'Wrong command!'


def main():
    command = sys.argv[1]
    filename = sys.argv[2]
    print(wc(command, filename))


if __name__ == '__main__':
    main()

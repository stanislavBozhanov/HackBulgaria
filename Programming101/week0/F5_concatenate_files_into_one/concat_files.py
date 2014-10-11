import sys


def main():
    filename = 'MEGATRON.txt'
    file_w = open(filename, 'a')

    for arg in range(1, len(sys.argv)):
        file_r = open(sys.argv[arg], 'r')
        content = file_r.read()
        file_w.write(''.join(content))
        file_r.close()

    file_w.close()

if __name__ == '__main__':
    main()

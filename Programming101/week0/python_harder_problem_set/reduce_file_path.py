def reduce_file_path(path):
    path = path.split('/')
    result = []
    for element in path:
        if element == '..':
            if result:
                result.pop()
        elif element != '.' and element != '/':
            result.append(element)
    result = list(filter(None, result))
    path = '/' + '/'.join(result)
    return path


def main():
    print(reduce_file_path("/"))
    print(reduce_file_path("/srv/../"))
    print(reduce_file_path("/srv/www/htdocs/wtf/"))
    print(reduce_file_path("/srv/www/htdocs/wtf"))
    print(reduce_file_path("/srv/./././././"))
    print(reduce_file_path("/etc//wtf/"))
    print(reduce_file_path("/etc/../etc/../etc/../"))
    print(reduce_file_path("//////////////"))
    print(reduce_file_path("/../"))


if __name__ == '__main__':
    main()

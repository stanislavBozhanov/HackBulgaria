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

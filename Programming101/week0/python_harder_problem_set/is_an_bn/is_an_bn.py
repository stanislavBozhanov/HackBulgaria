def is_an_bn(word):
    if len(word) == 0:
        return True
    return word == 'a' * (len(word) // 2) + 'b' * (len(word) // 2)

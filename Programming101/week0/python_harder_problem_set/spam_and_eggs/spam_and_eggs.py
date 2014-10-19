def prepare_meal(number):
    n = 0
    while number % 3 == 0:
        n += 1
        number //= 3

    if n > 0 and number % 5 != 0:
        return 'spam' + (n - 1) * ' spam'
    elif n > 0 and number % 5 == 0:
        return 'spam' + ' spam' * (n - 1) + ' and eggs'
    elif n == 0 and number % 5 == 0:
        return 'eggs'
    else:
        return ''

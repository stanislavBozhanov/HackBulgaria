def what_is_my_sign(day, month):
    signs = [
            [121, 219, 'Aquarius'],
            [220, 320, 'Pisces'],
            [321, 420, 'Aries'],
            [421, 521, 'Taurus'],
            [522, 621, 'Gemini'],
            [622, 722, 'Cancer'],
            [723, 822,  'Leo'],
            [823, 923, 'Virgo'],
            [924, 1023, 'Libra'],
            [1024, 1122, 'Scorpio'],
            [1123, 1221, 'Sagittarius'],
            [1222, 1231, 'Capricorn'],
            [0, 120, 'Capricorn']]
    date = day + month * 100
    for sign in signs:
        if date >= sign[0] and date <= sign[1]:
            return sign[2]


def main():
    print(what_is_my_sign(5, 8))
    print(what_is_my_sign(29, 1))
    print(what_is_my_sign(30, 6))
    print(what_is_my_sign(31, 5))
    print(what_is_my_sign(2, 2))
    print(what_is_my_sign(8, 5))
    print(what_is_my_sign(9, 1))


if __name__ == '__main__':
    main()

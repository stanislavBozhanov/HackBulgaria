def sort_fractions(fractions):
    frac_list = []
    result = []
    for fraction in fractions:
        value = fraction[0] / fraction[1]
        frac_list.append([value, fraction])
    frac_list.sort()
    for x in frac_list:
        result.append(x[1])
    return result

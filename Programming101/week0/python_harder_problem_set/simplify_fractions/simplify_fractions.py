def simplify_fraction(fraction):
    nom, denom = fraction[0], fraction[1]
    for num in range(min(nom, denom), 1, -1):
        if nom % num == 0 and denom % num == 0:
            nom //= num
            denom //= num
    return (nom, denom)

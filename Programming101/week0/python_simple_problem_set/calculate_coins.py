def calculate_coins(sum_):
    coins = [100, 50, 20, 10, 5, 2, 1]
    best_split = {1: 0, 2: 0, 100: 0, 5: 0, 10: 0, 50: 0, 20: 0}
    sum_ = int(sum_ * 100)
    for coin in coins:
        while sum_ - coin >= 0:
            best_split[coin] += 1
            sum_ -= coin
        if not sum_:
            break
    return best_split


def main():
    print(calculate_coins(0.53))
    print(calculate_coins(8.94))


if __name__ == '__main__':
    main()

class CashDesk(object):

    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, inserted):
        self.inserted = inserted
        for note, amount in inserted.items():
            self.money[note] += amount
"""
    def total(self):
        total_sum = 0
        for note, amount in self.money.items():
            total_sum += int(self.money[amount]) * int(note)
        return total_sum

    def can_withdraw_money(self, amount_of_money):
        self.amount_of_money = amount_of_money
        for note, amount in  amount_of_money.items():
"""
my_cash_desk = CashDesk()
my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
print(my_cash_desk.money)
# my_cash_desk.total()

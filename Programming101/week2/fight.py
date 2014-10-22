from random import random


class Fight():
    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def flip_coin(self):
        num = random()
        if num <= 0.5:
            return 0
        return 1

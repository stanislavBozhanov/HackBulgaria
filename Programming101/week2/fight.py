from random import random


class Fight():
    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def get_player_order(self):
        num = random()
        if num <= 0.5:
            return (self.hero, self.orc)
        return (self.orc, self.hero)

    def simulate_fight(self):
        attacker, defender = self.get_player_order()

        while self.hero.is_alive() and self.orc.is_alive():
            damage = attacker.attack()
            #print("{} hit {} for {} damage".format(attacker.name, defender.name, damage))
            defender.take_damage(damage)

            attacker, defender = defender, attacker

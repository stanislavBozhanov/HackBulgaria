class Entity(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._MAX_HEALTH = health
        self.equipped_weapon = None

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def take_healing(self, healing):
        if self.health == 0:
            return False
        else:
            if self._MAX_HEALTH < self.health + healing:
                self.health = self._MAX_HEALTH
            else:
                self.health += healing
        return True

    def has_weapon(self):
        if self.equipped_weapon:
            return True
        else:
            return False

    def equip_weapon(self, weapon):
        self.equipped_weapon = weapon

    def attack(self):
        if not self.has_weapon():
            return 0

        if self.equipped_weapon.critical_hit():
            return self.equipped_weapon.damage * 2
        else:
            return self.equipped_weapon.damage

from entity import Entity


class Hero(Entity):
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname = nickname
        self._MAX_HEALTH = health

    def known_as(self):
        return "{} the {}".format(self.name, self.nickname)

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

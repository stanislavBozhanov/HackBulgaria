class Hero(object):
    def __init__(self, name, health, nickname):
        self.name = name
        self.health = health
        self.nickname = nickname

    def known_as(self):
        return "{} the {}".format(self.name, self.nickname)
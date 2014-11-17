import sqlite3

movies = [
    ('The Hunger games: Catching Fire', 7.9),
    ('Wreck-It Ralph', 7.8),
    ('Her', 8.3)
]

projections = [
    (1, '3D', )
]


class MagicCinema:
    def __init__(self, db, ):
        self.connection = sqlite3.connect(db)
        self.connection.execute('PRAGMA foreign_keys = ON')
        self.connection.commit()
        self.cursor = self.connection.cursor()

    def query(self, arg):
        self.cursor.execute(arg)
        self.connection.commit()
        return self.cursor

    def queries(self, args):
        self.cursor.executemany(args)
        self.connection.commit()
        return self.cursor

    def __del__(self):
        self.connection.close()

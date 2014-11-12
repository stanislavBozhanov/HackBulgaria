import sqlite3


def create_table_movies():
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
                id INTEGER  PRIMARY KEY, name TEXT,
                rating REAL
                )''')
    db.commit()
    db.close()


def create_table_projections():
    db = sqlite3.connect('projections.db')
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS projections(
                id INTEGER PRIMARY KEY,
                movie_id INTEGER,
                type TEXT,
                date_ TEXT,
                time_ TEXT,
                FOREIGN KEY(movie_id) REFERENCES movies(id)
                )''')
    db.commit()
    db.close()


def create_table_reservations():
    db = sqlite3.connect('reservations.db')
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS reservations(
                id INTEGER  PRIMARY KEY,
                username TEXT,
                projection_id INTEGER,
                row INTEGER,
                col INTEGER,
                FOREIGN KEY(projection_id) REFERENCES projections(id)
                )''')
    db.commit()
    db.close()


def main():
    pass

if __name__ == '__main__':
    main()

import sqlite3


def create_table_movies():
    db = sqlite3.connect('cinema.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
                id INTEGER  PRIMARY KEY,
                name TEXT,
                rating REAL
                )''')
    db.commit()
    db.close()


def create_table_projections():
    db = sqlite3.connect('cinema.db')
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
    db = sqlite3.connect('cinema.db')
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


def insert_movie():
    name = input('movie_name>')
    rating = float(input('movie_rating>'))
    db = sqlite3.connect('cinema.db')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO movies(name, rating) VALUES(?,?)''', (name, rating))
    db.commit()
    db.close()


def show_movies():
    connection = sqlite3.connect('cinema.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    result = cursor.execute('SELECT id, name, rating FROM movies')
    for row in result:
        print('[{id}] - {name} ({rating})'.format(**row))


def main():
    create_table_movies()
    create_table_projections()
    create_table_reservations()
    while True:
        command = input('command>')
        command = command.split()
        if command[0] == 'show_movies':
            show_movies()
        elif command[0] == 'insert_movie':
            insert_movie()
        elif command[0] == 'break':
            break

if __name__ == '__main__':
    main()

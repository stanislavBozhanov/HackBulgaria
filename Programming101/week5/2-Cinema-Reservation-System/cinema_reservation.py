import sqlite3


def create_table_movies(db, cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
                id INTEGER  PRIMARY KEY,
                name TEXT,
                rating REAL
                )''')
    db.commit()


def create_table_projections(db, cursor):
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS projections(
                id INTEGER PRIMARY KEY,
                movie_id INTEGER,
                type_ TEXT,
                date_ TEXT,
                time_ TEXT,
                FOREIGN KEY(movie_id) REFERENCES movies(id)
                )''')
    db.commit()


def create_table_reservations(db, cursor):
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


def insert_movie(db, cursor, name, rating):
    cursor = db.cursor()
    cursor.execute('''INSERT INTO movies(name, rating) VALUES(?,?)''', (name, rating))
    db.commit()


def show_movies(db, cursor):
    cursor = db.cursor()
    result = cursor.execute('SELECT id, name, rating FROM movies ORDER BY rating')
    for row in result:
        print('[{id}] - {name} ({rating})'.format(**row))


def insert_projection(db, cursor, movie_id, type_, date_, time_):
    cursor = db.cursor()
    cursor.execute('''INSERT INTO projections(movie_id, type_, date_, time_)
                    VALUES(?,?,?,?)''', (movie_id, type_, date_, time_))
    db.commit()


def show_projections(db, cursor, movie_id, date_=None):
    cursor = db.cursor()
    if not date_:
        result = cursor.execute(''' SELECT projections.id, projections.date_, projections.time_, movies.name, projections.type_
                                    FROM projections
                                    INNER JOIN movies
                                    ON projections.movie_id = movies.id
                                    WHERE movie_id = ?
                                    ORDER BY date_''', (movie_id,))
        for row in result:
            #print("Projections for movie '{name}':".format(**row))
            print('[{id}] - {date_} ({type_})'.format(**row))
    else:
        result = cursor.execute(''' SELECT projections.id, projections.date_, projections.time_, movies.name, projections.type_
                                    FROM projections
                                    INNER JOIN movies
                                    ON projections.movie_id = movies.id
                                    WHERE movie_id = ? AND date_ = ?
                                    ORDER BY date_''', (movie_id, date_))
        for row in result:
            #print("Projections for movie '{name}' on date {date_}:".format(**row))
            print('[{id}] - {date_} ({type_})'.format(**row))


def main():
    db = sqlite3.connect('cinema.db')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    create_table_movies(db, cursor)
    create_table_projections(db, cursor)
    create_table_reservations(db, cursor)
    while True:
        command = input('command>')
        command = command.split()
        if command[0] == 'show_movies':
            show_movies(db, cursor)
        elif command[0] == 'insert_movie':
            name = input('movie_name>')
            rating = float(input('movie_rating>'))
            insert_movie(db, cursor, name, rating)
        elif command[0] == 'insert_projection':
            movie_id = int(input('movie_id>'))
            type_ = input('type>')
            date_ = input('date>')
            time_ = input('time>')
            insert_projection(db, cursor, movie_id, type_, date_, time_)
        elif command[0] == 'show_projections':
            movie_id = int(command[1])
            if len(command) == 3:
                date_ = command[2]
                show_projections(db, cursor, movie_id, date_)
            elif len(command) == 2:
                show_projections(db, cursor, movie_id)
        # elif command[0] == 'remove_movie':
        #     name = input('Enter movie name>')
        #     remove_movie(db, name)
        elif command[0] == 'break':
            db.close()
            break

if __name__ == '__main__':
    main()

import sqlite3


def create_table_movies(db, cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
                id INTEGER  PRIMARY KEY,
                name TEXT,
                rating REAL
                )''')
    db.commit()


def create_table_projections(db, cursor):
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
    cursor.execute('''INSERT INTO movies(name, rating) VALUES(?,?)''', (name, rating))
    db.commit()


def show_movies(db, cursor):
    result = cursor.execute('SELECT id, name, rating FROM movies ORDER BY rating')
    for row in result:
        print('[{id}] - {name} ({rating})'.format(**row))


def insert_projection(db, cursor, movie_id, type_, date_, time_):
    cursor.execute('''INSERT INTO projections(movie_id, type_, date_, time_)
                    VALUES(?,?,?,?)''', (movie_id, type_, date_, time_))
    db.commit()


def show_projections(db, cursor, movie_id, date_=None):
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


def get_reserved_seats(db, cursor, projection_id):
    seats = []
    result = cursor.execute(''' SELECT row, col
                                FROM reservations
                                WHERE projection_id = ?''', (projection_id,))
    for line in result:
        seats.append((line['row'], line['col']))
    return seats


def reserve_seats(reserved):
    matrix = [
        [' ', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        [2, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        [3, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        [4, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        [5, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        [6, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        [7, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        [8, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        [9, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        [10, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ]
    for item in reserved:
        matrix[item[0]][item[1]] = 'X'

    return matrix


def print_seats(matrix):
    for row in matrix:
        print(row)


def get_projections_for_movie(db, cursor, movie_id):
    result = cursor.execute(''' SELECT id, date_, time_, type_
                                FROM projections
                                WHERE movie_id = ?''', (movie_id,)).fetchall()
    for line in result:
        reserved = get_reserved_seats(db, cursor, line['id'])
        print('[{id}] - {date_} {time_} ({type_})'.format(**line) + ' - {} spots available'.format(100 - len(reserved)))


def insert_reservation(db, cursor, username, projection_id, row, col):
    cursor.execute('''INSERT INTO reservations(username, projection_id, row, col)
                    VALUES(?,?,?,?)''', (username, projection_id, row, col))
    db.commit()


def create_all_tables(db, cursor):
    create_table_movies(db, cursor)
    create_table_projections(db, cursor)
    create_table_reservations(db, cursor)


# def show_reservations():
#     matrix = ['.' for x in range(1,11) ]


def main():
    db = sqlite3.connect('cinema.db')
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA foreign_keys = ON')
    db.commit()
    cursor = db.cursor()
    create_all_tables(db, cursor)
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

        elif command[0] == 'insert_reservation':
            username = input('username>')
            projection_id = int(input('projection_id>'))
            row = int(input('row>'))
            col = int(input('col>'))
            insert_reservation(db, cursor, username, projection_id, row, col)

        elif command[0] == 'make_reservation':
            username = input('Choose name>')
            number_of_tickets = int(input('Choose number of tickets>'))
            print('Current movies:')
            show_movies(db, cursor)
            movie_id = int(input('Choose a movie>'))
            movie_name = cursor.execute('SELECT name FROM movies WHERE id = ?', (movie_id,)).fetchone()['name']
            print('Projections for movie {}'.format(movie_name))
            get_projections_for_movie(db, cursor, movie_id)

        elif command[0] == 'break':
            db.close()
            break

if __name__ == '__main__':
    main()

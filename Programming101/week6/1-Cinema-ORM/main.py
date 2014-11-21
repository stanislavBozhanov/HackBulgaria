from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from connection import Base
from movie import Movie
from projection import Projection
from reservation import Reservation
# from cinema import Cinema


engine = create_engine('sqlite:///cinema.db')
session = Session(bind=engine)


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


def show_movies():
    all_movies = session.query(Movie).order_by(Movie.rating)
    for movie in all_movies:
        print(movie)


def add_movie():
    name = input('name>')
    rating = float(input('rating>'))
    new_movie = Movie(name=name, rating=rating)
    session.add(new_movie)
    session.commit()


def add_projection():
    type_ = input('type>')
    date_ = input('date>')
    time_ = input('time>')
    movie_id = int(input('movie_id'))
    new_projection = Projection(type_=type_, date_=date_, time_=time_, movie_id=movie_id)
    session.add(new_projection)
    session.commit()


def add_reservation():
    un = input('username>')
    row = int(input('row>'))
    col = int(input('col>'))
    p_id = int(input('projection_id>'))
    new_reservation = Reservation(username=un, row=row, col=col, projection_id=p_id)
    session.add(new_reservation)
    session.commit()


def main():
    Base.metadata.create_all(engine)

    while True:
        command = input(">>>")
        if command == 'add_movie':
            add_movie()
        elif command == 'add_projection':
            add_projection()
        elif command == 'add_reservation':
            add_reservation()
        elif command == 'show_movies':
            show_movies()

if __name__ == '__main__':
    main()

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from connection import Base
from cinema import Cinema
# from movie import Movie
# from projection import Projection
# from reservation import Reservation


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


def main():
    Base.metadata.create_all(engine)
    arena = Cinema()

    while True:
        command = input(">>>")
        if command == 'add_movie':
            arena.add_movie()
        elif command == 'add_projection':
            arena.add_projection()
        elif command == 'add_reservation':
            arena.add_reservation()
        elif command == 'show_movies':
            arena.show_movies()
        elif command == 'show_movie_projections':
            arena.show_movie_projections(1, '2014-03-22')

if __name__ == '__main__':
    main()

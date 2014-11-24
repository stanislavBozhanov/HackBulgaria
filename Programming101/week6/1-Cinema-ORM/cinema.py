from movie import Movie
from projection import Projection
from reservation import Reservation
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class Cinema:
    def __init__(self):
        self.__engine = create_engine('sqlite:///cinema.db')
        self.__session = Session(bind=self.__engine)

    def show_movies(self):
        all_movies = self.__session.query(Movie).order_by(Movie.rating)
        for movie in all_movies:
            print(movie)

    def add_movie(self):
        name = input('name>')
        rating = float(input('rating>'))
        new_movie = Movie(name=name, rating=rating)
        self.__session.add(new_movie)
        self.__session.commit()

    def add_projection(self):
        type_ = input('type>')
        date_ = input('date>')
        time_ = input('time>')
        movie_id = int(input('movie_id'))
        new_projection = Projection(type_=type_, date_=date_, time_=time_, movie_id=movie_id)
        self.__session.add(new_projection)
        self.__session.commit()

    def add_reservation(self):
        un = input('username>')
        row = int(input('row>'))
        col = int(input('col>'))
        p_id = int(input('projection_id>'))
        new_reservation = Reservation(username=un, row=row, col=col, projection_id=p_id)
        self.__session.add(new_reservation)
        self.__session.commit()

    def show_movie_projections(self, movie_id, date_=None):
        if date_:
            all_projections = self.__session.query(Projection).\
                filter(Projection.movie_id == int(movie_id), Projection.date_ == date_).\
                order_by(Projection.time_)
            for proj in all_projections:
                print('[{}] - {} ({})'.format(proj.id, proj.time_, proj.type_))
        else:
            all_projections = self.__session.query(Projection).\
                filter(Projection.movie_id == movie_id).\
                order_by(Projection.date_, Projection.time_)
            for proj in all_projections:
                print('[{}] - {} {} ({})'.format(proj.id, proj.date_, proj.time_, proj.type_))

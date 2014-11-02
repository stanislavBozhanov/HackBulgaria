class Song():
    MAX_RATING = 5
    MIN_RATING = 1

    def __init__(self, name, artist, album, rating, length, bitrate):
        self.name = name
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self, number):
        if number < Song.MIN_RATING or number > Song.MAX_RATING:
            formatted = "Rating must be between {} and {}"
            raise ValueError(formatted.format(Song.MIN_RATING, Song.MAX_RATING))
        else:
            self.rating = number

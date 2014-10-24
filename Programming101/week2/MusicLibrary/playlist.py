class Playlist():
    def __init__(self, name):
        self.name = name
        self.songs = []

    def __str__(self):
        output = ""
        for item in self.songs:
            minutes = item.length // 60
            seconds = item.length % 60
            output += "{} {} - {:02d}:{:02d}\n".format(item.artist, item.name, minutes, seconds)
        return output

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        index = len(self.songs) - 1
        while index >= 0:
            if self.songs[index].name == song_name:
                self.songs[index] = None
            index = index - 1

    def total_length(self):
        seconds = 0
        for item in self.songs:
            seconds += item.length
        return seconds

    def remove_disrated(self, rating):
        index = len(self.songs) - 1
        while index >= 0:
            if self.songs[index].rating < rating:
                self.songs[index] = None
            index = index - 1

    def remove_bad_quality(self):
        index = len(self.songs) - 1
        while index >= 0:
            if self.songs[index].bitrate < 128:
                self.songs[index] = None
            index = index - 1

    def show_artists(self):
        artists = []
        for item in self.songs:
            artists.append(item.artist)
        artists = list(set(artists))
        return artists

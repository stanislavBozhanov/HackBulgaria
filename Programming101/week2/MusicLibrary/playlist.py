class Playlist():
    def __init__(self, name):
        self.name = name
        self.songs = []

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
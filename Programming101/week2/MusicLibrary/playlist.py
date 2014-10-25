from song import Song
import os.path
import json


def load(file_name):
    my_file = open(file_name, 'r')
    content = my_file.read()
    content = json.loads(content)
    my_file.close()
    loaded_plist = Playlist(content['name'])
    for song in content['songs']:
        loaded_plist.songs.append(
            Song(
                song['name'],
                song['artist'],
                song['album'],
                song['rating'],
                song['length'],
                song['bitrate']
            )
        )
    return loaded_plist


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

    def save(self):
        playlist = {"name": self.name, "songs": []}
        for item in self.songs:
            item = item.__dict__
            playlist["songs"].append(item)
        if os.path.isfile(self.name + ".json"):
            print("That playlist name is taken")
        else:
            my_file = open("{}.json".format(self.name), 'a+')
            my_file.write(json.dumps(playlist))
            my_file.close()

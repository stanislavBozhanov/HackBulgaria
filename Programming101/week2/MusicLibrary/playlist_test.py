import unittest
from song import Song
from playlist import Playlist


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.plist = Playlist("plist out")
        self.ruby = Song(
            "Ruby",
            "Kaiser Chiefs",
            "Unknown",
            1,
            300,
            320

        )
        self.plist.add_song(self.ruby)
        self.plist.add_song(self.ruby)

    def test_init(self):
        self.assertEqual(self.plist.name, "plist out")

    def test_add_song(self):
        self.assertIn(self.ruby, self.plist.songs)

    def test_remove_song(self):
        self.plist.remove_song("Ruby")
        self.assertNotIn(self.ruby, self.plist.songs)

    def test_total_length(self):
        self.assertEqual(self.plist.total_lenght(), 600)

if __name__ == '__main__':
    unittest.main()

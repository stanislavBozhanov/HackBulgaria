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
        self.rubyDNB = Song(
            "Ruby DNB",
            "Kaiser Chiefs",
            "Unknown",
            4,
            300,
            120

        )
        self.plist.add_song(self.ruby)
        self.plist.add_song(self.ruby)
        self.plist.add_song(self.rubyDNB)

    def test_init(self):
        self.assertEqual(self.plist.name, "plist out")

    def test_add_song(self):
        self.assertIn(self.ruby, self.plist.songs)

    def test_remove_song(self):
        self.plist.remove_song("Ruby")
        self.assertNotIn(self.ruby, self.plist.songs)

    def test_total_length(self):
        self.assertEqual(self.plist.total_length(), 900)

    def test_rating_out_of_range(self):
        for item in self.plist.songs:
            self.assertIn(item.rating, [1, 2, 3, 4, 5])

    def test_remove_disrated(self):
        self.plist.remove_disrated(3)
        self.assertIn(self.rubyDNB, self.plist.songs)
        self.assertNotIn(self.ruby, self.plist.songs)

    def test_remove_bad_quality(self):
        self.plist.remove_bad_quality()
        self.assertNotIn(self.rubyDNB, self.plist.songs)

    def test_show_artists(self):
        self.assertEqual(self.plist.show_artists(), ["Kaiser Chiefs"])

    def test_print_list(self):
        print(self.plist)

if __name__ == '__main__':
    unittest.main()

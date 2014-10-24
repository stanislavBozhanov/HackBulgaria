from song import Song
import unittest


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song(
            "Gangam Style",
            "PSY",
            "PSY",
            1,
            300,
            320
        )

    def test_init(self):
        self.assertEqual(self.song.name, "Gangam Style")
        self.assertEqual(self.song.artist, "PSY")
        self.assertEqual(self.song.album, "PSY")
        self.assertEqual(self.song.rating, 1)
        self.assertEqual(self.song.length, 300)
        self.assertEqual(self.song.bitrate, 320)

    def test_rate(self):
        self.assertRaises(ValueError, self.song.rate, (6))
        self.song.rate(3)
        self.assertEqual(self.song.rating, 3)


if __name__ == '__main__':
    unittest.main()

class Song:
    pass
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song._update_class_variables(artist, genre)

    @classmethod
    def _update_class_variables(cls, artist, genre):
        cls.count += 1
        cls.genres.add(genre)
        cls.artists.add(artist)

        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
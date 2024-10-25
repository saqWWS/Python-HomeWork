import abc


class Songs(abc.ABC):
    def __init__(self, title: str, artist: str, length: float):
        self.title = title
        self.artist = artist
        self.length = length

    def __repr__(self):
        return f"title: {self.title}, artist: {self.artist}, length: {self.length}"


class Rock(Songs):
    def __init__(self, title: str, artist: str, length: float):
        super().__init__(title, artist, length)

    def __repr__(self):
        return f"title: {self.title}, artist: {self.artist}, length: {self.length}"


rammstein = Rock("Sonne", "Rammstein", 4.13)
linkin_park = Rock("In the End", "Linkin Park", 3.39)
the_doors = Rock("Riders on the Storm", "The Doors", 7.10)


class POP(Songs):
    def __init__(self, title: str, artist: str, length: float):
        super().__init__(title, artist, length)

    def __repr__(self):
        return f"title: {self.title}, artist: {self.artist}, length: {self.length}"


ed_sheeran = POP("Perfect", "Ed Sheeran", 4.40)
nesli = POP("La Fine", "Nesli", 3.42)
fabri_fibra = POP("Stavo Pensando A Te", "Fabri Fibra", 4.26)


class Jazz(Songs):
    def __init__(self, title: str, artist: str, length: float):
        super().__init__(title, artist, length)

    def __repr__(self):
        return f"title: {self.title}, artist: {self.artist}, length: {self.length}"


louis_armstrong = Jazz("What a Wonderful World", "Louis Armstrong", 2.29)
sarah_vaughan = Jazz("Misty", "Sarah Vaughan", 5.45)
frank_sinatra = Jazz("I Love You Baby", "Frank Sinatra", 3.56)


class Albums:
    def __init__(self, title: str, artist: str, release_date: int):
        self.title = title
        self.artist = artist
        self.release_date = release_date
        self.songs_list = []

    def songs(self, song):
        self.songs_list.append(song)

    def show_album(self):
        return f" title: {self.title}, artiest: {self.artist}, date: {self.release_date} n\ {[x for x in self.songs_list]}"


class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.songs = []

    def add_song(self, value):
        self.songs.append(value)

    def list_of_songs(self, user: 'Users'):
        return f"{Users(user)} songs list: {self.songs}"

    def find_song(self, song):
        if song in self.songs:
            return song
        return "Song not found"


class Users:
    def __init__(self, user):
        self.user = user

    def __repr__(self):
        return f"{self.user}"

    def listen_song(self, value):
        return f"{self.user} listen: {value}"


user_1 = Users("Alice")
print(user_1.listen_song(rammstein))

play = Playlist("Top")
play.add_song(frank_sinatra)
play.add_song(fabri_fibra)
print(play.list_of_songs(user_1))
print()

print(play.find_song(rammstein))

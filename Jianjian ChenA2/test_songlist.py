"""
(incomplete) Tests for SongList class
"""
from Assignment2.songlist import SongList
from Assignment2.song import Song

# test empty SongList
song_list = SongList()
print(song_list)
assert len(song_list.songs) == 0

# test loading songs
song_list.load_songs('songs.csv')
print(song_list)
assert len(song_list.songs) > 0  # assuming CSV file is not empty

# TODO: add tests below to show the various required methods work as expected
# test sorting songs
print('Sorting:')
song_list.sort('year')
print(song_list)
song_list.sort('artist')
print(song_list)
# test adding a new Song
song_list.add_songs(Song('title','artist',1999,Song.is_required))

def song_playlist(songs, max_size):
    """
    Start with the first song in the 'songs' list, then pick the 
    song to be the one with the lowest file size not already picked, repeat.
    :param songs: list of tuples, ('song_name', song_len, song_size) 
    :param max_size: float, maximum size of total songs that you can fit
    :return: a list of a subset of songs fitting in 'max_size' in the
             order in which they were chosen.
    """
    cum_size = 0
    picked_songs = []
    if songs[0][2] <= max_size:
        picked_songs.append(songs[0][0])
        cum_size += songs[0][2]
        songs_copy = sorted(songs[1:], key=lambda x: x[2])
        for song in songs_copy:
            if cum_size + song[2] > max_size:
                break;
            else:
                if song[0] not in picked_songs:
                    picked_songs.append(song[0])
                    cum_size += song[2]
    else:
        pass
    return picked_songs

songs = [('Roar',4.4, 4.0),('Timber', 5.1, 6.9),('Sail',3.5, 7.7),('Wannabe',2.7, 1.2)]
print(song_playlist(songs, 25))



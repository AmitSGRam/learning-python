def make_album(artist, title, no_of_songs=None):
    album = {'artist' : artist, 'title' : title}
    if no_of_songs:
        album['no'] = no_of_songs
    #print(album)
    return album

album = make_album('weeknd', 'starboy', 18)
print(album)
album = make_album('weeknd', 'House of Balloons')
print(album)
def make_albums(artist, title, no_of_songs=None):
    album = {'artist' : artist, 'title' : title}
    if no_of_songs:
        album['ln'] = no_of_songs
    return album

while True:
    print(
        "\nThis function is to make a dictionary of albums with name of the artist, title of the album, number of songs in the album"
    )
    print("\nPlease enter 'q' to quit at any time.")
    artist_name = input("\nPlease Enter name of the artist.\t")
    if artist_name == 'q':
        break
    title_name = input("\nPlease Enter name of the album.\t")
    if title_name == 'q':
        break
    number_of_songs = input("\nPlease enter the number of songs in the album.(not mandatory)\t")
    if number_of_songs == 'q':
        break
    album = make_albums(artist_name, title_name, number_of_songs)
    print(album)
def make_album(artist, title, tracks=0):
    if tracks:
        album = {
            artist: [title, tracks]
        }
    else:
        album = {
            artist: title
        }
    print(album)

loop = 1
while loop == 1:
    artist = input("Enter the artist's name: ")
    title = input("Enter the album title: ")

    feedback = input("Would you like to enter the number of tracks? [yes/no] ")
    if feedback.lower() == 'yes':
        tracks = input("Enter the number of tracks on the album: ")
        print()
        make_album(artist, title, tracks)
    else:
        print()
        make_album(artist, title)

    cont = input("Press 'q' to quit or any other key to add another.")
    if cont.lower() == 'q':
        loop = 0
        break

    
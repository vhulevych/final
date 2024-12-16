songs = input("Enter the songs that you listened with ';' : ")
if ";" and "-" not in songs:
    print("There was an error processing your input. Check format and try once again.")
if ";" in songs:
    count_of_songs_with_symbol = songs.count(";")
    print(f"symbol '{";"}' in user input was {count_of_songs_with_symbol}")
num_of_songs = {count_of_songs_with_symbol} + 1
print(f"You've listened to {num_of_songs} artists!")
single_songs = songs.split(";")
song = {}
for single_songs in songs:
    if song:
        song_count = single_songs.get(song, 0) + 1
most_listened_song = max(single_songs, key=song_count)
print(most_listened_song)







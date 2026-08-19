try: 
    import csv 
    import os
    import intentData as id 
except ImportError:
    print("Please install reccommended dependencies: os, csv.")
    quit()

# CONSTANTS 
SONG_DATASET = "../datasets/songDataset.csv"

    
# Function to add a song to playlist
def add_to_playlist(song_title, playlist_name):
    # Check if the playlist file exists
    playlist_file_path = f"{playlist_name.lower()}_playlist.csv"
    try:
        with open(playlist_file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # Check if the song is already in the playlist
            for row in reader:
                if row and row[0].lower() == song_title.lower():
                    print(f"MusicMan: '{song_title}' is already in the '{playlist_name}' playlist.")
                    return
    except FileNotFoundError:
        print(f"MusicMan: Sorry, the playlist '{playlist_name}' doesn't exist.")
        return
    except Exception as e:
        print(f"MusicMan: An error occurred while checking the playlist.")
        return

    try:
        with open(SONG_DATASET, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            song_found = False
            for row in reader:
                if row['SongTitle'].lower() == song_title.lower():
                    # Append the song to the playlist
                    with open(playlist_file_path, 'a', newline='', encoding='utf-8') as playlist_file:
                        writer = csv.writer(playlist_file)
                        writer.writerow([row['SongTitle'], row['Artist'], row['Album'], row['Genre'], row['Duration']])
                    print(f"MusicMan: '{song_title}' has been added to the '{playlist_name}' playlist.")
                    song_found = True
                    break
            if not song_found:
                print(f"MusicMan: Sorry, I don't have access to '{song_title}'. :()")
    except FileNotFoundError:
        print("MusicMan: Sorry, the song dataset is missing.")
    except Exception:
        print(f"MusicMan: An error occurred while checking the song dataset.")


# Function to delete a song from a playlist
def delete_from_playlist(song_title, playlist_name):
    # Check if the playlist file exists
    playlist_file_path = f"{playlist_name.lower()}_playlist.csv"
    try:
        # Check if the playlist exists
        if not os.path.exists(playlist_file_path):
            print(f"MusicMan: Sorry, the playlist '{playlist_name}' doesn't exist.")
            return

        # Read the existing playlist
        with open(playlist_file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)

        # Check if the song is in the playlist
        song_found = False
        for row in rows:
            if row and row[0].lower() == song_title.lower():
                rows.remove(row)
                song_found = True
                break

        if not song_found:
            print(f"MusicMan: Sorry, '{song_title}' is not in the '{playlist_name}' playlist.")
            return

        # Write the updated playlist
        with open(playlist_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print(f"MusicMan: '{song_title}' has been removed from the '{playlist_name}' playlist.")
    except Exception:
        print(f"MusicMan: An error occurred while deleting the song from the playlist.")
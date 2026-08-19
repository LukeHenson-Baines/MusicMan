try:
    import os 
    import csv 
except ImportError:
    print("Please install reccommended dependencies: os, csv")
    quit()

# Function to delete a playlist
def delete_playlist(playlist_name):
    playlist_file_path = f"{playlist_name.lower()}_playlist.csv"    
    try:
        # Attempt to remove the playlist file
        os.remove(playlist_file_path)
        print(f"MusicMan: Playlist '{playlist_name}' has been successfully deleted.")
    except FileNotFoundError:
        print(f"MusicMan: Sorry, I couldn't find a playlist named '{playlist_name}'.")
    except Exception:
        print(f"MusicMan: An error occurred while deleting the playlist.")

# Function to view a playlist
def view_playlist(playlist_name):
    playlist_file_path = f"{playlist_name.lower()}_playlist.csv"
    
    try:
        with open(playlist_file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print(f"MusicMan: \n{playlist_name.capitalize()}")
            for row in reader:
                song_name = row['SongTitle']
                artist = row['Artist']
                album = row['Album']
                genre = row['Genre']
                duration = row['Duration']
                
                print(f"{song_name} : {artist} : {album} : {genre} : {duration}")
    except FileNotFoundError:
        print(f"MusicMan: Sorry, I couldn't find a playlist named '{playlist_name}'.")
    except Exception:
        print(f"MusicMan: An error occurred while viewing the playlist.")
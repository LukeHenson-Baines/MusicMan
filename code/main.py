# IMPORTS
try:
    import re 
    from nltk.tokenize import word_tokenize

    import intentData as id
    import smallTalk as st
    import nameManagement as nm
    import dateTime as dt
    import questionAnswering as qa 
    import csvUtil as cu
    import classification as cc
    import songChanges as sc 
    import playlistManagement as pm 
except ImportError:
    print("Please install recommended dependencies: csv, nltk, sklearn, re, os.")
    quit()

# Discoverability
def discoverability(userInput):
    inputTok = word_tokenize(userInput)
    for keyword, response in id.DDATA.items():
        if keyword in inputTok:
            return response
    return None

# Basic Text Pre-Processing
def preprocess(userInput):
    userInput = userInput.lower()
    # Remove special characters, leaving only alphanumeric characters and spaces
    userInput = re.sub("[^a-zA-Z0-9\s]", "", userInput)
    return userInput

# Main Loop
if __name__ == "__main__":
    nm.changeName("You")
    greeting = dt.greetingTOD()
    print(f"""
          MusicMan: {greeting} My name is MusicMan, your personal playlist manager! You can ask me to add/
          remove songs, get information about the songs, display your playlist, and lots more. I'm also here to be a virtual
          friend if you need one! If you need to go at any point, just say "bye," and I'll get the message. :)\n """)

    while True:
        userInput = input(f"{nm.getName()}: ")
        userInput = preprocess(userInput)
        if userInput == 'bye':
            break
        if not userInput or userInput.isspace():
            print("MusicMan: Please provide a user input.")
            continue
        else:
            QA = qa.questionAnswering(userInput)
            if QA:
                print(f"MusicMan: {QA}")
            else:
                intent = cc.classifyIntent(userInput)
                if intent == "small_talk":
                    print("MusicMan: " + st.smallTalk(userInput))
                elif intent == "name_inquiry":
                    print("MusicMan: " + nm.nameInquiry(userInput))
                elif intent == "change_name":
                    new_name = input(f"MusicMan: What name would you like to use?\n{nm.getName()}: ")
                    nm.changeName(new_name)
                    print(f"MusicMan: Okay, I've changed your name to {nm.getName()}.")
                elif intent == "current_time":
                    print("MusicMan: " + dt.datetimeHandling("time"))
                elif intent == "current_date":
                    print("MusicMan: " + dt.datetimeHandling("date"))
                elif intent == "discoverability":
                    print("MusicMan: " + discoverability(userInput))
                elif intent == "add_to_playlist":
                    song_title = input(f"MusicMan: Enter the title of the song you want to add to a playlist:\n{nm.getName()}: ")
                    playlist_name = input(f"MusicMan: Enter the name of the playlist where you want to add '{song_title}':\n{nm.getName()}: ")
                    sc.add_to_playlist(song_title, playlist_name)
                elif intent == "remove_from_playlist":
                    song_title = input(f"MusicMan: Enter the title of the song you want to remove from a playlist:\n{nm.getName()}: ")
                    playlist_name = input(f"MusicMan: Enter the name of the playlist where you want to remove '{song_title}':\n{nm.getName()}: ")
                    sc.delete_from_playlist(song_title, playlist_name)
                elif intent == "view_playlist":
                    playlist_name = input(f"MusicMan: Enter the name of the playlist you want to view:\n{nm.getName()}: ")
                    pm.view_playlist(playlist_name)
                elif intent == "make_playlist":
                    print("MusicMan: Sure! What would you like to name your new playlist?")
                    playlist_name = input(f"{nm.getName()}: ").strip()
                    # Confirm user choice
                    print(f"MusicMan: You want to create a playlist named '{playlist_name}'. Is that correct? (Yes/No)")
                    confirm_choice = input(f"{nm.getName()}: ")
                    confirm_choice = preprocess(confirm_choice)
                    if confirm_choice == "yes":
                        cu.create_csv_file(f"{playlist_name}_playlist.csv", ["SongTitle","Artist","Album","Genre","Duration"])
                        print(f"MusicMan: Great! I've created a new playlist named '{playlist_name}'.")
                    else:
                        print("MusicMan: Okay, let me know if you'd like to create a playlist with a different name.")

                elif intent == "delete_playlist":
                    playlist_name = input(f"MusicMan: Enter the name of the playlist you want to delete:\n{nm.getName()}: ")
                    print(f"MusicMan: You want to delete the playlist named '{playlist_name}'. Is that correct? (Yes/No)")
                    confirm_choice = input(f"{nm.getName()}: ")
                    confirm_choice = preprocess(confirm_choice)
                    if confirm_choice == "yes":
                        pm.delete_playlist(playlist_name)
                    else:
                        print("MusicMan: Okay, let me know if you'd like to delete a playlist with a different name.")

                else: #intent = default_class
                    print("MusicMan: I'm sorry, I didn't understand that.")
    print("MusicMan: See ya! :)")
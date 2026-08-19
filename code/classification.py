try: 
    from sklearn.svm import SVC
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.pipeline import make_pipeline

    import intentData as id
except ImportError:
    print("Please install recommended dependencies: sklearn.")  
    quit()

# Intent Classification
def classifyIntent(userInput):
    # Combine all patterns from different intent categories
    all_patterns = []
    all_labels = []

    # Small-Talk
    all_patterns.extend(id.STDATA.keys())
    all_labels.extend(["small_talk"] * len(id.STDATA))

    # Name Inquiry and Change Name
    all_patterns.extend(id.NIDATA + id.CNADATA)
    all_labels.extend(["name_inquiry"] * len(id.NIDATA) + ["change_name"] * len(id.CNADATA))

    # Discoverability
    all_patterns.extend(id.DDATA.keys())
    all_labels.extend(["discoverability"] * len(id.DDATA))

    # Date/Time
    all_patterns.extend(id.CTDATA)
    all_labels.extend(["current_time"] * len(id.CTDATA))

    all_patterns.extend(id.CDDATA)
    all_labels.extend(["current_date"] * len(id.CDDATA))

    # Playlist Management
    all_patterns.extend(id.ADD_TO_PLAYLIST_DATA + id.REMOVE_FROM_PLAYLIST_DATA + id.VIEW_PLAYLIST_DATA + id.MAKE_NEW_PLAYLIST_DATA + id.DELETE_PLAYLIST_DATA)
    all_labels.extend(
        ["add_to_playlist"] * len(id.ADD_TO_PLAYLIST_DATA) +
        ["remove_from_playlist"] * len(id.REMOVE_FROM_PLAYLIST_DATA) +
        ["view_playlist"] * len(id.VIEW_PLAYLIST_DATA) +
        ["make_playlist"] * len(id.MAKE_NEW_PLAYLIST_DATA) +
        ["delete_playlist"] * len(id.DELETE_PLAYLIST_DATA)
    )

    # Add a default class to ensure there are always more than one class
    all_labels.append("default_class")
    all_patterns.append("default_pattern")

    # Create a pipeline with CountVectorizer and SVM
    intent_classifier = make_pipeline(CountVectorizer(), SVC(kernel='linear'))
    
    # Fit the model
    intent_classifier.fit(all_patterns, all_labels)

    # Predict the intent
    predicted_intent = intent_classifier.predict([userInput])[0]
    
    return predicted_intent
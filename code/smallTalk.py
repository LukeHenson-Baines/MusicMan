try: 
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    import intentData as id
except ImportError:
    print("Please install recommended dependency: sklearn")
    quit()
    
# Small-Talk
def smallTalk(userInput):
    # Vectorize the input and small talk data
    vectorizer = TfidfVectorizer(analyzer="word")
    input_vector = vectorizer.fit_transform([userInput])
    stdata_vectors = vectorizer.transform(list(id.STDATA.keys()))

    # Compute cosine similarity between the input and small talk data
    similarities = cosine_similarity(input_vector, stdata_vectors)

    # Find the index of the most similar response
    max_similarity_index = similarities.argmax()

    # Get the response based on the index
    response = list(id.STDATA.values())[max_similarity_index]

    return response
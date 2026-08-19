try: 
    import random
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    import csvUtil as cu 
    import intentData as id
except ImportError:
    print("Please install reccommended dependencies: sklearn, random")
    quit()

# Provided Question Answering Dataset
QA_DATASET = "../datasets/qaDataset.csv"

# Question Answering
def questionAnswering(userInput):
    tfidfVec = TfidfVectorizer(analyzer="word")
    qa_dataset = cu.load_csv(QA_DATASET)
    
    # Check if the input question is in the dataset
    if userInput in (question.lower() for question, _ in qa_dataset):
        matching_questions = [question for question, _ in qa_dataset if userInput == question.lower()]
        inputs = [userInput] + matching_questions
        tfidf_mat = tfidfVec.fit_transform(inputs)
        
        # Compute cosine similarities
        cos_sim = cosine_similarity(tfidf_mat[0], tfidf_mat[1:])
        
        # Set a threshold
        threshold = 0.5
        
        # Find the indices of all occurrences above the threshold
        qa_questions_indices = [i for i, sim in enumerate(cos_sim[0]) if sim >= threshold]
        
        # Make sure indices are unique
        qa_questions_indices = list(set(qa_questions_indices))
        
        # Create a list to store all matching answers
        answers = [ans for i in qa_questions_indices for q, ans in qa_dataset if q == matching_questions[i]]
        
        if answers:
            # Randomly select one of the most similar questions
            selected_answer = random.choice(answers)
            return f"{selected_answer}"
    
    # Provide a default response if the input question is not in the dataset
    return None
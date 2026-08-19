try:
    from nltk.tokenize import word_tokenize
    from nltk.util import ngrams

    import intentData as id 
except ImportError:
    print("Please install recommended dependency: nltk.")
    quit()

# Name Getter 
def getName():
    global name 
    return name 

# Name Management
def changeName(userInput):
    global name
    name = userInput
    return name

# Name Inquiry Function
def nameInquiry(userInput):
    global name 
    inputTok = word_tokenize(userInput)
    inputNGram = list(ngrams(inputTok, 2))
    nameQT = "name"
    for question in id.NIDATA:
        question_tokens = word_tokenize(question.lower())
        question_ngrams = list(ngrams(question_tokens, 2))
        if any(token in inputNGram for token in question_ngrams):
            if nameQT in question:
                return f"MusicMan: Your name is {getName()}. If you want to change it, just ask!"
    return None

# Change Name Request Function
def changeNameRequest(userInput):
    change_name_phrases = ["change my name", "set a new name", "update my name", "switch name"]
    input_ngram = list(ngrams(word_tokenize(userInput), 2))
    name_qt = "name"
    for phrase in change_name_phrases:
        phrase_tokens = word_tokenize(phrase.lower())
        phrase_ngrams = list(ngrams(phrase_tokens, 2))
        if all(token in input_ngram for token in phrase_ngrams) and name_qt in phrase:
            return "MusicMan: Sure! What would you like your new name to be?"
    return None
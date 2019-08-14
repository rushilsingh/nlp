import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer



stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation = dict((ord(character), None) for character in string.punctuation)

def stem(tokens):
    return [stemmer.stem(item) for item in tokens]

def tokenize(text):
    return nltk.word_tokenize(text.lower().translate(remove_punctuation))

def tokenizer(text):
    return stem(tokenize(text))

vectorizer = TfidfVectorizer(tokenizer=tokenizer, stop_words='english')

def similarity(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

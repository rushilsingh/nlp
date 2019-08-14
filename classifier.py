import nltk
nltk.download('movie_reviews')
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
 
def compute_features(words):
    return dict([(word, True) for word in words])
 
def classifier():
    negative_ids = movie_reviews.fileids('neg') 
    positive_ids = movie_reviews.fileids('pos')
    features = [(compute_features(movie_reviews.words(fileids=[ids])), 'neg') for ids in negative_ids] + [(compute_features(movie_reviews.words(fileids=[ids])), 'pos') for ids in positive_ids]
    trained_classifier = NaiveBayesClassifier.train(features)
    return trained_classifier

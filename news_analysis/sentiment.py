from classifier import classifier, compute_features
from similarity import tokenize
import json


Papers = ["TheHindu", "TOI", "TheWire", "IndiaToday"]


def load_article(fname):
    import pickle
    with open(fname, "rb") as f:
        compound_article = pickle.load(f)
    return compound_article


def sentiment(text):
    smap = {"pos": "positive", "neg": "negative"}
    words = tokenize(text)
    features = compute_features(words)
    nb_classifier = classifier()
    return smap[nb_classifier.classify(features)]


def populate_sentiment():
    compound_article = load_article("popular")
    compound_article["Sentiment"] = sentiment(compound_article["Text"])
    for paper in Papers:
        if paper == compound_article["Newspaper"]:
            continue
        if not compound_article[paper]:
            continue
        text = compound_article[paper]["Text"]
        compound_article[paper]["Sentiment"] = sentiment(text)

    with open("popular", "wb") as f:
        import pickle
        pickle.dump(compound_article, f)


def display_results():

    compound_article = load_article("popular")

    print("In newspaper %s, the title of the news article is %s, and the sentiment is %s" % (compound_article["Newspaper"], compound_article["Title"], compound_article["Sentiment"]))
    for paper in Papers:
        if paper == compound_article["Newspaper"]:
            continue
        if not compound_article[paper]:
            continue
        print("In newspaper %s, the title of the news article is %s, and the sentiment is %s" % (paper, compound_article[paper]["Title"], compound_article[paper]["Sentiment"]))

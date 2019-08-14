from agent import Agent
from similarity import similarity
import nltk

nltk.download('punkt')


def build_articles():
    agent = Agent()
    import time
    start = time.time()
    agent.populate()
    end = time.time() - start
    print("Took", b)

    articles = {}

    for paper in agent.papers:
        articles[paper.title] = agent.articles[paper.title]
    return articles

def store_data(fname, data):
    import pickle
    with open(fname, "wb") as f:
        pickle.dump(data, f)
      

def store_news_data():
    
    articles = build_articles()
    store_data("data", articles)

def load_news_articles():
    articles = load_data("data")
    return articles

def load_data(fname):
    import pickle
    with open(fname, "rb") as f:
        data = pickle.load(f)
    return data



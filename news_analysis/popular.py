from similarity import similarity
import nltk
from store import load_news_articles

THRESHOLD = 0.4

def same(a1,a2):
    
    return similarity(a1["Text"], a2["Text"]) > 0.4

def same_pairs(list1, list2):
    
    pairs = []
    for a1 in list1:
        local = 0
        for a2 in list2:
            if a2["Newspaper"] in a1 and a1[a2["Newspaper"]]:
                continue
            if a1["Newspaper"] in a2 and a2[a1["Newspaper"]]:
                continue
            if same(a1,a2):
                a1["Count"] += 1
                a2["Count"] += 1
                a1[a2["Newspaper"]] = a2
                a2[a1["Newspaper"]] = a1
            else:
                a1[a2["Newspaper"]] = None
                a2[a1["Newspaper"]] = None


def populate_counts():


    articles = load_news_articles()
    for paper, article_list in articles.items():
            for article in article_list:
                    article["Count"] = 0


    same_pairs(articles["TheHindu"], articles["TOI"])
    same_pairs(articles["TheHindu"], articles["TheWire"])
    same_pairs(articles["TheHindu"], articles["IndiaToday"])
    same_pairs(articles["TOI"], articles["TheWire"])
    same_pairs(articles["TOI"], articles["IndiaToday"])
    same_pairs(articles["TheWire"], articles["IndiaToday"])
    
    counted_articles = []
    for key, alist in articles.items():
        counted_articles.extend(alist)

    import pickle
    with open("counted", "wb") as f:
        pickle.dump(counted_articles, f)

def load_counted_articles():   
        import pickle
        with open("counted", "rb") as f:
            articles = pickle.load(f)
        return articles

def popular():

    articles = load_counted_articles()
    max_count = 0
    popular = None
    for article in articles:
        if article["Count"] > max_count:
            max_count = article["Count"]
            popular = article
    
    import pickle
    with open("popular", "wb") as f:
            pickle.dump(popular, f)
    return popular

def determine_popular_article():
    import time
    start = time.time()
    article = popular()
    print("Popular article", article["Title"])
    print("Score(0-3)", article["Count"])
    end = time.time() - start
    return article
    
    

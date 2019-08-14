from newspapers import TheHindu, TOI, TheWire, IndiaToday
import nltk



class Agent:

    def __init__(self):
        hindu = TheHindu()
        toi = TOI()
        wire = TheWire()
        it = IndiaToday()
        self.papers = [hindu, toi, wire, it]
        self.articles = {}

    def populate(self):

        [paper.crawl() for paper in self.papers]

        for paper in self.papers:
            self.articles[paper.title] = paper.parse_articles(paper.articles)



        


      
            

    



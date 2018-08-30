import requests
from bs4 import BeautifulSoup


VISITED = []

class Newspaper(object):

    def __init__(self, url, restrict=[], discard=[], include=[]):

        self.title = "Newspaper" 

        self.discard = discard
        self.restrict = restrict
        self.include = include
        self.url = url
        self.alt_url = self.flip(url)
        

        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        self.links = []
        self.articles = {}

        for link in soup.find_all('a'):
            link = link.get('href')
            if link is None:
                continue
            if link.startswith("/http"):
                link = link.replace("/", "", 1)
            if link.startswith("/"):
                link = link.replace("/", self.url, 1)
            if self.is_valid(link):
                self.links.append(link)
        VISITED.append(self.url)
        VISITED.append(self.alt_url)

    def flip(self, url):
        if type(url) is not str: 
            return url
        if url.startswith("https"):
            flipped = url.replace("https", "http", 1)
        else:
            flipped = url.replace("http", "https", 1)

        return flipped


    def is_valid(self, link):

        check = type(link) is str and link not in VISITED
        if not check:
            return False

        for url in self.discard:
            if link.startswith(url):
                return False

        for url in self.include:
            if link.startswith(url):
                return True
        check = (link.startswith(self.url) or link.startswith(self.alt_url))
        if not check:
            return False
        else:
            if not self.restrict:
                return True
            check = False
            for url in self.restrict:
                check = link.startswith(url) or link.startswith(self.flip(url))
                if check:
                    return True
        return False


    def step(self):
        if not self.links:
            return None, None
        link = self.links.pop()
        if link.startswith("/http"):
            link = link.replace("/", "", 1)
        elif link.startswith("/"):
            link = link.replace("/", self.url, 1)
        if self.is_valid(link):
            print("LINK", link)
            VISITED.append(link)
            VISITED.append(self.flip(link))
            data = requests.get(link).text
            return data, link
        return None, None

    def crawl(self):

        while True:
            self.step()
            if not self.links: break

    def parse_articles(self, articles):
        
        from newspaper import Article

        article_list = []
        for url, data in articles.items():
            try:
                article_obj = Article('')
                article_obj.set_html(data)
                article_obj.parse()
                article = {}
                article["Newspaper"] = self.title
                article["Url"] = url
                article["Data"] = data
                article["Title"] = article_obj.title
                article["Text"] = article_obj.text
                article_list.append(article)

                print("Article", article["Title"])
            except Exception as e:
                print(e)
                print("Parsing failed. Ignoring article")

        return article_list

    def normalize_article(self, article):
        if "Data" in article:
            del article["Data"]
        if "Obj" in article:
            del article["Obj"]

        return article


class TheHindu(Newspaper):

    def __init__(self):
        super(TheHindu, self).__init__("https://www.thehindu.com/news", restrict=["https://www.thehindu.com/news/national", "https://www.thehindu.com/news/international"])
        self.title = "TheHindu"

    def step(self):
        data, link = super(TheHindu, self).step()
        if not data:
            return
        else:
            if '"@type": "NewsArticle"' in data:
                self.articles[link] = data
            else:
                soup = BeautifulSoup(data, 'html.parser')

                for link in soup.find_all('a'):
                    link = link.get('href')
                    if self.is_valid(link):
                        self.links.append(link)


    def is_valid(self, link):
       
        check = super(TheHindu, self).is_valid(link)
        if not check:
            return False
        else:
            import re
            pattern = re.compile(".*page=(\d+)")
            match = pattern.match(link)
            if match:
                number = int(match.groups()[0])
                if number>1:
                    return False
        return True

class TOI(Newspaper):

    def __init__(self):
        super(TOI, self).__init__("https://timesofindia.indiatimes.com", restrict=["https://timesofindia.indiatimes.com/india", "https://timesofindia.india.com/world"])
        self.title = "TOI"

    def step(self):
        data, link = super(TOI, self).step()
        if not data:
            return

        if "articleshow" in link:
            self.articles[link] = data
        else:
            soup = BeautifulSoup(data, 'html.parser')
            for link in soup.find_all('a'):
                link = link.get('href')
                if self.is_valid(link):
                    self.links.append(link)

class TheWire(Newspaper):

    def __init__(self):
        super(TheWire, self).__init__("https://thewire.in/")
        self.title = "TheWire"

    def step(self):
        data, link = super(TheWire, self).step()
        if not data:
            return
        if '"@type": "NewsArticle"' in data:
            self.articles[link] = data
        else:
            soup = BeautifulSoup(data, 'html.parser')
            for link in soup.find_all('a'):
                link = link.get('href')
                if self.is_valid(link):
                    self.links.append(link)

class IndiaToday(Newspaper):

    def __init__(self):
        super(IndiaToday, self).__init__("https://www.indiatoday.in/", 
                                         discard=["https://www.indiatoday.in/video",
                                                  "https://www.indiatoday.in/photo",
                                                  "https://www.indiatoday.in/programme",
                                                  "https://www.indiatoday.in/auto",
                                                  "https://www.indiatoday.in/television",
                                                  "https://www.indiatoday.in/movies",
                                                  "https://www.indiatoday.in/sports",
                                                  "https://www.indiatoday.in/travel",
                                                  "https://www.indiatoday.in/lifestyle"])
        self.title = "IndiaToday"

    def step(self):
        data, link = super(IndiaToday, self).step()
        if not data:
            return
        if '/story/' in link:
            self.articles[link] = data
        else:
            soup = BeautifulSoup(data, 'html.parser')
            for link in soup.find_all('a'):
                link = link.get('href')
                if self.is_valid(link):
                    self.links.append(link)




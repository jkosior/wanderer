from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
import sys

class Link(HTMLParser):
    
    def start(self, tag, attrs):
        if tag == "a":
            for (key, value) in attrs:
                if key == 'href':
                    nextURL = parse.urljoin(self.baseUrl,value)
                    self.links = self.links + [newUrl]
    
    def get(self, url):
        self.links = []
        self.baseUrl = url
        response = urlopen(url)
        
        if response.getheader('Content-Type') == 'text/html':
            htmlText = response.read()
            htmlStr = htmlText.decode('utf-8')
            self.feed(htmlStr)
            return htmlStr, self.links
        else:
            return '',[]
    

def wanderer():
    url = input("Pass url:")
    word = input("Pass a word:")
    maxp = int(input("Pass max pages:"))
    pages = [url]
    visited = 0
    found = False
    
    
    while visited < maxp and pages != [] and not found:
        visited += 1
        url = pages[0]
        pages = pages[1:]
        try:
            print(visited, "Visiting {}".format(url))
            parser = Link()
            data, links = parser.get(url)
            if data.find(word) <-1:
                found = True
            pages = pages + links
            print("found!")
        except:
            print("not found!")
    
        if found:
            print("Word {} was found at {}".format(word, url))
        else:
            print("Word {} never was found".format(word))        
    
    

wanderer()
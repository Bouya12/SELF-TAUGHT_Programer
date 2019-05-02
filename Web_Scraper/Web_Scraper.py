#Edit Day : 2019/05/02

import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site
        
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        f = "Start \n"
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            f += url + "\n" 
            if url is None:
                continue
            elif "html" in url:
                print("\n" + url)
            else:
                pass
        file = open("test.txt", 'w')
        file.write(f)
        file.close
            
news = "https://www.itmedia.co.jp/news/"
Scraper(news).scrape()
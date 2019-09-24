import requests
import json
from bs4 import BeautifulSoup
from parse import *
import time

class Main:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = 'https://www.reddit.com/r/AskReddit/top/?t=all'
        self.session = requests.Session()
        self.session.headers.update({'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'})
        self.pages = int(input("Pages to Scrape: "))
    
    def scrapedata(self):
        time.sleep(3)
        response = self.session.get(self.url)
        soup = BeautifulSoup(response.text,'html.parser')
        script = soup.find('script',{'id':'data'})
        script = script.text
        begin = 14

        lend = script.rfind('; window.___prefetches ')

        script = script[begin:lend]
        jdata  = json.loads(script)
        parsepage(jdata)

        self.url = soup.find('link',{'rel':'next'}).get('href')
        
 
def run():
    ts = Main()

    while(ts.pages > 0):
        print("Scraping :",ts.url)
        print('Pages left to Scrape {}'.format(ts.pages))
        ts.scrapedata()
        ts.pages= ts.pages - 1 
        print("Page Scraped , Manual Delay to avoid block")
        for t in range(5):
            print("{} seconds".format(t))
            time.sleep(1)
        
run()
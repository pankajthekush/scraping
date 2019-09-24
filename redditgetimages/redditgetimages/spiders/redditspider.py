# -*- coding: utf-8 -*-
import scrapy
import json
from redditgetimages.items import RedditgetimagesItem
from bs4 import BeautifulSoup
import time
from scrapy import signals
from HelpingMods import HelpingModules

class RedditspiderSpider(scrapy.Spider):
    name = 'redditspider'
    allowed_domains = ['web']
    start_urls = ['https://www.reddit.com/r/calvinandhobbes/']


    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(RedditspiderSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_opened, signals.spider_opened)
        crawler.signals.connect(spider.spider_closed, signals.spider_closed)
        return spider

    def spider_opened(self, spider):
        print('Opening {} spider'.format(spider.name))

    def spider_closed(self, spider):
        print("Download Complete , Uploading")
        time.sleep(2)
        hp = HelpingModules()
        hp.makearchive()
        time.sleep(2)
        hp.gdriveupload()
        print("Upload Complete..")
        

    def parse(self, response):
        item =  RedditgetimagesItem()
        script = response.xpath('//script[@id="data"]/text()').extract()
        script = script[0]
        script = script[14:script.rfind('; window.___prefetches ')]
        jdata = json.loads(script)
        jposts = jdata['posts']['models']

        postdata = [v for k,v in jposts.items()]
        urldata = []

        for u in postdata:

            kmedia = (u.get('media'))
            if kmedia is not None:
                contenturl = kmedia.get('content')
                if contenturl is not None:
                    urldata.append(contenturl)
        

        item['image_urls'] = urldata
        
        soup = BeautifulSoup(response.text,"html.parser")
        nextlink = soup.find('link',{'rel':'next'}).get('href')
        yield item

        if nextlink:
            time.sleep(2)
            yield scrapy.Request(nextlink,callback=self.parse,dont_filter = True)
           

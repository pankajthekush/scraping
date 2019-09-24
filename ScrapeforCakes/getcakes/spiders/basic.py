# -*- coding: utf-8 -*-
import scrapy
import json
import csv
import os
from getcakes.items import GetcakesItem
class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls =  ['https://www.fnp.com/pl/cakes/noida?category_id=cakes%2Fnoida&pageType=category&FNP_CURRENT_CATALOG_ID=india&viewIndex={0}&viewSize=60&sortFields=SEQUENCE_NUM_cakes%2Fnoida%7CASC&format=json'.format(i) for i in range(5)]

    
    def parse(self, response):
        jdata = json.loads(response.text)
        productdata = jdata['productResults']
        fileexits = os.path.isfile('cake.csv')
        keys = productdata[0].keys()
        with open('cake.csv','a',encoding='utf8',newline='') as outputcsv:
            dict_writer = csv.DictWriter(outputcsv,keys)

            if not fileexits:
                dict_writer.writeheader()
            dict_writer.writerows(productdata)
        item = GetcakesItem()
        item['jsonresponse'] = response.text
        return item

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GetcakesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jsonresponse = scrapy.Field()
    # price = scrapy.Field()
    # reviews = scrapy.Field()
    # image_url = scrapy.Field

    # images = scrapy.Field()


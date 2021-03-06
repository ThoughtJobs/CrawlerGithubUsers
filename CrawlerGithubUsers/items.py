# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GitUsersItem(scrapy.Item):
    # define the fields for your item here like:
    username = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    email = scrapy.Field()
    followers = scrapy.Field()
    company = scrapy.Field()
    hireable = scrapy.Field()
    created_at = scrapy.Field()
    product = scrapy.Field()

    pass

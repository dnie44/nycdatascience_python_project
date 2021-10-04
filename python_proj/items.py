# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TV_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tv_category = scrapy.Field()
    category_id = scrapy.Field()
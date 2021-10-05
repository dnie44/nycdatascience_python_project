# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TV_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    top_class = scrapy.Field()
    sub_class = scrapy.Field()
    tv_name = scrapy.Field()
    manufacturer = scrapy.Field()
    color = scrapy.Field()
    customerReviewAverage = scrapy.Field()
    customerReviewCount = scrapy.Field()
    features = scrapy.Field()               # features is a nested dictionary from Bestbuy API pull
    modelNumber = scrapy.Field()
    regularPrice = scrapy.Field()
    salePrice = scrapy.Field()
    sku = scrapy.Field()
    longDescription = scrapy.Field()
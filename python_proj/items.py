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
    # TV Features is a nested dictionary, max of 8
    feat1 = scrapy.Field()
    feat2 = scrapy.Field()
    feat3 = scrapy.Field()
    feat4 = scrapy.Field()
    feat5 = scrapy.Field()
    feat6 = scrapy.Field()
    feat7 = scrapy.Field()
    feat8 = scrapy.Field()
    modelNumber = scrapy.Field()
    regularPrice = scrapy.Field()
    salePrice = scrapy.Field()
    sku = scrapy.Field()
    longDescription = scrapy.Field()
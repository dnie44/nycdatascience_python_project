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
    review_average = scrapy.Field()
    review_count = scrapy.Field()
    # TV Features is a nested dictionary, max of 8
    feat1 = scrapy.Field()
    feat2 = scrapy.Field()
    feat3 = scrapy.Field()
    feat4 = scrapy.Field()
    feat5 = scrapy.Field()
    feat6 = scrapy.Field()
    feat7 = scrapy.Field()
    feat8 = scrapy.Field()
    model_num = scrapy.Field()
    regular_px = scrapy.Field()
    sale_px = scrapy.Field()
    sku = scrapy.Field()
    long_desc = scrapy.Field()
    store_avail = scrapy.Field()
    online_avail = scrapy.Field()
    screen_size = scrapy.Field()
    curved = scrapy.Field()     # yes or no
    resolution = scrapy.Field()
    warranty = scrapy.Field()   # Warranty years
    energy_eff = scrapy.Field() # Estimated Annual Electricity Use
    display_type = scrapy.Field() #LED, OLED, etc
    model_year = scrapy.Field()
    brightness = scrapy.Field() # in candela per sq meter
    width = scrapy.Field()
    height_nostand = scrapy.Field() # height without stand
    weight_nostand = scrapy.Field() # weight without stand
    smart_capable = scrapy.Field()
    refresh_rate = scrapy.Field()
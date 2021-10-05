import scrapy
import json
# from scrapy.loader import ItemLoader
from python_proj.items import TV_Item
from python_proj.spiders.myAPIkey import getkey

myAPIkey = getkey()                             # load in my API key
bb_category = '(categoryPath.id=abcat0101000)'  # category id for TV & Home Theater (from Bestbuy's API documentation)
sort = 'customerReviewAverage.dsc'              # sort by setting
psize = 'pageSize=100'                          # set # of results per API get (max 100)
attribs = [
    'class',
    'subclass',
    'name',
    'manufacturer',
    'color',
    'customerReviewAverage',
    'customerReviewCount',
    'features.feature',
    'modelNumber',
    'regularPrice',
    'salePrice',
    'sku',
    'longDescription'
]                                               # list of desired TV data
attrib_query = ','.join(attribs)                # join desired data into url string

# initialize the TV item
tv_item = TV_Item()

class BBSpider(scrapy.Spider):
    name = 'bb_spider'
    allowed_domains = ['api.bestbuy.com/']
    #start_urls = [f'https://api.bestbuy.com/v1/products/mostViewed(categoryId=abcat0101000)?apiKey={myAPIkey}']
    #start_urls = [f'https://api.bestbuy.com/v1/categories(id=abcat*)?apiKey={myAPIkey}&show=id,name&format=json']
    #start_urls = [f'https://api.bestbuy.com/v1/{bb_category}?apiKey={myAPIkey}&{psize}&show=subCategories.name,subCategories.id&format=json']
    start_urls = [f'https://api.bestbuy.com/v1/products({bb_category})?apiKey={myAPIkey}&sort={sort}&show={attrib_query}&{psize}&page=2&format=json']

    def parse(self, response):
        res = json.loads(response.body)
        print(res['products'])
        for each in res['products']:
            tv_item['top_class'] = each['class']
            tv_item['sub_class'] = each['subclass']
            tv_item['tv_name'] = each['name']
            tv_item['manufacturer'] = each['manufacturer']
            tv_item['color'] = each['color']
            tv_item['customerReviewAverage'] = each['customerReviewAverage']
            tv_item['customerReviewCount'] = each['customerReviewCount']
            tv_item['features'] = each['features']
            tv_item['modelNumber'] = each['modelNumber']
            tv_item['regularPrice'] = each['regularPrice']
            tv_item['salePrice'] = each['salePrice']
            tv_item['sku'] = each['sku']
            tv_item['longDescription'] = each['longDescription']
            
            yield tv_item
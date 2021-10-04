import scrapy
import json
# from scrapy.loader import ItemLoader
from python_proj.items import TV_Item
from python_proj.spiders.myAPIkey import getkey

# initialize the TV item
tv_item = TV_Item()

myAPIkey = getkey()                             # load in my API key
bb_category = 'categories(id=abcat0101000)'        # category id for TVs (from Bestbuy's API documentation)
psize = 'pageSize=100'                          # set # of results per API get

class BBSpider(scrapy.Spider):
    name = 'bb_spider'
    allowed_domains = ['api.bestbuy.com/']
    #start_urls = [f'https://api.bestbuy.com/v1/products/mostViewed(categoryId=abcat0101000)?apiKey={myAPIkey}']
    #start_urls = [f'https://api.bestbuy.com/v1/categories(id=abcat*)?apiKey={myAPIkey}&show=id,name&format=json']
    start_urls = [f'https://api.bestbuy.com/v1/{bb_category}?apiKey={myAPIkey}&{psize}&show=subCategories.name,subCategories.id&format=json']

    def parse(self, response):
        #print(response.body)
        resp = json.loads(response.body)
        for eachrow in resp["categories"][0]['subCategories']:
            cat = eachrow['name']
            cat_id = eachrow['id']

            tv_item['tv_category'] = cat
            tv_item['category_id'] = cat_id
            yield tv_item
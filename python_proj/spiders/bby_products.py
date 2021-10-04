import scrapy
import json
from python_proj.spiders.myAPIkey import getkey

myAPIkey = getkey()

class BbyProductsSpider(scrapy.Spider):
    name = 'bby_products'
    allowed_domains = ['api.bestbuy.com/']
    #start_urls = [f'https://api.bestbuy.com/v1/products/mostViewed(categoryId=abcat0101000)?apiKey={myAPIkey}']
    #start_urls = [f'https://api.bestbuy.com/v1/categories(id=abcat*)?apiKey={myAPIkey}&show=id,name&format=json']
    start_urls = [f'https://api.bestbuy.com/v1/categories(id=abcat0101000)?apiKey={myAPIkey}&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json']

    def parse(self, response):
        #print(response.body)
        resp = json.loads(response.body)
        for each in resp["categories"][0]['subCategories']:
            print(each)
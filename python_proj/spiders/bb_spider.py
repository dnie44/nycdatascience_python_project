import scrapy
import json
# from scrapy.loader import ItemLoader
from python_proj.items import TV_Item
from python_proj.spiders.myAPIkey import getkey

myAPIkey = getkey()                             # load in my API key
bb_category = '(categoryPath.id=abcat0101000)'  # category id for TV & Home Theater (from Bestbuy's API documentation)
sort = 'customerReviewAverage.dsc'              # sort by setting
psize = 'pageSize=100'                          # set # of results per API get (max 100)
attributes = [
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
attrib_query = ','.join(attributes)                # join desired data into url string

def remove_linebreak(s):
    return ' '.join(s.split('\n'))

# initialize the TV item
tv_item = TV_Item()

# set beginning API url
url_head = f'https://api.bestbuy.com/v1/products({bb_category})?apiKey={myAPIkey}&sort={sort}&show={attrib_query}&{psize}'

class BBSpider(scrapy.Spider):
    name = 'bb_spider'
    allowed_domains = ['api.bestbuy.com/']
    #start_urls = [f'{url_head}&page=2&format=json']

    def start_requests(self):
        for i in range(1,6):
            yield scrapy.Request(url=f'{url_head}&page={str(i)}&format=json',callback = self.parse)

    def parse(self, response):
        res = json.loads(response.body)
        print(res['products'])
        for attrib in res['products']:
            tv_item['top_class'] = attrib['class']
            tv_item['sub_class'] = attrib['subclass']
            tv_item['tv_name'] = attrib['name']
            tv_item['manufacturer'] = attrib['manufacturer']
            tv_item['color'] = attrib['color']
            tv_item['customerReviewAverage'] = attrib['customerReviewAverage']
            tv_item['customerReviewCount'] = attrib['customerReviewCount']
            # Nested features.feature needs iteration
            for idx in range(8):
                try: 
                    tv_item['feat'+str(idx+1)] = remove_linebreak(attrib['features'][idx]['feature'])
                except:
                    tv_item['feat'+str(idx+1)] = ''

            tv_item['modelNumber'] = attrib['modelNumber']
            tv_item['regularPrice'] = attrib['regularPrice']
            tv_item['salePrice'] = attrib['salePrice']
            tv_item['sku'] = attrib['sku']
            tv_item['longDescription'] = attrib['longDescription']
            
            yield tv_item
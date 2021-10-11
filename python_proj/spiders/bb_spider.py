import scrapy
import json
# from scrapy.loader import ItemLoader
from python_proj.items import TV_Item
from python_proj.spiders.myAPIkey import getkey

myAPIkey = getkey()                             # load in my API key
bb_category = '(categoryPath.id=abcat0101000)'  # category id for TV & Home Theater (from Bestbuy's API documentation)
sort = 'customerReviewAverage.dsc'              # sort by setting
psize = 'pageSize=100'                         # set # of results per API get (max 100)
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
    'longDescription',
    'inStoreAvailability',
    'onlineAvailability',
    'details.value'
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
        #print(res)
        print(res['products'])
        for attrib in res['products']:
            tv_item['top_class'] = attrib['class']
            tv_item['sub_class'] = attrib['subclass']
            tv_item['tv_name'] = attrib['name']
            tv_item['manufacturer'] = attrib['manufacturer']
            tv_item['color'] = attrib['color']
            tv_item['review_average'] = attrib['customerReviewAverage']
            tv_item['review_count'] = attrib['customerReviewCount']
            # Nested features.feature needs iteration, max of 8 features
            for idx in range(8):
                try: 
                    tv_item['feat'+str(idx+1)] = remove_linebreak(attrib['features'][idx]['feature'])
                except:
                    tv_item['feat'+str(idx+1)] = ''

            tv_item['model_num'] = attrib['modelNumber']
            tv_item['regular_px'] = attrib['regularPrice']
            tv_item['sale_px'] = attrib['salePrice']
            tv_item['sku'] = attrib['sku']
            tv_item['long_desc'] = attrib['longDescription']
            tv_item['store_avail'] = attrib['inStoreAvailability']
            tv_item['online_avail'] = attrib['onlineAvailability']
            # Nested details.values needs iteration & checks
            attrib_dets = attrib['details']              # response item
            num_dets = len(attrib['details'])       # number of different details
            det_match = {
                'screen_size':'Screen Size Class',
                'curved':'Curved Screen',
                'resolution':'Resolution',
                'warranty':"Manufacturer's Warranty - Parts",
                'energy_eff':'Estimated Annual Electricity Use',
                'display_type':'Display Type',
                'model_year':'Model Year',
                'brightness':'Brightness',
                'width':'Product Width',
                'height_nostand':'Product Height Without Stand',
                'weight_nostand':'Product Weight Without Stand',
                'smart_capable':'Smart Capable',
                'refresh_rate':'Refresh Rate'
            }
            
            for item, pull in det_match.items():
                tmp = [attrib_dets[i]['value'] for i in range(num_dets) if attrib_dets[i]['name']==pull]
                tv_item[item] = tmp[0] if tmp else ''

            yield tv_item
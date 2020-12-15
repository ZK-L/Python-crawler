# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import requests 
from myCrawler.settings import IMAGES_STORE

header = {'Referer': 'www.mzitu.com',
            'USER-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Cookie': 'Hm_lvt_cb7f29be3c304cd3bb0c65a4faa96c30=1607914702,1607917701,1607920724; Hm_lpvt_cb7f29be3c304cd3bb0c65a4faa96c30=1607934612'
        }

class imagCrawlerPipeline(object):
    def process_item(self, item, spider):
        
        for img, title in zip(item['img_src'], item['file_name']):
            path = os.path.join(IMAGES_STORE, title)
            if not os.path.exists(path):
                os.makedirs(path)
            
            with open('{}//{}.jpg'.format(path,img[-10:-4]),'wb') as f:
                req = requests.get(img, headers = header)
                f.write(req.content)
        

        return item
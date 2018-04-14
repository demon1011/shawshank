# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class DoubanscrapyPipeline(object):
    def process_item(self, item, spider):
    	
    	with open('/home/darren/PycharmProjects/doubanScrapy-master/doubanScrapy/spiders/rawdata/'+item['movie_name']+'.json', 'at') as f:
    		f.write(item['comment_content'].strip()+'\n')
        # return item



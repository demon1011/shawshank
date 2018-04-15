from scrapy import Request, Spider
from doubanScrapy.items import DoubanscrapyItem 

class ShawScrapy(Spider):
	"""Comment of all movies"""
	name = 'google'
	# 爬虫起始url
	start_urls = ["https://www.google.com"]

	def start_request(self):
		yield Request(self.start_urls, callback = self.parse)

	
	def parse(self,response):
		view(response)

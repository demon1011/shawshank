from scrapy import Request, Spider
from doubanScrapy.items import DoubanscrapyItem 

class ShawScrapy(Spider):
	"""Comment of Shawshank"""
	name = 'shaw'
	# 爬虫起始url
	start_urls = ["https://movie.douban.com/subject/1292052/reviews"]

	def start_request(self):
		yield Request(self.start_urls, callback = self.parse)

	def parse(self, response):
		for msg in response.xpath('//div[@class="main-bd"]'):
			review_page=msg.xpath('h2/a/@href').extract()[0]
			if review_page:				
				yield Request(review_page,callback=self.parse_download)
				
	
	def parse_download(self,response):
		item = DoubanscrapyItem()
		item['comment_name']=response.url
		content =response.xpath('//div[@id="link-report"]/div[@property="v:description"]/descendant::text()').extract()      		
		if content:
			item['comment_content']=''.join(content)
		yield item

			
		#获取当前url的下一页链接	
		'''next_page = response.xpath('//span[@class="next"]/a/@href').extract_first()

		if next_page:
			request_url = response.urljoin(next_page)
			yield Request(request_url, callback = self.parse)'''
    
		

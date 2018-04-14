# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html


def spider_opened(self, spider):
	spider.logger.info('Spider opened: %s' % spider.name)

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
# from scrapy_djangoitem import DjangoItem
# from core.models import row_news

# call model meta 
class SpiderItem(scrapy.Item):
	id = scrapy.Field()
	title = scrapy.Field()
	datetime = scrapy.Field()
	author = scrapy.Field()
	content = scrapy.Field()
	url = scrapy.Field()

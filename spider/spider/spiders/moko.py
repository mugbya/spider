# -*- coding: utf-8 -*-
import scrapy

from spider.items import SpiderItem 

class MokoSpider(scrapy.Spider):
    name = "moko"
    allowed_domains = ["moko.cc"]
    start_urls = (
        'http://www.moko.cc/',
    )

    def parse(self, response):
        for divs in response.xpath('//div[@class="cover"]'):
            img_url = divs.xpath('.//img/@src2').extract()[0]
            urlItem = MokoItem()
            urlItem['url'] = img_url.encode('utf-8')
            yield urlItem

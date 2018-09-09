# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem

class WhhanspiderSpider(scrapy.Spider):
    name = "whHanSpider"
    allowed_domains = ["tianqi.com"]
    citys = ['wuhan','shanghai']
    start_urls = []

    for city in citys:
        start_urls.append('http://'+city+'.tianqi.com/')



    def parse(self, response):
        subSelector = response.xpath('//dl[@class="weather_info"]')

        items = []
        for sub in subSelector:

            item = WeatherItem()
            
            item['name'] = sub.xpath('/dd[@class="name"]/h2/text()').extract()[0]
            item['week'] = sub.xpath('/dd[@class="week"]/text()').extract()[0]
            item['weather'] = sub.xpath('/dd[@class="weather"]/p/b/text()').extract()[0]
            item['shidu'] = sub.xpath('/dd[@class="shidu"]/b/text()').extract()[0]
            item['kongqi'] = sub.xpath('/dd[@class="kongqi"]/h6/text()').extract()[0]
            items.append(item)
        return items

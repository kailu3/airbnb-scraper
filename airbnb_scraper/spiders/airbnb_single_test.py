# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import CloseSpider
import json
import time
from scrapy_splash import SplashRequest
# NEED TO RUN SCRAPY SPLASH ON DOCKER TO RUN!!!
class AirbnbSpider(scrapy.Spider):
    name = 'airbnb_single_test'
    
    def start_requests(self):
        url = 'https://www.airbnb.com/rooms/10823831'
        yield SplashRequest(url=url,
         callback=self.parse_id, endpoint = "render.html", args={'wait': '0.5'})
    
    def parse_id(self, response):          
        _file = "sample_listing.html"
        with open(_file, 'wb') as f:
            f.write(response.body)
            
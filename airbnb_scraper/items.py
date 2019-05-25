# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirbnbScraperItem(scrapy.Item):

    # Host Fields
    host_languages = scrapy.Field()
    is_superhost = scrapy.Field()
    host_id = scrapy.Field()

    # Room Fields
    price = scrapy.Field()
    url = scrapy.Field()
    is_business_travel_ready = scrapy.Field()
    is_fully_refundable = scrapy.Field()
    is_new_listing = scrapy.Field()
    lat = scrapy.Field()
    lng = scrapy.Field()
    localized_city = scrapy.Field()
    localized_neighborhood = scrapy.Field()
    listing_name = scrapy.Field()
    person_capacity = scrapy.Field()
    picture_count = scrapy.Field()
    reviews_count = scrapy.Field()
    room_type_category = scrapy.Field()
    star_rating = scrapy.Field() # Rounded to .5 or .0 Avg Rating
    avg_rating = scrapy.Field()
    can_instant_book = scrapy.Field()
    monthly_price_factor = scrapy.Field()
    currency = scrapy.Field()
    amt_w_service = scrapy.Field()
    rate_type = scrapy.Field()
    weekly_price_factor = scrapy.Field()
    bathrooms = scrapy.Field()
    bedrooms = scrapy.Field()






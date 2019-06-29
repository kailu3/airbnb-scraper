# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import CloseSpider
import json
import time
import pprint
import collections

with open('data.json', 'r') as file:
    data = json.load(file)

# Need Try/Catch for first page as sometimes has airbnb plus
 
#homes = data.get('explore_tabs')[0].get('sections')[0].get('listings')

#if homes is None:
homes = data.get('explore_tabs')[0].get('sections')[3].get('listings')

print(homes)
# data_dict = collections.defaultdict(dict)

# base_url = 'https://www.airbnb.com/rooms/'
# for home in homes:
#     room_id = str(home.get('listing').get('id'))
#     url = base_url + str(home.get('listing').get('id'))

#     # Map price for specific home to each url
#     data_dict[room_id]['url'] = url
#     data_dict[room_id]['price'] = home.get('pricing_quote').get('rate').get('amount')
#     data_dict[room_id]['bathrooms'] = home.get('listing').get('bathrooms')

#     # Copy below
#     data_dict[room_id]['bedrooms'] = home.get('listing').get('bedrooms')
#     data_dict[room_id]['host_languages'] = home.get('listing').get('host_languages')
#     data_dict[room_id]['is_business_travel_ready'] = home.get('listing').get('is_business_travel_ready')
#     data_dict[room_id]['is_fully_refundable'] = home.get('listing').get('is_fully_refundable')
#     data_dict[room_id]['is_new_listing'] = home.get('listing').get('is_new_listing')
#     data_dict[room_id]['is_superhost'] = home.get('listing').get('is_superhost')
#     data_dict[room_id]['lat'] = home.get('listing').get('lat')
#     data_dict[room_id]['lng'] = home.get('listing').get('lng')
#     data_dict[room_id]['localized_city'] = home.get('listing').get('localized_city')
#     data_dict[room_id]['localized_neighborhood'] = home.get('listing').get('localized_neighborhood')
#     data_dict[room_id]['listing_name'] = home.get('listing').get('name')
#     data_dict[room_id]['person_capacity'] = home.get('listing').get('person_capacity')
#     data_dict[room_id]['picture_count'] = home.get('listing').get('picture_count')
#     data_dict[room_id]['reviews_count'] = home.get('listing').get('reviews_count')
#     data_dict[room_id]['room_type_category'] = home.get('listing').get('room_type_category')
#     data_dict[room_id]['star_rating'] = home.get('listing').get('star_rating')
#     data_dict[room_id]['host_id'] = home.get('listing').get('user').get('id')
#     data_dict[room_id]['avg_rating'] = home.get('listing').get('avg_rating')


#     data_dict[room_id]['can_instant_book'] = home.get('pricing_quote').get('can_instant_book')
#     data_dict[room_id]['monthly_price_factor'] = home.get('pricing_quote').get('monthly_price_factor')
#     data_dict[room_id]['currency'] = home.get('pricing_quote').get('rate').get('currency')
#     data_dict[room_id]['amount_with_service_fee'] = home.get('pricing_quote').get('rate_with_service_fee').get('amount')
#     data_dict[room_id]['rate_type'] = home.get('pricing_quote').get('rate_type')
#     data_dict[room_id]['weekly_price_factor'] = home.get('pricing_quote').get('weekly_price_factor')



# printer = pprint.PrettyPrinter()
# printer.pprint(data_dict)
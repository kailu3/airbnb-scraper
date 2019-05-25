# -*- coding: utf-8 -*-
import scrapy
import json
import collections
import re
from scrapy_splash import SplashRequest
from airbnb_scraper.items import AirbnbScraperItem


class AirbnbSpider(scrapy.Spider):
    name = 'airbnb'
    allowed_domains = ['www.airbnb.com']

    # TODO: WRITE METHOD HEADER
    def start_requests(self):
        url = (
        'https://www.airbnb.com/api/v2/explore_tabs?_format=for_explore_search_web'
        '&_intents=p1&adults=0&allow_override%5B%5D=&auto_ib=false&children=0'
        '&client_session_id=7c313cb9-183b-47a1-a687-7c96d5ee391a&currency=CAD&experiences_per_grid=20'
        '&fetch_filters=true&guests=0&guidebooks_per_grid=20&has_zero_guest_treatment=true&infants=0'
        '&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_offset=18&items_per_grid=18'
        '&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=en&luxury_pre_launch=false'
        '&metadata_only=false&place_id=ChIJs0-pQ_FzhlQRi_OBm-qWkbs&query=Vancouver%2C%20BC%2C%20Canada'
        '&query_understanding_enabled=true&refinement_paths%5B%5D=%2Fhomes&s_tag=G4F7MNfG&satori_version=1.1.9'
        '&screen_height=797&screen_size=medium&screen_width=885&search_type=PAGINATION&section_offset=8'
        '&selected_tab_id=home_tab&show_groupings=true&supports_for_you_v3=true&timezone_offset=-240&version=1.5.6')
        yield scrapy.Request(url=url, callback=self.parse_id)

    # This method parses all the urls 
    def parse_id(self, response):
        
        # Fetch and Write the response data
        data = json.loads(response.body)

        # Return a List of all homes
        try: 
            homes = data.get('explore_tabs')[0].get('sections')[2].get('listings')
        except:
            homes = data.get('explore_tabs')[0].get('sections')[0].get('listings')
        

        base_url = 'https://www.airbnb.com/rooms/'

        data_dict = collections.defaultdict(dict)

        for home in homes:
            room_id = str(home.get('listing').get('id'))
            url = base_url + str(home.get('listing').get('id'))
            data_dict[room_id]['url'] = url
            data_dict[room_id]['price'] = home.get('pricing_quote').get('rate').get('amount')
            data_dict[room_id]['bathrooms'] = home.get('listing').get('bathrooms')
            data_dict[room_id]['bedrooms'] = home.get('listing').get('bedrooms')
            data_dict[room_id]['host_languages'] = home.get('listing').get('host_languages')
            data_dict[room_id]['is_business_travel_ready'] = home.get('listing').get('is_business_travel_ready')
            data_dict[room_id]['is_fully_refundable'] = home.get('listing').get('is_fully_refundable')
            data_dict[room_id]['is_new_listing'] = home.get('listing').get('is_new_listing')
            data_dict[room_id]['is_superhost'] = home.get('listing').get('is_superhost')
            data_dict[room_id]['lat'] = home.get('listing').get('lat')
            data_dict[room_id]['lng'] = home.get('listing').get('lng')
            data_dict[room_id]['localized_city'] = home.get('listing').get('localized_city')
            data_dict[room_id]['localized_neighborhood'] = home.get('listing').get('localized_neighborhood')
            data_dict[room_id]['listing_name'] = home.get('listing').get('name')
            data_dict[room_id]['person_capacity'] = home.get('listing').get('person_capacity')
            data_dict[room_id]['picture_count'] = home.get('listing').get('picture_count')
            data_dict[room_id]['reviews_count'] = home.get('listing').get('reviews_count')
            data_dict[room_id]['room_type_category'] = home.get('listing').get('room_type_category')
            data_dict[room_id]['star_rating'] = home.get('listing').get('star_rating')
            data_dict[room_id]['host_id'] = home.get('listing').get('user').get('id')
            data_dict[room_id]['avg_rating'] = home.get('listing').get('avg_rating')
            data_dict[room_id]['can_instant_book'] = home.get('pricing_quote').get('can_instant_book')
            data_dict[room_id]['monthly_price_factor'] = home.get('pricing_quote').get('monthly_price_factor')
            data_dict[room_id]['currency'] = home.get('pricing_quote').get('rate').get('currency')
            data_dict[room_id]['amt_w_service'] = home.get('pricing_quote').get('rate_with_service_fee').get('amount')
            data_dict[room_id]['rate_type'] = home.get('pricing_quote').get('rate_type')
            data_dict[room_id]['weekly_price_factor'] = home.get('pricing_quote').get('weekly_price_factor')

        # Iterate through dictionary of URLs to send a SplashRequest for each
        for room_id in data_dict:
            yield SplashRequest(url=base_url+room_id, callback=self.parse_details,
                                meta=data_dict.get(room_id),
                                endpoint="render.html",
                                args={'wait': '0.5'})
    
    # TODO: WRITE METHOD HEADER
    # This method parses all the information from one listing
    def parse_details(self, response):

        # New Instance
        listing = AirbnbScraperItem()

        # Fill in fields for Instance from initial scrapy call
        listing['host_languages'] = response.meta['host_languages']
        listing['is_superhost'] = response.meta['is_superhost']
        listing['host_id'] = str(response.meta['host_id'])
        listing['price'] = response.meta['price']
        listing['url'] = response.meta['url']
        listing['bathrooms'] = response.meta['bathrooms']
        listing['bedrooms'] = response.meta['bedrooms']
        listing['is_business_travel_ready'] = response.meta['is_business_travel_ready']
        listing['is_fully_refundable'] = response.meta['is_fully_refundable']
        listing['is_new_listing'] = response.meta['is_new_listing']
        listing['lat'] = response.meta['lat']
        listing['lng'] = response.meta['lng']
        listing['localized_city'] = response.meta['localized_city']
        listing['localized_neighborhood'] = response.meta['localized_neighborhood']
        listing['listing_name'] = response.meta['listing_name']
        listing['person_capacity'] = response.meta['person_capacity']
        listing['picture_count'] = response.meta['picture_count']
        listing['reviews_count'] = response.meta['reviews_count']
        listing['room_type_category'] = response.meta['room_type_category']
        listing['star_rating'] = response.meta['star_rating']
        listing['avg_rating'] = response.meta['avg_rating']
        listing['can_instant_book'] = response.meta['can_instant_book']
        listing['monthly_price_factor'] = response.meta['monthly_price_factor']
        listing['weekly_price_factor'] = response.meta['weekly_price_factor']
        listing['currency'] = response.meta['currency']
        listing['amt_w_service'] = response.meta['amt_w_service']
        listing['rate_type'] = response.meta['rate_type']

        # Other fields scraped from html response.text using regex (some might fail hence try/catch)
        try:
            listing['num_beds'] = int((re.search('"bed_label":"(.).*","bedroom_label"', response.text)).group(1))
        except:
            listing['num_beds'] = 0

        try:
            listing['host_reviews'] = int((re.search(r'"badges":\[{"count":(.*?),"id":"reviews"',
                                      response.text)).group(1))
        except:
            listing['host_reviews'] = 0

        # Main six rating metrics + overall_guest_satisfication
        try:
            listing['accuracy'] = int((re.search('"accuracy_rating":(.*?),"', response.text)).group(1))
            listing['checkin'] = int((re.search('"checkin_rating":(.*?),"', response.text)).group(1))
            listing['cleanliness'] = int((re.search('"cleanliness_rating":(.*?),"', response.text)).group(1))
            listing['communication'] = int((re.search('"communication_rating":(.*?),"', response.text)).group(1))
            listing['value'] = int((re.search('"value_rating":(.*?),"', response.text)).group(1))
            listing['location'] = int((re.search('"location_rating":(.*?),"', response.text)).group(1))
            listing['guest_satisfication'] = int((re.search('"guest_satisfaction_overall":(.*?),"',
                                             response.text)).group(1))
        except:
            listing['accuracy'] = 0
            listing['checkin'] = 0
            listing['cleanliness'] = 0
            listing['communication'] = 0
            listing['value'] = 0
            listing['location'] = 0
            listing['guest_satisfication'] = 0

        # Extra Host Fields
        try:
            listing['response_rate'] = int((re.search('"response_rate_without_na":"(.*?)%",', response.text)).group(1))
            listing['response_time'] = (re.search('"response_time_without_na":"(.*?)",', response.text)).group(1)
        except:
            listing['response_rate'] = 0
            listing['response_time'] = ''

        # Finally yield the object
        yield listing

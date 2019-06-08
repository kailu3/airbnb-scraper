# airbnb_scraper

Spider built with scrapy and scrapySplash to crawl listings

- [x] Spider can successfully parse one page of listings  
- [x] Spider can successfully parse mutliple/all pages of designated location
- [x] Spider can take price ranges as arguments (`price_lb` and `price_ub`)
- [x] Spider can take location as argument
*Note: Airbnb only returns a maximum of ~300 listings per specific filter*

Run with `scrapy crawl airbnb -o {filename}.json -a city='{cityname}' -a price_lb='{pricelowerbound}' -a price_ub='{priceupperbound}'`
# airbnb_scraper

Spider built with scrapy and ScrapySplash to crawl listings

- [x] Spider can successfully parse one page of listings  
- [x] Spider can successfully parse mutliple/all pages of designated location
- [x] Spider can take price ranges as arguments (`price_lb` and `price_ub`)
- [x] Spider can take location as argument  
**Note: Airbnb only returns a maximum of ~300 listings per specific filter**

## Set up

Before running spider, remember to run scrapy-splash in the background.

    `docker run -p 8050:8050 scrapinghub/splash`

See [scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash) for installation instructions.

## Crawling

Run with `scrapy crawl airbnb -o {filename}.json -a city='{cityname}' -a price_lb='{pricelowerbound}' -a price_ub='{priceupperbound}'`

`cityname` refers to a valid city name

`pricelowerbound` refers to a lower bound for price from 0 to 999

`priceupperbound` refers to upper bound for price from 0 to 999. Spider will close if `priceupperbound` is less than
`pricelowerbound`

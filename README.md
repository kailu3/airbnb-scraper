# airbnb_scraper :spider:

Spider built with scrapy and ScrapySplash to crawl listings

## Checklist

*This checklist is for personal use and isn't relevant to using the scraper.*

- [x] Spider can successfully parse one page of listings  
- [x] Spider can successfully parse mutliple/all pages of designated location
- [x] Spider can take price ranges as arguments (`price_lb` and `price_ub`)
- [x] Spider can take location as argument  

## Set up

Before running spider, remember to run scrapy-splash in the background.

    docker run -p 8050:8050 scrapinghub/splash

See [scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash) for installation instructions.

## Crawling

Run with `scrapy crawl airbnb -o {filename}.json -a city='{cityname}' -a price_lb='{pricelowerbound}' -a price_ub='{priceupperbound}'`

`cityname` refers to a valid city name

`pricelowerbound` refers to a lower bound for price from 0 to 999

`priceupperbound` refers to upper bound for price from 0 to 999. Spider will close if `priceupperbound` is less than
`pricelowerbound`  
**Note: Airbnb only returns a maximum of ~300 listings per specific filter (price range). To get more listings, I recommend scraping multiple times using small increments in price and concatenating the datasets.**

If you would like to do multiple scrapes over a wide price range (e.g. 10-spaced intervals from 20 to 990), see `cancun.sh` which I used to crawl a large number listings for Cancún.

## Acknowledgements
I would like to thank **Ahmed Rafik** for his guidance and teachings.
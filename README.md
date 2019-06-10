# airbnb_scraper

Spider built with scrapy and ScrapySplash to crawl listings

- [x] Spider can successfully parse one page of listings  
- [x] Spider can successfully parse mutliple/all pages of designated location
- [x] Spider can take price ranges as arguments (`price_lb` and `price_ub`)
- [x] Spider can take location as argument
*Note: Airbnb only returns a maximum of ~300 listings per specific filter*

Before running, make sure you have ScrapySplash running.
`docker run -p 8050:8050 scrapinghub/splash`  

Install scrapy-splash using pip::

    $ pip install scrapy-splash  

Scrapy-Splash uses Splash_ HTTP API, so you also need a Splash instance.
Usually to install & run Splash, something like this is enough::

    $ docker run -p 8050:8050 scrapinghub/splash  

Run with `scrapy crawl airbnb -o {filename}.json -a city='{cityname}' -a price_lb='{pricelowerbound}' -a price_ub='{priceupperbound}'`

TODO:
fix price ranges 990 and above to just involve [990, inifinity]
add error checking to ensure that price ranges input are numerical and price_ub > price_lb
added bash script to run over different price intervals and generate a file each time
https://stackoverflow.com/questions/11005756/how-to-loop-an-executable-command-in-the-terminal-in-linux

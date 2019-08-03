#!/bin/sh

for var in `seq 15 10 995`
do

   lower_bound=$var
   upper_bound=`expr $var + 10`

   # Fixed Variables
   CITY="New%20York%"
   CONJUNCTION="to"
   FORMAT=".json"
   DATA_LOCATION="new_york_data"

   filename="$lower_bound$CONJUNCTION$upper_bound$FORMAT"

   # Run scraper on specific range
   scrapy crawl airbnb -o $filename -a city=$CITY -a price_lb=$lower_bound -a price_ub=$upper_bound
   mv $filename $DATA_LOCATION

done


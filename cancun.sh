#!/bin/sh

for var in `seq 21 10 991`
do

   lower_bound=$var
   upper_bound=`expr $var + 10`
   CITY="Cancun"
   
   CONJUNCTION="to"
   FORMAT=".json"
   DATA_LOCATION="cancun_data"

   filename="$lower_bound$CONJUNCTION$upper_bound$FORMAT"
   # Run scraper on specific range
   scrapy crawl airbnb -o $filename -a city=$CITY -a price_lb=$lower_bound -a price_ub=$upper_bound
   mv $filename $DATA_LOCATION

#    echo $LOWER_BOUND
#    echo $UPPER_BOUND
#    echo $CITY
#    echo $filename
done


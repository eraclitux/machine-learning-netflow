#!/bin/sh

./masquerade.sh

cat test-samples.txt | sed '/^;/d' |  cut -d'#' -f1 > test-samples.raw
cat test-samples.txt | sed '/^;/d' |  cut -d'#' -f2 | tr -s [:space:] > test-samples-labels.txt

./mangle.sh test-samples.raw > test-samples.csv       
./mangle.sh incoming-floods.raw > incoming-floods.csv       
./mangle.sh small-flood.raw > small-flood.csv       
./mangle.sh http.raw > http.csv                     
./mangle.sh tivoli.raw > tivoli.csv                 
./mangle.sh smtp.raw > smtp.csv 

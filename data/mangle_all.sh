#!/bin/sh

./masquerade.sh

cat test-samples.txt | sed '/^;/d' |  cut -d'#' -f1 > test-samples.raw
cat test-samples.txt | sed '/^;/d' |  cut -d'#' -f2 | tr -s [:space:] > test-samples-labels.txt

for f in `ls *raw`; do
	echo ${f%\.*}
	./mangle.sh $f > ${f%\.*}.csv
done

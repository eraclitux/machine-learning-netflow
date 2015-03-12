#!/bin/sh

sed '/^#/d;s/(.[0-9].[0-9])//g;s/ M/M/g;s/ G/G/g;' $1 |  awk  '{print $3,$6,$7,$8,$9,$10,$11}' | sed 's/ /,/g'

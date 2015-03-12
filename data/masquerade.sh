#!/bin/sh

for f in `ls ./sensible`; do
	sed 's/[0-9]\+\.[0-9]\+\.[0-9]\+\.[0-9]\+/XXX.XXX.XXX.XXX/g' ./sensible/$f > ./$f
done

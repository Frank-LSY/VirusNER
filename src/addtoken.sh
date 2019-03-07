#!/bin/bash

i = 1
while [[ $i<=300 ]]; 
do
	echo $i
	sed -i '' '1i\
	token' "../labeled-token/$i.tsv"
	let "i++"
	#statements
done
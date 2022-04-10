#!/bin/bash
digitLimit=2000
sum=0
for(( i=1000; i<=$digitLimit; i++ ))
do
	sum=$(( sum + i ))
done
echo "Sum of the numbers b/w 1000 and 2000 - ${sum}"
bin=$(echo "obase=2;$sum" | bc)
echo "Binary - ${bin}"

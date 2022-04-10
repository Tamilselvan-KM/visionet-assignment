#!/bin/bash
mkdir five
n=5
for (( i=1; i<=$n; i++ ))
do
  mkdir five/dir$i
  for (( j=1; j<=4; j++ ))
  do
    touch five/dir$i/file$j
    if [ $j -eq 1 ]
    then
       echo "1 - Hi, This is first file and its containing single digit" > five/dir$i/file$j
    elif [ $j -eq 2 ]
    then
       echo "11 - Hi, This is second file 
	22 - its containing double digits" > five/dir$i/file$j
    elif [ $j -eq 3 ]
    then
       echo "111 - Hi,
	222 - This is third file its containing 
	333 - triple digits" > five/dir$i/file$j
    elif [ $j -eq 4 ]
    then
       echo "1111 - Hi,
		      2222 - This is fourth file 
		      3333 - its containing 
		      4444 - four digits" > five/dir$i/file$j
    fi
  done
done

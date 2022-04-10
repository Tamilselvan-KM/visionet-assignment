#!/bin/bash
if [ -d $1 ]
then 
	echo "The passing args is a Directory"
elif [ -f $1 ]
then
	echo "The passing args is a File"
else
	echo "The passing args is not exist on the system"
fi


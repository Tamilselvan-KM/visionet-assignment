#!/bin/sh
processIn="bash"
if ps | grep "$processIn"
then
	echo "Yes"
else
	echo "NO"
fi

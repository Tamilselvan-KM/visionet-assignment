#!/bin/sh
isFile= wc -w < /home/tamilsabarikm/linux-assignments/test1/file1.sh 
if [ "$isFile"!=0 ]
then
	mv /home/tamilsabarikm/linux-assignments/test2/file2.sh  /home/tamilsabarikm/linux-assignments/test1/file1.sh
	echo "The file is moved"
else
	echo "File is not available"
fi

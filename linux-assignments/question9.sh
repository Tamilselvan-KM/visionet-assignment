#!/bin/bash
if [ $# -ne 2 ]
then
echo "pass directory name and bytes as two arguments"
else
a='find $1 -type f -size +$2c'
echo "files with more than $2 bytes are"
rm $a
echo "removed all files more than $2 bytes"
fi

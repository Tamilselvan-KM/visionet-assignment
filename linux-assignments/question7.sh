#!/bin/sh
Count=$(who|grep $USER|wc -l)
echo "$Count times logged as $USER"

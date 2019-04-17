#!/bin/bash

echo $0 $1 $2

pwd
ls

if [[ $2 != "needed" ]];
then
 echo binding $2 to $1
 rfcomm release "$1"
 rfcomm bind "$1" "$2"
 chmod a+rwx "/dev/rfcomm$1"
fi

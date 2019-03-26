#!/bin/sh

sudo rfcomm release 0
sudo rfcomm bind 0 98:D3:A1:FD:44:FE

file="/dev/rfcomm0"

while IFS= read -r line
do
	echo "reading a line:"
	echo "$line"
done < "$file"

sudo rfcomm release 0

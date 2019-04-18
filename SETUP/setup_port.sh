#!/bin/bash

echo "setting up all 5 arduino rfcomm ports"

# 0

if test -f '/dev/rfcomm0'; then
	echo "unbinding rfcomm0"
	rfcomm release "0"
fi
echo "binding rfcomm0"
rfcomm bind "0" "98:D3:11:FC:1C:45"
chmod a+rwx "/dev/rfcomm0"

# 1

if test -f '/dev/rfcomm1'; then
	echo "unbinding rfcomm1"
	rfcomm release "1"
fi
echo "binding rfcomm1"
rfcomm bind "1" "98:D3:A1:FD:44:FE"
chmod a+rwx "/dev/rfcomm1"

# 2

if test -f '/dev/rfcomm2'; then
	echo "unbinding rfcomm2"
	rfcomm release "2"
fi
echo "binding rfcomm2"
rfcomm bind "2" "98:D3:A1:FD:49:8D"
chmod a+rwx "/dev/rfcomm2"

# 3

if test -f '/dev/rfcomm3'; then
	echo "unbinding rfcomm3"
	rfcomm release "3"
fi
echo "binding rfcomm3"
rfcomm bind "3" "98:D3:91:FD:4B:59"
chmod a+rwx "/dev/rfcomm3"

# 4

if test -f '/dev/rfcomm4'; then
	echo "unbinding rfcomm4"
	rfcomm release "4"
fi
echo "binding rfcomm4"
rfcomm bind "4" ""
chmod a+rwx "/dev/rfcomm4"




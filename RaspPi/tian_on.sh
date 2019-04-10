#!/bin/bash

# TIAN's MAC address
TIAN=98:D3:A1:FD:49:8D

# ON command
COMMAND=1

./pair_bluetooth.sh $TIAN

echo connecting to port
sudo rfcomm connect hci0 $TIAN &
echo starting picocom
coproc sudo picocom -c /dev/rfcomm0


echo sending 1 to picocom
echo 1 >&"${COPROC[1]}" 
sleep 1
#cat <&"${COPROC[0]}"
#echo sleeping for 1 second
#sleep 1
#echo sending 0 to picocom
#echo 0 >&"${COPROC[1]}" 


sleep 1
sudo rfcomm release 0
sudo pkill rfcomm

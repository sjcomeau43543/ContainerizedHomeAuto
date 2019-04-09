#!/bin/bash

DEVICE="$1"
echo "Pairing $DEVICE via bluetoothctl"

coproc sudo bluetoothctl
echo "agent on" >&"${COPROC[1]}"
echo "scan on" >&"${COPROC[1]}"

action () {
    while true; do
    	read var <&"${COPROC[0]}"
        #echo $var
        if [[ "$var" == *"$DEVICE"* ]]
        then
            echo Found "$DEVICE"
            echo pair "$DEVICE" >&"${COPROC[1]}"
            echo "1234" >&"${COPROC[1]}"
            echo Paired with "$DEVICE"
            echo trust "$DEVICE" >&"${COPROC[1]}"
            echo connect "$DEVICE" >&"${COPROC[1]}"
            echo exit >&"${COPROC[1]}"
            break
        fi
    done
}

echo Searching for "$1" in available devices
action


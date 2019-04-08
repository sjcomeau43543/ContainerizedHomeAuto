#!/bin/bash

echo "Pairing LEONARD via bluetoothctl"

echo "starting coproc"
coproc sudo bluetoothctl

echo "agent on"
echo "agent on" >&"${COPROC[1]}"

echo "scan on"
echo "scan on" >&"${COPROC[1]}"

action () {
    echo "running action."
    while true; do
    	read var <&"${COPROC[0]}"
        #echo $var
        if [[ "$var" == *"98:D3:91:FD:4B:59"* ]]
        then
            echo "Found LEONARD"
            echo "pair 98:D3:91:FD:4B:59" >&"${COPROC[1]}"
            echo "1234" >&"${COPROC[1]}"
            echo "exit" >&"${COPROC[1]}"
            break
        fi
    done
}

echo "Searching for LEONARD in available devices"
action


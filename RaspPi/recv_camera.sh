#!/bin/sh

echo Bind LEONARD to rfcomm0
sudo rfcomm bind 0 98:D3:91:FD:4B:59

action () {
    echo running action.
    while true; do
        if [$1 == 0]
        then echo the output is 0
	#elif [ $1 -lt 0 ] || [ $1 -gt 0 ]
        #then echo the output is 1
        fi
    done
}

echo Listening to traffic on rfcomm0
sudo cat -E /dev/rfcomm0 | action

sudo rfcomm unbind 0


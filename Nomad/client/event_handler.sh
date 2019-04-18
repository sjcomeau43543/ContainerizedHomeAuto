#!/bin/bash

ID="$1"
STATUS="$2"

if [[ "$ID" == "photo" ]]
then
    if [[ "$STATUS" == "1" ]]
    then
        echo turn lights off
        curl -X POST -d @/home/pirate/lights_off.json http://localhost:4646/v1/job/action/dispatch
    elif [[ "$STATUS" == "0" ]]
    then
        echo turn lights on
        curl -X POST -d @/home/pirate/lights_on.json http://localhost:4646/v1/job/action/dispatch
    else
        echo photo status error
    fi
elif [[ "$ID" == "ir" ]]
then
    if [[ "$STATUS" == "1" ]]
    then
        echo turn lights on
        curl -X POST -d @/home/pirate/lights_on.json http://localhost:4646/v1/job/action/dispatch
    elif [[ "$STATUS" == "0" ]]
    then
        echo turn lights off
        curl -X POST -d @/home/pirate/lights_off.json http://localhost:4646/v1/job/action/dispatch
    else
        echo ir status error
    fi
else
    echo status error
fi


#!/bin/bash

# getting input mac address
MAC=${1?Error: No MAC given}

# trap on exit and unbind rfcomm
trap kill_proc SIGINT SIGTERM

connect () {
  echo -e "\tstarting coproc"
  coproc sudo bluetoothctl

  echo -e "\tagent on"
  echo "agent on" >&"${COPROC[1]}"

  echo -e "\tscan on"
  echo "scan on" >&"${COPROC[1]}"

  echo -e "\trunning action."
  while true; do
  	read var <&"${COPROC[0]}"
      if [[ "$var" == *"$MAC"* ]]
      then
        echo -e "\tFound device"
        echo "pair $MAC" >&"${COPROC[1]}"
        echo "1234" >&"${COPROC[1]}"
        echo "exit" >&"${COPROC[1]}"
        break
      fi
  done
}

bind_port() {
  sudo rfcomm bind 0 "$MAC"
}

unbind_port() {
  sudo rfcomm release 0
}

kill_proc() {
  #kill -s SIGTERM $!
  unbind_port
  exit 0
}

read_continuously() {
  while true
  do
    sudo cat /dev/rfcomm0
    wait $!
  done
}

echo "Connecting to device..."
connect

echo "Binding rfcomm port..."
bind_port

echo "Reading from rfcomm port continuously..."
read_continuously

echo "Unbinding rfcomm port..."
unbind_port

#!/bin/bash

echo $0 $1 $2

rfcomm release "$1"
rfcomm bind "$1" "$2"
chmod a+rwx "/dev/rfcomm$1"


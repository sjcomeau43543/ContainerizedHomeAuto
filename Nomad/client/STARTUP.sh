#!/bin/bash

cd /home/pirate
mkdir nomad

consul agent -data-dir=/tmp/consul -node=agent-two -bind@10.0.0.11 &

sudo nomad agent -config=client.conf -network-interface=eth0

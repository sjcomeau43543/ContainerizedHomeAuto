#!/bin/bash

cd /home/pirate

consul agent -server -bootstrap-expect=1 -data-dir=/tmp/consul -node=agent-one
-bind=10.0.0.8 &

consul join 10.0.0.11

sudo nomad agent -config=server.conf

nomad job run photo_sensor.nomad
nomad job run ir_sensor.nomad
nomad job run event_handler.nomad
nomad job run action.nomad

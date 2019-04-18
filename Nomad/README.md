This is the basic setup for running Nomad

# Starting a client and server
Can start these in either order. After starting consul, check that both agents
are running with `consul members`

## Server
`consul agent -server -bootstrap-expect=1 -data-dir=/tmp/consul -node=agent-one -bind=10.0.0.8 &`

After you've started the client consul agent, join the two together
`consul join 10.0.0.11`

`sudo nomad agent -config=server.conf`

## Client
sudo consul agent -data-dir=/tmp/consul -node=agent-two -bind=10.0.0.11 &

sudo nomad agent -config=client.conf -network-interface=eth0


## NOTES

- If there's an error, try deleting everything in the nomad/ directory
- Server should have: all the .nomad job files, server.conf, nomad/
- Client should have: automate.py, client.conf, nomad/
- Check job stderr with
`nomad alloc logs -stderr e36b0512-a801-2404-a9fb-e63a6efd5efd`
where e36b0512-a801-2404-a9fb-e63a6efd5efd is the hash assigned to the job (you
can see it in the client INFO logs)


# How to run automate.py (t = 1 is on)
OLD:
sudo python automate.py -w -m 98:D3:A1:FD:49:8D -t 1

# CURL

## Dispatch parameterized job ({} is the parameters)
`curl -X POST -d "{}" http://localhost:4646/v1/job/test/dispatch`

## Force garbage collection
`curl -X PUT http://localhost:4646/v1/system/gc`

## List jobs
`curl -X GET http://localhost:4646/v1/jobs`

# Run a parameterized job
First, consul and nomad need to be running on the client and server.

You need to start the job on the server:
`nomad job run test.nomad` where `test.nomad` is the name of the job file.

Then, send a POST request to the http API of Nomad:
`curl --request POST -d "{}" http://localhost:4646/v1/job/test/dispatch`
{} is the parameters to be sent with the job (corresponds to parameterized{}
stanza in test.nomad). NOTE: It literally needs to say "{}". You can put
arguments inside this if you'd like: "{foo}" where foo is an argument


# Flow of control
Reading from sensors: Reading Pis run a batch job (photo\_sensor.nomad and
ir\_sensor.nomad) whose command is to forever
listen to an Arduino. When an event occurs (e.g., Arduino says "the room is
bright"), the Pi uses the Nomad http API to dispatch a job that will trigger the
proper actuators.

Somewhere in the command, happens when Arduino sends event alert:
`curl -X POST -d "{}" http://localhost:4646/v1/job/event_handler/dispatch`

event\_handler job: The event\_handler job is a batch/parameterized job in which
the home automation logic takes place. The job is run at the beginning of setup
by the server. After which, any Nomad agent can dispatch a job with arguments
using the API. The event\_handler takes as parameters the ID and status of the
sensor (e.g.  the photovoltaic sensor will say "light on" or "light off", the IR
camera will say "people in" or "people out"). Based on this input, the
event\_handler will dispatch the proper jobs to the actuators using the action
job.

Based on the arguments passed when dispatched, this will call something like:
`curl -X POST -d @lights_on.json http://localhost:4646/v1/job/action/dispatch`

Where lights\_on.json contains the MAC address and port for the HC-05 Bluetooth
module and the message "1" for "on".

action job: This is a second batch/parameterized job whose parameters include
the MAC address of the Arduino (the Bluetooth module) and what action should be
taken (1 or 0 for on or off). The main command of this job is automate.py. When
a job is dispatched, one of the client Pis will bind (or not) to the Arduino
over Bluetooth, send the command, and then terminate.

`nomad job dispatch -meta "mac=123" action`
`curl --request POST -d @payload.json
http://localhost:4646/v1/job/action/dispatch`

payload.json looks like:
`{
    "Meta": {
        "mac" : "234"
    }
}
`
NOTE: for now, all PIs need these payload files on them, This is not ideal,
since it prevents easily adding a new device. A problem for another time
perhaps.

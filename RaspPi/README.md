This is the basic setup for running Nomad

# Starting a client and server
Can start these in either order. After starting consul, check that both agents
are running with `consul members`

## Server
`consul agent -server -bootstrap-expect=1 -data-dir=/tmp/consul -node=agent-one -bind=10.0.0.8`

`sudo nomad agent -config=server.conf`

## Client
sudo consul agent -data-dir=/tmp/consul -node=agent-two -bind=10.0.0.11 &

sudo nomad agent -config=client.conf -network-interface=eth0


# How to run automate.py (t = 1 is on)
sudo python automate.py -w -m 98:D3:A1:FD:49:8D -t 1

# CURL

## Dispatch parameterized job ({} is the parameters)
`curl -X POST -d "{}" http://localhost:4646/v1/job/test/dispatch`

## Force garbage collection
`curl -X PUT http://localhost:4646/v1/system/gc`

## List jobs
`curl -X GET http://localhost:4646/v1/jobs`

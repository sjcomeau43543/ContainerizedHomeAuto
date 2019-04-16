This is the basic setup for running Nomad

# First window
// Need consul in addition to nomad
sudo consul agent -dev -bind=127.0.0.1
sudo nomad agent -dev

# Second window
nomad job init
nomad job run example.nomad
nomad status example


# How to run automate.py
sudo python automate.py -w -m 98:D3:A1:FD:49:8D -t 1

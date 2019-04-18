## Usage

### Set up the bindings
sudo ./setup_port.sh $PORT $MAC

Where port is the RFCOMM port and MAC is the mac address of the bluetooth module to connect to

### Communicate over bluetooth
python2 automate.py $RW $MAC $PORT $MESSAGE

Where RW is "read" or "write" depending on function you want to perform
MAC is the mac address of the bluetooth module #TODO remove this arg we don't need it if it's already bound to the rfcomm port
PORT is the RFCOMM port
MESSAGE is either an empty string or the message you want to send to the bluetooth device


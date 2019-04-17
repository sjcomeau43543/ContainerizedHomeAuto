import socket, sys

print sys.argv[1], sys.argv[2]

sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
sock.bind((sys.argv[1], int(sys.argv[2])))

import subprocess, time, sys, os

import serial

# calls a command using subprocess
def call(command, stdout=subprocess.PIPE):
  print 'Calling: ' + str(command)
  subprocess.call(command, stdout=stdout)

# writes a message to the rfcomm port (bluetooth)
def write(serial_obj, message, port):
  serial_obj.write(message)
  response = read(serial_obj)
  while 'SUCCESS' not in response:
    serial_obj.write(message)
    response = read(serial_obj)

# reads for input on the rfcomm port
def read(serial_obj):
  print 'Reading...'
  result = serial_obj.read_until()
  print 'Read:', result
  return result

def main():
  readwrite = sys.argv[1]
  mac = sys.argv[2]
  port = sys.argv[3]
  message = sys.argv[4]

  print sys.argv

  if readwrite == "needed":
    print 'ERROR: You need to provide read or write'
    exit()
 
  if mac == "needed":
    print 'ERROR: You need to provide a mac address'
    exit()

  if readwrite == "read":
    serial_obj = serial.Serial('/dev/rfcomm'+port, 9600, timeout=1)
  
    while 1:
      read(serial_obj)
  elif readwrite == "write": 
    if message == "needed":
      print 'ERROR: If you want to write to the bluetooth device please give a message using -t MESSAGE'
      exit()

    serial_obj = serial.Serial('/dev/rfcomm'+port, 9600, timeout=1)

    write(serial_obj, message, port)
  else: 
    print 'ERROR: You must have either the -r,--read or -w,--write flags to tell if you want to read or write to the bluetooth device.'
    exit()


if __name__ == '__main__':
  main()


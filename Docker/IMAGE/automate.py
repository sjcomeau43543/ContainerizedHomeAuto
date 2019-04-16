import subprocess, time, sys, os

import serial

# calls a command using subprocess
def call(command, stdout=subprocess.PIPE):
  print 'Calling: ' + str(command)
  subprocess.call(command, stdout=stdout)

# ummm this doesn't work sorry, but as long as you pair once, you don't need to re-pair
def connect(MAC):
  p = subprocess.Popen(['sudo', 'bluetoothctl'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

  p.stdin.write('power on\n')
  time.sleep(1)
  p.stdin.write('agent on\n')
  time.sleep(1)
  p.stdin.write('default-agent\n')
  time.sleep(1)
  p.stdin.write('scan on\n')
  for line in iter(p.stdout.readline, ''):
    print line
    if MAC in line:
      print line
      break
  p.stdin.write('trust '+MAC+'\n')
  time.sleep(1)
  p.stdin.write('exit\n')

  #p.terminate()

# unbinds the rfcomm port
def unbind(port):
  if os.path.exists('/dev/rfcomm'+port):
    call(['sudo', 'rfcomm', 'release', port])

# binds the rfcomm port
def bind(MAC, port):
  call(['sudo', 'rfcomm', 'bind', port, MAC])
  call(['sudo', 'chmod', 'a+rwx', '/dev/rfcomm'+port])

# writes a message to the rfcomm port (bluetooth)
def write(serial_obj, message, port):
  serial_obj.write(message)
  response = read(serial_obj)
  while 'Turning the LED ' not in response:
    serial_obj.write(message)
    response = read(serial_obj)
  #call(['sudo', 'echo', str(message)], open('/dev/rfcomm'+str(port), 'wb'))

# reads for input on the rfcomm port
def read(serial_obj):
  print 'Reading...'
  result = serial_obj.read_until()
  print 'Read:', result
  return result

def main():
  to_bind = sys.argv[1]
  readwrite = sys.argv[2]
  mac = sys.argv[3]
  port = sys.argv[4]
  message = sys.argv[5]

  print sys.argv

  if readwrite == "needed":
    print 'ERROR: You need to provide read or write'
    exit()
 
  if mac == "needed":
    print 'ERROR: You need to provide a mac address'
    exit()

  if to_bind == "true":
    unbind(port)
    bind(mac, port)

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


import subprocess, time, argparse

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
  call(['sudo', 'rfcomm', 'release', str(port)])

# binds the rfcomm port
def bind(MAC, port):
  call(['sudo', 'rfcomm', 'bind', str(port), MAC])
  call(['sudo', 'chmod', 'a+rwx', '/dev/rfcomm'+str(port)])

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
  parser = argparse.ArgumentParser(description="Use this program to communicate over bluetooth with a device you've paired and trusted in the past.")
  
  # actions
  parser.add_argument('-r', '--read', action='store_true', help="Read from the bluetooth device")
  parser.add_argument('-w', '--write', action='store_true', help="Write to the bluetooth device")
  parser.add_argument('-b', '--bind', action='store_true', help="Bind/Unbind the port")

  # options
  parser.add_argument('-m', '--mac', required=True, help="The MAC address of the bluetooth device.") 
  parser.add_argument('-p', '--port', default=0, help="The RFCOMM port to use for communication")
  parser.add_argument('-t', '--message', help="The message to write to the bluetooth device")

  args = parser.parse_args()

  if args.bind:
    unbind(str(args.port))
    bind(args.mac, str(args.port))

  if args.read:
    serial_obj = serial.Serial('/dev/rfcomm'+str(args.port), 9600, timeout=1)
  
    while 1:
      read(serial_obj)
  elif args.write: 
    if args.message is None:
      print 'ERROR: If you want to write to the bluetooth device please give a message using -t MESSAGE'
      exit()

    serial_obj = serial.Serial('/dev/rfcomm'+str(args.port), 9600, timeout=1)

    write(serial_obj, str(args.message), str(args.port))
  else: 
    print 'ERROR: You must have either the -r,--read or -w,--write flags to tell if you want to read or write to the bluetooth device.'
    exit()


if __name__ == '__main__':
  main()


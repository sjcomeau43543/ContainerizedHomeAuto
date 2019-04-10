import subprocess, time, argparse

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
def write(port, message):
  f = open('/dev/rfcomm'+str(port), 'w')
  call(['sudo', 'echo', str(message)], f)

# reads for input on the rfcomm port
def read(port):
  call(['sudo', 'cat', '/dev/rfcomm'+str(port)])

def main():
  parser = argparse.ArgumentParser(description="Use this program to communicate over bluetooth with a device you've paired and trusted in the past.")
  
  # actions
  parser.add_argument('-r', '--read', action='store_true', help="Read from the bluetooth device")
  parser.add_argument('-w', '--write', action='store_true', help="Write to the bluetooth device")

  # options
  parser.add_argument('-m', '--mac', required=True, help="The MAC address of the bluetooth device.") 
  parser.add_argument('-p', '--port', default=0, help="The RFCOMM port to use for communication")
  parser.add_argument('-t', '--message', help="The message to write to the bluetooth device")

  args = parser.parse_args()

  if args.read:
    unbind(str(args.port))
    bind(args.mac, str(args.port))
  
    read(str(args.port))
  elif args.write: 
    if args.message is None:
      print 'ERROR: If you want to write to the bluetooth device please give a message using -t MESSAGE'
      exit()
    unbind(str(args.port))
    bind(args.mac, str(args.port))
    write(str(args.port), str(args.message))
  else: 
    print 'ERROR: You must have either the -r,--read or -w,--write flags to tell if you want to read or write to the bluetooth device.'
    exit()


if __name__ == '__main__':
  main()


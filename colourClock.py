import socket
import time, math
import datetime

def sendUdp(firstByte, secondByte, times = 3):
  UDP_IP = "192.168.1.255"
  UDP_PORT = 8899
  MESSAGE = firstByte + secondByte + "\x55"
  sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  for x in range(0, times):
    time.sleep(0.05)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


def sendColour(colour):
  sendUdp("\x40", colour)


def sendBrightness(brightness):
  sendUdp("\x4E", brightness)


def turnOff():
  sendUdp("\x41", "\x00")


def turnOn():
  sendUdp("\x42", "\x00")

def convert(x):
  if x < 86:
    x = x + 170
  else:
    x -= 86
  return x

def xconvert(x):
  if x < 76:
    x += 180
  else:
    x -= 76
  return x


def startToFinish(sleepFor, num):
    for loop in range(1, num + 1):
       x = loop * int(math.floor(255 / num))
       sendColour(chr(convert(x)))
       print(str(convert(x)))


def startToFinishBrightness():
    for loop in range(1, 255):
       sendBrightness(chr(loop))
       print(str(loop))
       time.sleep(0.5)



def matchSeconds():
  while 1:
    colour = int(datetime.datetime.now().second * 4.25)
    print("Colour: " + str(colour))
    turnOn()
    tosend = chr(convert(colour))
    sendColour(tosend)
    print(str(ord(tosend)))
    time.sleep(1.5)


def matchMinutes():
  while 1:
    colour = int(datetime.datetime.now().minute * 4.25)
    print("Colour: " + str(colour))
    turnOn()
    tosend = chr(xconvert(colour))
    sendBrightness(chr(3))
    sendColour(tosend)
    print(str(ord(tosend)))
    time.sleep(10)


matchMinutes()
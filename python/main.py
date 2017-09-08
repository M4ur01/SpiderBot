from __future__ import division
from time import sleep
import signal 
import sys
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

#class test(Adafruit_PCA9685.PCA9685):

#	def __init__(self):
#		super(test,self).__init__()
	
	
#	def pwm.set_all_pwm(self, on, off):
#		self._device.write16(0xFA


def signal_handler(signal,frame):
  print("Shutting down")
  pwm.set_all_pwm(0,0)
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def stand():
  user = input("Leg2seg3: ")
  pwm.set_all_tri_pwm(380,400,460,300,400,380,375,350,270)
def walk():
  user = input("460 : ")
  pwm.set_all_tri_pwm(380,400,550,300,400,400,375,350,270)
  sleep(0.2)
  pwm.set_all_tri_pwm(380,400,200,300,400,user,375,350,270) 

##Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)
pwm.set_all_pwm(0,0)
print('Moving servo on channel 0, press Ctrl-C to quit...')
num = 0.1
while True:
#    Move servo on channel O between extremes.

  stand()
  ##sleep(0.5)
  ##walk()
  ##sleep(0.5)    


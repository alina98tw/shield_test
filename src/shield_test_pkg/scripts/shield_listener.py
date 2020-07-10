#!/usr/bin/env python

# This will move channel 0 from min to max position repeatedly.

from __future__ import division
import rospy, time
import RPi.GPIO as GPIO
from std_msgs.msg import Int32
import Adafruit_PCA9685


# Initialise the PCA9685 using the default address (0x40).
pwm0 = Adafruit_PCA9685.PCA9685(address=0x40)

# Alternatively specify a different address and/or bus:
pwm1 = Adafruit_PCA9685.PCA9685(address=0x41)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(pwmno,channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    if pwmno == 0:
        pwm0.set_pwm(channel, 0, pulse)
    elif pwmno == 1:
        pwm1.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm0.set_pwm_freq(60)
pwm1.set_pwm_freq(60)


def shield_callback(msg):
  rospy.loginfo("I heard %s", msg.data)
  print('Moving servos, press Ctrl-C to quit...')
  for i in [0, 2, 4, 6, 8, 10, 12, 14]:
        pwm0.set_pwm(i, 0, msg.data)
        pwm0.set_pwm(i+1, 0, msg.data)
        time.sleep(3)
  pwm1.set_pwm(0, 0, msg.data)
  pwm1.set_pwm(1, 0, msg.data)

def shield_listener():
  rospy.init_node('shield_listener', anonymous=True)
  rospy.Subscriber('move_servos', Int32, shield_callback)
  rospy.spin()

if __name__=='__main__':
  try:
    shield_listener()
  except rospy.RosInterruptException:
    pass

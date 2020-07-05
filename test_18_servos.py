# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

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

print('Moving servos, press Ctrl-C to quit...')
while True:
    # Move servos to min extreme.
    pwm0.set_pwm(0, 0, servo_min)
    pwm0.set_pwm(1, 0, servo_min)
    time.sleep(3)
    pwm0.set_pwm(2, 0, servo_min)
    pwm0.set_pwm(3, 0, servo_min)
    time.sleep(3)
    pwm0.set_pwm(4, 0, servo_min)
    pwm0.set_pwm(5, 0, servo_min)
    time.sleep(3)
    pwm0.set_pwm(6, 0, servo_min)
    pwm0.set_pwm(7, 0, servo_min)
    time.sleep(3)
    pwm0.set_pwm(8, 0, servo_min)
    pwm0.set_pwm(9, 0, servo_min)
    time.sleep(3)
    pwm0.set_pwm(10, 0, servo_min)
    pwm0.set_pwm(11, 0, servo_min)
    time.sleep(3)
    pwm0.set_pwm(12, 0, servo_min)
    pwm0.set_pwm(13, 0, servo_min)
    time.sleep(3)
    pwm0.set_pwm(14, 0, servo_min)
    pwm0.set_pwm(15, 0, servo_min)
    time.sleep(3)
    pwm1.set_pwm(0, 0, servo_min)
    pwm1.set_pwm(1, 0, servo_min)
    time.sleep(5)

    # Move servos to max extreme.
    pwm0.set_pwm(0, 0, servo_max)
    pwm0.set_pwm(1, 0, servo_max)
    time.sleep(3)
    pwm0.set_pwm(2, 0, servo_max)
    pwm0.set_pwm(3, 0, servo_max)
    time.sleep(3)
    pwm0.set_pwm(4, 0, servo_max)
    pwm0.set_pwm(5, 0, servo_max)
    time.sleep(3)
    pwm0.set_pwm(6, 0, servo_max)
    pwm0.set_pwm(7, 0, servo_max)
    time.sleep(3)
    pwm0.set_pwm(8, 0, servo_max)
    pwm0.set_pwm(9, 0, servo_max)
    time.sleep(3)
    pwm0.set_pwm(10, 0, servo_max)
    pwm0.set_pwm(11, 0, servo_max)
    time.sleep(3)
    pwm0.set_pwm(12, 0, servo_max)
    pwm0.set_pwm(13, 0, servo_max)
    time.sleep(3)
    pwm0.set_pwm(14, 0, servo_max)
    pwm0.set_pwm(15, 0, servo_max)
    time.sleep(3)
    pwm1.set_pwm(0, 0, servo_max)
    pwm1.set_pwm(1, 0, servo_max)
    time.sleep(3)


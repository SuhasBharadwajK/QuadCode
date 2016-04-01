from RPIO import PWM
import RPi.GPIO as GPIO
import pigpio
import time


SERVO = 17

pi = pigpio.pi() # Connect to local Pi.

pi.set_servo_pulsewidth(SERVO, 1000) # Minimum throttle.

time.sleep(1)

pi.set_servo_pulsewidth(SERVO, 2000) # Maximum throttle.

time.sleep(1)

pi.set_servo_pulsewidth(SERVO, 1100) # Slightly open throttle.

time.sleep(1)

pi.set_servo_pulsewidth(SERVO, 0) # Stop servo pulses.

pi.stop() # Disconnect from local Raspberry Pi.

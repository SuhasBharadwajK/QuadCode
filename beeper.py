import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

print "Enter GPIO pin number as per board:"
pin = int(raw_input())
print "Enter the time in seconds:"
secs = float(raw_input())
print "Enter the number of times to beep:"
times = int(raw_input())

def beep(pinnum, tsecs):
    GPIO.setup(pinnum, GPIO.OUT)
    for i in range(times):
        time.sleep(tsecs)
        GPIO.output(pinnum, GPIO.HIGH)
        time.sleep(tsecs)
        GPIO.output(pinnum, GPIO.LOW)

beep(pin, secs)

GPIO.cleanup()

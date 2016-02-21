import RPi.GPIO as GPIO
import time

class Drone:
    channels = [11, 13, 22, 40]
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

        GPIO.setwarnings(False)
        GPIO.cleanup()

        for channel in self.channels:
            GPIO.setup(channel, GPIO.OUT)

        self.motor1 = GPIO.PWM(11, 50)
        self.motor2 = GPIO.PWM(13, 50)
        self.motor3 = GPIO.PWM(22, 50)
        self.motor4 = GPIO.PWM(40, 50)

        self.speeds = {self.motor1 : 5, self.motor2 : 5, self.motor3 : 5, self.motor4 : 5.1}
        self.motors = [self.motor1, self.motor2, self.motor3, self.motor4]


    def printSpeeds(self):
        print "Speeds are :"
        for motor in self.motors:
            print self.speeds[motor]


    def start(self):
        for motor in self.motors:
            motor.start(self.speeds[motor])

        self.printSpeeds()


    def goUp(self):
        for motor in self.motors:
            self.speeds[motor] += 0.1
            motor.ChangeDutyCycle(self.speeds[motor])

        self.printSpeeds()

    
    def goDown(self):
        for motor in self.motors:
            self.speeds[motor] -= 0.1
            motor.ChangeDutyCycle(self.speeds[motor])

        self.printSpeeds()


    def stop(self):
        while self.speeds[max(self.speeds, key=lambda i : self.speeds[i])] > 5:
            for motor in self.motors:
                self.speeds[motor] -= 0.1
                motor.ChangeDutyCycle(self.speeds[motor])
            time.sleep(0.05)

        for motor in self.motors:
            motor.stop()
        GPIO.cleanup()
        self.printSpeeds()


    def cleanPins(self):
        GPIO.cleanup(11)
        GPIO.cleanup(13)
        GPIO.cleanup(22)
        GPIO.cleanup(40)


    def intialize(self):
        self.motor1 = GPIO.PWM(11, 50)
        self.motor2 = GPIO.PWM(13, 50)
        self.motor3 = GPIO.PWM(22, 50)
        self.motor4 = GPIO.PWM(40, 50)

import RPi.GPIO as GPIO
import time

class Drone:
    channels = [11, 13, 22, 40]
    isGoingForward = False; isGoingBack = False
    isGoingLeft = False; isGoingRight = False
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

        self.speeds = {self.motor1 : 5, self.motor2 : 5, self.motor3 : 5, self.motor4 : 5}
        self.freqs = {self.motor1 : 50, self.motor2 : 50, self.motor3 : 50, self.motor4 : 50}
        self.motors = [self.motor1, self.motor2, self.motor3, self.motor4]


    def setSpeeds(self, speed1 = 5, speed2 = 5, speed3 = 5, speed4 = 5):
        for index in range(1, 5):
            self.speeds[eval("self.motor" + str(index))] = eval("speed" + str(index));

    def printSpeeds(self):
        print "Speeds are :"
        for motor in self.motors:
            print self.speeds[motor]


    def changeFrequency(self, freq1 = 50, freq2 = 50, freq3 = 50, freq4 = 50):
        for index in range(1, 5):
            eval("self.motor" + str(index)).ChangeFrequency(eval("freq" + str(index)))


    def increaseFreq(self):
        for motor in self.motors:
            self.freqs[motor] += 5
            motor.ChangeFrequency(self.freqs[motor])


    def decreaseFreq(self):
        for motor in self.motors:
            self.freqs[motor] -= 5
            motor.ChangeFrequency(self.freqs[motor])


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


    def goForward(self):
        self.speeds[self.motor2] += 0.05
        self.speeds[self.motor3] += 0.05
        self.motor2.ChangeDutyCycle(self.speeds[self.motor2])
        self.motor3.ChangeDutyCycle(self.speeds[self.motor3])
        self.isGoingForward = True

    def goBack(self):
        self.speeds[self.motor1] += 0.05
        self.speeds[self.motor4] += 0.05
        self.motor1.ChangeDutyCycle(self.speeds[self.motor1])
        self.motor4.ChangeDutyCycle(self.speeds[self.motor4])
        self.isGoingBack = True


    def stop(self):
        while self.speeds[min(self.speeds, key=lambda i : self.speeds[i])] > 5:
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

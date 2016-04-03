#import time, readchar
from Motor import Motor

class Drone:
    def __init__(self, pin1 = 17, pin2 = 27, pin3 = 21, pin4 = 25, throttle = 1000):
        self.throttle = throttle
        self.motor1 = Motor(1, pin1, self.throttle)
        self.motor2 = Motor(2, pin2, self.throttle)
        self.motor3 = Motor(3, pin3, self.throttle)
        self.motor4 = Motor(4, pin4, self.throttle)
        self.motors = [self.motor1, self.motor2, self.motor3, self.motor4]
        print "----------------------------------------------------------"
        print "---------------Motors have been initialized---------------"
        print self.motor1.throttle
        print self.motor2.throttle
        print self.motor3.throttle
        print self.motor4.throttle
        print "----------------------------------------------------------"
        #self.diag

    def start(self):
        self.throttle = 1000
        for motor in self.motors:
            motor.setThrottle(self.throttle)

    def goUp(self):
        if self.throttle <= 2000:
            self.throttle += 10
            for motor in self.motors:
                motor.setThrottle(self.throttle)
        #self.motor1.increaseThrottle()
        #self.motor2.increaseThrottle()
        #self.motor3.increaseThrottle()
        #self.motor4.ince

    def goDown(self):
        if self.throttle >= 1100:
            self.throttle -= 10
            for motor in self.motors:
                motor.setThrottle(self.throttle)

    def stop(self):
        self.throttle = 0
        for motor in self.motors:
            motor.setThrottle(self.throttle)

    def setPins(self, pin1, pin2, pin3, pin4):
        self.motor1 = Motor(1, pin1, self.throttle)
        self.motor2 = Motor(2, pin2, self.throttle)
        self.motor3 = Motor(3, pin3, self.throttle)
        self.motor4 = Motor(4, pin4, self.throttle)
        #gc.collect()

#drone = Drone()

#drone.goUp()

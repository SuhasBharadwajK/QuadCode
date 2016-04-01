from RPIO import PWM
import time, readchar
from subprocess import call


throttle = 1000

pin1 = 17
pin2 = 27
pin3 = 25
pin4 = 21

pins = [17, 27, 25, 21]

motors = list()

class Motor:
    def __init__(self, pin):
        self.pin = pin
        self.command = "pigs s " + str(pin) + " " + str(throttle)
        print self.command
        call(["pigs", "s", str(pin), str(throttle)]);
        

    
    
    
def throttleUp():
    global throttle
    throttle += 10
    for motor in motors:
    #self.command = "pigs s " + str(pin) + " " + str(throttle)
        call(["pigs", "s", str(motor.pin), str(throttle)]);

def throttleDown():
    global throttle
    throttle -= 10
    for motor in motors:
    #self.command = "pigs s " + str(pin) + " " + str(throttle)
        call(["pigs", "s", str(motor.pin), str(throttle)]);

def switchOff():
    #:wq
    global throttle
    throttle = 0
    for motor in motors:
    #self.command = "pigs s " + str(pin) + " " + str(throttle)
        call(["pigs", "s", str(motor.pin), str(throttle)]);


#motors = [motor1, motor2, motor3, motor4]

def initialize():
    for pin in pins:
        motors.append(Motor(pin))

    '''time.sleep(5)
    for motor in motors:
        call(["pigs", "s", str(motor.pin), "1270"])

    time.sleep(5)
    for motor in motors:
        call(["pigs", "s", str(motor.pin), "0"])'''




if __name__ == '__main__':
    initialize()
    print "w > increase | s > decrease | q > quit"
    while(True):
        print throttle
        choice = readchar.readchar()
        if choice == "w":
            throttleUp()
        if choice == "s":
            throttleDown()
        if choice == "q":
            switchOff()
            exit()

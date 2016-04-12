from subprocess import call

class Motor:
    def __init__(self, number, pin, throttle):
        self.number = number
        self.pin = pin
        self.throttle = throttle

    def increaseThrottle(self):
        self.throttle += 10
        #print "Throttle of motor " + str(self.number) + " is " + str(self.throttle)
        call(["pigs", "s", str(self.pin), str(self.throttle)])

    def decreaseThrottle(self):
        self.throttle -= 10
        #print "Throttle of motor " + str(self.number) + " is " + str(self.throttle)
        call(["pigs", "s", str(self.pin), str(self.throttle)])

    def setThrottle(self, throttle):
        self.throttle = throttle
        #print "Throttle of motor " + str(self.number) + " is " + str(self.throttle)
        call(["pigs", "s", str(self.pin), str(self.throttle)])

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)


motor1 = GPIO.PWM(11, 50)
motor2 = GPIO.PWM(13, 50)
motor3 = GPIO.PWM(22, 50)
motor4 = GPIO.PWM(40, 50)

dutyCycle = 5

motor1.start(dutyCycle)
motor2.start(dutyCycle)
motor3.start(dutyCycle)
motor4.start(dutyCycle + 0.5)

print ('increase > w | decrease > s | quit > q')

running = True
while running:
	res = raw_input()

	'''motor1.ChangeDutyCycle(dutyCycle)
	motor2.ChangeDutyCycle(dutyCycle)
	motor3.ChangeDutyCycle(dutyCycle)
	motor4.ChangeDutyCycle(dutyCycle)'''
	if res == 'w':
	    dutyCycle = dutyCycle + 0.1
            motor1.ChangeDutyCycle(dutyCycle)
            motor2.ChangeDutyCycle(dutyCycle)
    	    motor3.ChangeDutyCycle(dutyCycle)
            motor4.ChangeDutyCycle(dutyCycle)
	        


	if res == 's':
    	    dutyCycle = dutyCycle - 0.1
	    motor1.ChangeDutyCycle(dutyCycle)
            motor2.ChangeDutyCycle(dutyCycle)
	    motor3.ChangeDutyCycle(dutyCycle)
            motor4.ChangeDutyCycle(dutyCycle)

        if res == 'q':
            running = False
            while dutyCycle > 4:
                dutyCycle = dutyCycle - 0.1
                motor3.ChangeDutyCycle(dutyCycle)
                motor4.ChangeDutyCycle(dutyCycle)
                motor2.ChangeDutyCycle(dutyCycle)
                motor1.ChangeDutyCycle(dutyCycle)
                time.sleep(0.05)
                
                        
                motor1.stop()
                motor2.stop()
                motor3.stop()
                motor4.stop()
                GPIO.cleanup()


        print ("Duty cycle is: " + str(dutyCycle))




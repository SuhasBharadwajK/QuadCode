from Drone import Drone
from PID import PID
from Sensors import IMU, Compass
import time
import readchar
import threading

drone = Drone(throttle = 1300)

imu = IMU()
compass = Compass()

initialRollAngle = imu.getRoll()
initialPitchAngle = imu.getPitch()
initialYawAngle = compass.getYaw()

PID_Roll = PID(initialRollAngle)
PID_Pitch = PID(initialPitchAngle)
PID_Yaw = PID(initialYawAngle)



def PIDThread(keepRunning = True):
    #global drone, imu, compass, yawAngleOriginal
    global drone, yawAngleOriginal    
    
    while keepRunning:
        imu = IMU()
        compass = Compass()


        rollAngle = imu.getRoll()
        pitchAngle = imu.getPitch()
        yawAngle = compass.getYaw()

       
        rollPID = int(PID_Roll.update(rollAngle))
        pitchPID = int(PID_Pitch.update(pitchAngle))
        yawPID = int(PID_Yaw.update(yawAngle))

        #print rollAngle, pitchAngle, yawAngle
        #print rollPID, pitchPID, yawPID
        #print int(rollPID), int(pitchPID), int(yawPID)

        drone.motor1.setThrottle(drone.throttle + pitchPID - yawPID) #Front
        drone.motor3.setThrottle(drone.throttle - pitchPID - yawPID) #Back
        drone.motor4.setThrottle(drone.throttle + rollPID + yawPID)  #Left
        drone.motor2.setThrottle(drone.throttle - rollPID + yawPID)  #Right

        time.sleep(0.1)
        #break



if __name__ == '__main__':

    try:
        PIDController = threading.Thread(target = PIDThread, args = ())
        PIDController.daemon = True
        PIDController.start()
        while(True):
            print "w > go up | s > go down | q > quit"

            choice = readchar.readchar()

            for motor in drone.motors:
                print motor.throttle

            if choice == "w":
                drone.goUp()
                #PIDa

            elif choice == "s":
                drone.goDown()

            elif choice == "q":
                #PIDController.stop()
                drone.stop()
                break
        '''for motor in drone.motors:
            motor.setThrottle(1300)'''
        #drone.goUp()
        #PIDThread()

    except KeyboardInterrupt:
        for motor in drone.motors:
            drone.stop()
        print "Ciao"
    
    '''drone = Drone()

    imu = IMU()
    compass = Compass()

    rollAngle = imu.getRoll()
    pitchAngle = imu.getPitch()
    yawAngle = compass.getYaw()

    PID_Roll = PID(0.0)
    PID_Pitch = PID(0.0)
    PID_Yaw = PID(yawAngle)

    rollPID = int(PID_Roll.update(rollAngle))
    pitchPID = int(PID_Pitch.update(pitchAngle))
    yawudoID = int(PID_Yaw.update(yawAngle))

    print rollAngle, pitchAngle, yawAngle
    print rollPID, pitchPID, yawPID
    print int(rollPID), int(pitchPID), int(yawPID)

    motor1.setThrottle(throttle + pitchPID - yawPID) #Front
    motor3.setThrottle(throttle - pitchPID - yawPID) #Back
    motor4.setThrottle(throttle + rollPID + yawPID)  #Left
    motor2.setThrottle(throttle - rollPID + yawPID)  #Right'''

   

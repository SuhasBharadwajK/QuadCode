import DroneControl
import readchar

drone = DroneControl.Drone()

#drone.setSpeeds(speed4 = 5.1)
drone.setSpeeds(4.95, 4.95, 5.1, 5.08)

drone.start()

print 'increase > w | decrease > s | stop > q'

while True:
    #option = raw_input()
    option = readchar.readchar()

    if option == 'w':
        drone.goUp()
    elif option == 's':
        drone.goDown()
    elif option == 'q':
        drone.stop()
        break

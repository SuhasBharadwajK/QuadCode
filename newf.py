import DronePackage

drone = DronePackage.Drone()


drone.start()

print 'increase > w | decrease > s | stop > q'
while True:
    option = raw_input()

    if option == 'w':
        drone.goUp()
    elif option == 's':
        drone.goDown()
    elif option == 'q':
        drone.stop()
        break

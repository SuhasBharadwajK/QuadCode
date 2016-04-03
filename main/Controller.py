from Drone import Drone
import time, readchar

if __name__ == '__main__':
    drone = Drone()

    while(True):
        print "w > go up | s > go down | q > quit"

        choice = readchar.readchar()

        if choice == "w":
            drone.goUp()

        elif choice == "s":
            drone.goDown()

        elif choice == "q":
            drone.stop()
            break

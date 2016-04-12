from Sensors import IMU
import time


#imu = IMU()

while True:
    imu = IMU()
    imu.wakeAndPrint()
    time.sleep(1)

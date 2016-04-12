#!/usr/bin/python

import smbus
import math
import time

class IMU:
    def __init__(self):
        self.power_mgmt_1 = 0x6b
        self.power_mgmt_2 = 0x6c
        self.bus = smbus.SMBus(1)
        self.address = 0x68

        self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)

        gyro_xout = self.read_word_2c(0x43)
        gyro_yout = self.read_word_2c(0x45)
        gyro_zout = self.read_word_2c(0x47)

        accel_xout = self.read_word_2c(0x3b)
        accel_yout = self.read_word_2c(0x3d)
        accel_zout = self.read_word_2c(0x3f)

        accel_xout_scaled = accel_xout / 16384.0
        accel_yout_scaled = accel_yout / 16384.0
        accel_zout_scaled = accel_zout / 16384.0

        self.roll = self.get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
        self.pitch = self.get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)



    def read_byte(self, adr):
        bus = self.bus
        return bus.read_byte_data(address, adr)

    def read_word(self, adr):
        bus = self.bus
        address = self.address
        high = bus.read_byte_data(address, adr)
        low = bus.read_byte_data(address, adr+1)
        val = (high << 8) + low
        return val

    def read_word_2c(self, adr):
        val = self.read_word(adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val

    def dist(self, a, b):
        return math.sqrt((a*a)+(b*b))

    def get_y_rotation(self, x, y, z):
        radians = math.atan2(x, self.dist(y, z))
        return -1 * radians * 180/math.pi
        #return -math.degrees(radians)

    def get_x_rotation(self, x, y, z):
        radians = math.atan2(y, self.dist(x, z))
        return math.degrees(radians)

    def get_roll(self, x, y, z):
        radians = math.atan2(y, z) * 180/math.pi
        return radians

    def get_pitch(self, x, y, z):
        radians = math.atan2(x, math.sqrt(y**2 + z**2))
        degrees = radians * 180 / math.pi
        return degrees

    def get_yaw(self, x, y, z):
        return (z / math.sqrt(x**2 + z**2)) / math.pi;

    def wakeAndPrint(self):
        self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)

        gyro_xout = self.read_word_2c(0x43)
        gyro_yout = self.read_word_2c(0x45)
        gyro_zout = self.read_word_2c(0x47)

        accel_xout = self.read_word_2c(0x3b)
        accel_yout = self.read_word_2c(0x3d)
        accel_zout = self.read_word_2c(0x3f)

        accel_xout_scaled = accel_xout / 16384.0
        accel_yout_scaled = accel_yout / 16384.0
        accel_zout_scaled = accel_zout / 16384.0

        roll = self.get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
        pitch = self.get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)

        print self.roll, self.pitch

        return (roll, pitch)

    def getRoll(self):
        #self.wakeAndPrint()
        return self.roll

    def getPitch(self):
        #self.wakeAndPrint()
        return self.pitch

class Compass:
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.address = 0x1e

    def read_byte(self, adr):
        return self.bus.read_byte_data(self.address, adr)

    def read_word(self, adr):
        address = self.address
        bus = self.bus
        high = bus.read_byte_data(address, adr)
        low = bus.read_byte_data(address, adr+1)
        val = (high << 8) + low
        return val

    def read_word_2c(self, adr):
        val = self.read_word(adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val

    def write_byte(self, adr, value):
        self.bus.write_byte_data(self.address, adr, value)

    def getYaw(self):

        self.write_byte(0, 0b01110000) # Set to 8 samples @ 15Hz
        self.write_byte(1, 0b00100000) # 1.3 gain LSb / Gauss 1090 (default)
        self.write_byte(2, 0b00000000) # Continuous sampling

        scale = 0.92

        x_out = self.read_word_2c(3) * scale
        y_out = self.read_word_2c(7) * scale
        z_out = self.read_word_2c(5) * scale

        bearing  = math.atan2(y_out, x_out) 
        if (bearing < 0):
            bearing += 2 * math.pi

        return math.degrees(bearing)



imu = IMU()
print imu.getRoll()
print imu.getPitch()
print imu.wakeAndPrint()

#compass = Compass()
#print compass.getYaw()

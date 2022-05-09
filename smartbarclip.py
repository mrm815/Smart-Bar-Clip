import random
import board
import busio
import time
import adafruit_adxl34x

#Gyro_Address=0x53
i2c = board.I2C()
gyro = adafruit_adxl34x.ADXL345(i2c)

multi=0.004
gravity=9.80665
ratio=multi*gravity

def setup():
    print("All peripherals and sensors have been set up")
    return True

def buzzer_long():
    print("The buzzer is playing a long tone")

def buzzer_pulse():
    print("The buzzer is playing a pulsing tone")

def gyro_x():
    print("X: ",(gyro.raw_x)*ratio)
    return ((gyro.raw_x)*ratio)

def gyro_y():
    print("Y: ",(gyro.raw_y)*ratio)
    return ((gyro.raw_y)*ratio)
    
def gyro_z():
    print("Z: ",(gyro.raw_z)*ratio)
    return ((gyro.raw_z)*ratio)



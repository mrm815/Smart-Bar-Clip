import random
import board
import busio
import adafruit_adxl34x

Gyro_Address=0x53
i2c = board.I2C()
gyro = adafruit_adxl34x.ADXL345(i2c)

def setup():
    print("All peripherals and sensors have been set up")
    return True

def buzzer_long():
    print("The buzzer is playing a long tone")

def buzzer_pulse():
    print("The buzzer is playing a pulsing tone")

def gyro_x():
    return random.randint(0,100)

try:
    while True:
        print(gyro.acceleration)
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()

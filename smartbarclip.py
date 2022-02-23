import random

def setup():
    print("All peripherals and sensors have been set up")
    return True

def buzzer_long():
    print("The buzzer is playing a long tone")

def buzzer_pulse():
    print("The buzzer is playing a pulsing tone")

def gyro_x():
    return random.randint(0,100)

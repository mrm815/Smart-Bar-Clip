import smartbarclip as sbc
import time


sbc.setup()

x_range=4
y_range=4

def dlift():
  if ((-x_range)<sbc.gyro_x()<x_range):
    print(" X Form error")
    sbc.buzzer_long()
  if ((-y_range)<sbc.gyro_y()<y_range):
    print("Y Form Error")
    sbc.buzzer_pulse()
    
try:
  while True:
    #print(sbc.gyro_x(),sbc.gyro_y(),sbc.gyro_z())
    #time.sleep(1)
    dlift()
    time.sleep(0.5)
except KeyboardInterrupt:
  GPIO.cleanup()
  sys.exit()

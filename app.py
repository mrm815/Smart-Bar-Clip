import smartbarclip as sbc
import time

sbc.setup()

x_range=4
y_range=4

def dlift():
  if (((-x_range)<sbc.gyro_x()<x_range) or ((-y_range)<sbc.gyro_y()<y_range)):
    print("Form error")
    
try:
  while True:
    #print(sbc.gyro_x(),sbc.gyro_y(),sbc.gyro_z())
    #time.sleep(1)
    dlift()
except KeyboardInterrupt:
  GPIO.cleanup()
  sys.exit()

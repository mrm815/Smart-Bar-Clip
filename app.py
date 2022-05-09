import smartbarclip as sbc

sbc.setup()

x_range=20
y_range=20
z_range= 20

def dlift():
  if (((-z_range)<sbc.gyro_z()<z_range) or ((-y_range)<sbc.gyro_y()<y_range)):
    print("Form error")
    
try:
  while True:
    sbc.gyro_x()
    sbc.gyro_y()
    sbc.gyro_z()
except KeyboardInterrupt:
  GPIO.cleanup()
  sys.exit()

import smartbarclip as sbc
import time

sbc.setup()

sbc.buzzer_long()
time.sleep(5)
sbc.buzzer_pulse

x_axis=sbc.gyro_x()
print("The bar is moving at",str(x_axis),"m/s^2")

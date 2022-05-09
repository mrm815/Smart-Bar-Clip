import smartbarclip as sbc
import time
import RPi.GPIO as GPIO
import sys
from flask import Flask, render_template, redirect, request


sbc.setup()

x_range=4
y_range=4

def dlift():
  if (not((-x_range)<sbc.gyro_x()<x_range)):
    print(" X Form error")
    sbc.buzzer_long()
  if (not((-y_range)<sbc.gyro_y()<y_range)):
    print("Y Form Error")
    sbc.buzzer_pulse()

app= Flask(__name__, static_folder='assets')

@app.route("/")
def home():
  return redirect("/templates/index")

@app.route("templates/index")
def home_template():
  return render_template("index.html")



if __name__ == "__main__":
  app.run(host='0.0.0.0',port=80,debug=True, threaded= True)

try:
  while True:
    #print(sbc.gyro_x(),sbc.gyro_y(),sbc.gyro_z())
    #time.sleep(1)
    dlift()
    time.sleep(0.5)
except KeyboardInterrupt:
  GPIO.cleanup()
  sys.exit()

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

global buzz
buzz="Unknown"

@app.route("/")
def home():
  return redirect("/templates/index")

@app.route("/templates/index")
def home_template():
  return render_template("index.html")

@app.route("/templates/gyro")
def gyro_template():
  x=sbc.gyro_x()
  y=sbc.gyro_y()
  z=sbc.gyro_z()
  return render_template("gyro.html",xlevel=x,ylevel=y,zlevel=z)

@app.route("/templates/buzzer")
def buzzer_template():
  on=""
  off=""
  if buzz=="Armed":
    on="disabled"
    off=""
  elif buzz=="Inactive":
    on=""
    off="disabled"
  return render_template("buzzer.html",buzzerstatus=buzz, ondisabled=on, offdisabled=off)

@app.route("/buzzer/<int:action>")
def buzzer_act(action):
  global buzz
  if action==0:
    buzz="Armed"
    print("Buzzer is armed")
    while action==0:
      dlift()
  elif action==1:
    buzz="Inactive"
    print("Buzzer is not armed")
  return redirect("/templates/buzzer")

#if __name__ == "__main__":
app.run(host='0.0.0.0',port=80,debug=True, threaded= True)

#try:
 # while True:
  #  app.run(host='0.0.0.0',port=80,debug=True, threaded= True)
    #print(sbc.gyro_x(),sbc.gyro_y(),sbc.gyro_z())
    #time.sleep(1)
    #dlift()
    #time.sleep(0.5)
#except KeyboardInterrupt:
 # GPIO.cleanup()
  #sys.exit()

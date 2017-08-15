#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time, threading
import serial

sensor = serial.Serial('/dev/ttyACM0', 115200)
def update():
    threading.Timer(5.0, update).start()
    print(sensor.readline().decode().strip())

update()

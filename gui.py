#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: franckysolo
import serial
from tkinter import *

bgColor = '#212121'
# connexion à l'arduino
sensor = serial.Serial('/dev/ttyACM0', 115200)
# Création de la fénêtre
root = Tk()
root['bg'] = bgColor
root['padx'] = 20
root['pady'] = 20
root.title('Interface capteur Adafruit AM2302')

"""
Construit un label pour l'affichage d'une valeur de capteur
"""
def build_label(title, row, col):
    lf = LabelFrame(root, text=title, bg=bgColor, fg="white")
    lf.grid(row=row, column=col, padx=20, pady=20)
    label = Label(lf)
    label.config(text="")
    label.config(fg="#39dac2")
    label.config(bg=bgColor)
    label.config(padx=10)
    label.config(pady=10)
    label.pack()
    return label

"""
Callback: met à jour les valeurs du capteur dans la fenêtre
"""
def update_label():
    data = sensor.readline().decode().strip().split(':')
    labelHumidity.config(text=data[0] + '%')
    labelTmp.config(text=data[1] + '°C')
    root.after(1000, update_label)

# run the script
labelHumidity = build_label("Humidité", 0, 0)
labelTmp = build_label("Température", 0, 1)

update_label()

root.mainloop()

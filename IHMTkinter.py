# ! /usr/bin/python3

import serial
import time
from tkinter import *
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
from graph import *

port = '/dev/ttyACM0'
baudrate = 115200
serBuffer = ""


# TODO Tester avec connexion au STM32
# TODO revoir toute l'organisationd des emplacements des modules

########################################################################
#                        FUNCTIONS
########################################################################

def onPushTest():
    var = int(strEstimated.get())
    strEstimated.set(var + 1)
    print("value récupérée du checkbutton du moteur : ")
    print(x.get())
    x.set(not x.get())


########################################################################
#                             MAIN
########################################################################

if __name__ == "__main__":
    # try:
    #    ser = serial.Serial(port, baudrate, bytesize=8, parity='N', stopbits=1, timeout=None, rtscts=False, dsrdtr=False)
    #    print("serial port " + ser.name + " opened")
    # except Exception:
    #    print("error open serial port: " + port)
    #    exit()

    ui = Tk()

    ui.title("IPS - Déformation par jauge")
    ui.geometry("1000x500")
    # ui.resizable(width=0, height=0)

    # zone avec graphique de la déformation en fonction de la donnée reçu
    # essayer de faire le graphique évolutif
    ui.graph = Frame(ui, width=150, bg="#ababab")
    ui.graph.grid(row=0, column=0, rowspan=2, sticky="ns")

    graph(ui)

    # Label : estimation de poids
    labelWeightEstimation = Label(ui, text="Estimation du poids (en g)", font=("Arial", 15), fg="black")
    labelWeightEstimation.grid(row=0, column=1)
    # labelWeightEstimation.pack()

    # zone de texte avec "poid : *zone de texte modifiable* g"
    strEstimated = StringVar(value="0")
    WeightEntry = Entry(ui, textvariable=strEstimated, font=("Arial", 15), fg="black")
    WeightEntry.grid(row=0, column=2)
    # WeightEntry.pack()

    testButton = Button(ui, text="add +1", font=("Arial", 12), background="seagreen", fg="black", bd=2, relief=RAISED,
                        command=onPushTest)
    testButton.grid(row=1, column=1)
    # avoir une zone "moteur"
    ui.servomoteur = Frame(ui, width=150, bg="#ababab")
    ui.servomoteur.grid(row=0, column=2)
    # une case cochable pour indiquer si le moteur est en train  de tourner
    x = IntVar()
    moteurButton = Checkbutton(ui, text="Moteur en route", height=10, width=10, variable=x)
    moteurButton.grid(row=2, column=2)
    # avoir une zone qui indique la vitesse envoyée au moteur

    labelToSendMes = Label(ui, text="Message to Send", font=("Arial", 10), fg="black")
    # labelToSendMes.pack()

    strToSend = StringVar()
    toSendEntry = Entry(ui, textvariable=strToSend)
    # toSendEntry.pack()

    # ui.after(1,receive)
    ui.mainloop()  # MAIN LOOP

########################################################################
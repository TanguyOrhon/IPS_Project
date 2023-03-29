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
from func import *

port = '/dev/ttyACM0'
baudrate = 115200
serBuffer = ""

########################################################################
#                             MAIN
########################################################################

if __name__ == "__main__":

    #try: 
    #    ser = serial.Serial(port, baudrate, bytesize=8, parity='N', stopbits=1, timeout=None, rtscts=False, dsrdtr=False)
    #    print("serial port " + ser.name + " opened")
    #except Exception:
    #    print("error open serial port: " + port)
    #    exit()

    ui = Tk()
    ui.title("IPS - Déformation par jauge")
    ui.geometry("1000x500")
    ui.graph = Frame(ui, width=150, bg="#ababab")
    ui.graph.grid(row=0, column=0, rowspan=2, sticky="ns")

    ui.servomoteur = Frame(ui, width=150, bg="#ababab")
    ui.servomoteur.grid(row=0, column=2)

    begin = Func()
    begin.graph(ui)
    begin.weight(ui)
    begin.button(ui)

    ui.mainloop()
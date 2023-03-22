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
#                        FUNCTIONS
########################################################################

def begin_ui():
    ui = Tk()
    ui.title("IPS - Déformation par jauge")
    ui.geometry("1000x500")
    ui.graph = Frame(ui, width=150, bg="#ababab")
    ui.graph.grid(row=0, column=0, rowspan=2, sticky="ns")
    ui.servomoteur = Frame(ui, width=150, bg="#ababab")
    ui.servomoteur.grid(row=0, column=2)
    # ui.resizable(width=0, height=0)
    return ui


def begin_func(ui):
    begin = Func()
    begin.graph(ui)
    begin.weight(ui)
    begin.button(ui)
    return begin


def run():
    ui = begin_ui()
    begin = begin_func(ui);
    ui.mainloop()  # MAIN LOOP

########################################################################
#                             MAIN
########################################################################

if __name__ == "__main__":
    run()

########################################################################

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
from stm import *



########################################################################
#                        FUNCTIONS
########################################################################

def begin_ui():
    ui = Tk()
    ui.title("IPS - Déformation par jauge")
    ui.geometry("1300x700")
    ui.graph = Frame(ui, width=150, bg="#ababab")
    ui.graph.grid(row=0, column=0, rowspan=2, sticky="ns")
    ui.servomoteur = Frame(ui, width=150, bg="#ababab")
    ui.servomoteur.grid(row=0, column=2)
    # ui.resizable(width=0, height=0)
    return ui

def begin_func(ui,stm):
    begin = Func(stm)
    begin.graph(ui)
    begin.weight(ui)
    begin.button(ui)
    #begin.animate(ui)
    return begin

def begin_stm(ui):
    stm = Stm(ui)
    stm.display()
    return stm

def run():
    ui = begin_ui()
    stm = begin_stm(ui)
    begin_func(ui,stm)
    ui.mainloop()  # MAIN LOOP

########################################################################
#                             MAIN
########################################################################

if __name__ == "__main__":
    run()

########################################################################

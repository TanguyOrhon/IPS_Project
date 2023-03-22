#! /usr/bin/python3
 
import serial
import time
from tkinter import *  
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
 
port='/dev/ttyACM0'
baudrate=115200
serBuffer = ""

 
########################################################################
#                             MAIN
########################################################################
 
if  __name__ == "__main__" :
 
    #try: 
    #    ser = serial.Serial(port, baudrate, bytesize=8, parity='N', stopbits=1, timeout=None, rtscts=False, dsrdtr=False)
    #    print("serial port " + ser.name + " opened")
    #except Exception:
    #    print("error open serial port: " + port)
    #    exit()
 
    ui=Tk()
 
    ui.title("IPS - Déformation par jauge")
    ui.geometry("400x400")

    #GRAPH
    
    k = 2*np.pi
    w = 2*np.pi
    dt = 0.001

    xmin = 0
    xmax = 100
    nbx = 100
    x = np.linspace(xmin, xmax, nbx)

    fig = plt.figure() # initialise la figure
    line, = plt.plot([], []) 
    plt.xlim(xmin, xmax)
    plt.ylim(298, 302)

    def animate(i): 
        t = i * dt
        y = np.cos(k*x -w*t ) + 300
        line.set_data(x, y)
        return line,

    ani = animation.FuncAnimation(fig, animate, frames=10000,
                                interval=1, blit=True, repeat=False)
   
    
    matplotlib.use("TkAgg")
    canvas = FigureCanvasTkAgg(fig, ui)
    canvas.get_tk_widget().pack()
 
    #ui.after(1,receive)
    ui.mainloop()       # MAIN LOOP


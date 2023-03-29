import serial
import time
from tkinter import *
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib


class Func:
    def __init__(self):
        self.strEstimated = StringVar(value="0")
        self.x = IntVar()

    def animate(i):
        k = 2*np.pi
        w = 2*np.pi
        dt = 0.001
        xmin = 0
        xmax = 100
        nbx = 100
        x = np.linspace(xmin, xmax, nbx)
        line, = plt.plot([], [])
        t = i * dt
        y = np.cos(k*x -w*t ) + 300
        line.set_data(x, y)
        plt.xlim(xmin, xmax)
        plt.ylim(298, 302)
        return line,

    def graph(self, ui):
    
        figure = plt.figure()
        
        anim = animation.FuncAnimation(figure, self.animate, frames=10000, interval=1, blit=True, repeat=False)
        
        matplotlib.use("TkAgg")
        canvas = FigureCanvasTkAgg(figure, ui.graph)
        canvas.get_tk_widget().grid(row=0, column=0)

    def weight(self, ui):
        # Label : estimation de poids
        labelWeightEstimation = Label(ui, text="Estimation du poids (en g)", font=("Arial", 15), fg="black")
        labelWeightEstimation.grid(row=0, column=1)
        # labelWeightEstimation.pack()

        # zone de texte avec "poid : *zone de texte modifiable* g"
        WeightEntry = Entry(ui, textvariable=self.strEstimated, font=("Arial", 15), fg="black")
        WeightEntry.grid(row=0, column=2)
        # WeightEntry.pack()

    def button(self, ui):
        moteurButton = Checkbutton(ui, text="Moteur en route", height=10, width=10, variable=self.x)
        moteurButton.grid(row=2, column=2)
        testButton = Button(ui, text="add +1", font=("Arial", 12), background="seagreen", fg="black", bd=2,
                            relief=RAISED,
                            command=self.onPushTest)
        testButton.grid(row=1, column=1)

    def onPushTest(self):
        var = int(self.strEstimated.get())
        self.strEstimated.set(var + 1)
        print("value récupérée du checkbutton du moteur : ")
        print(self.x.get())
        self.x.set(not self.x.get())
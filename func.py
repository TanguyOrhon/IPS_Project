import serial
import time
from tkinter import *
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
#import matplotlib.animation as animation
import matplotlib
import random


class Func:
    def __init__(self,stm):
        self.strEstimated = StringVar(value="0")
        self.x = IntVar()
        self.x_values = []
        self.y_values = []
        self.xlimadd = 100
        self.xlim = self.xlimadd
        self.stm = stm
        self.yval = 0
        
    def animate(self,canvas,ui,i=0):
        self.x_values.append(i)
        if (self.stm.strReceived[0].get()):
            self.yval = int(self.stm.strReceived[0].get())
        self.y_values.append(self.yval)
        if (i == self.xlim):
            plt.xlim(self.xlim,self.xlim+self.xlimadd)
            self.xlim = self.xlim+self.xlimadd
        plt.plot(self.y_values, color='black')
        canvas.draw()
        ui.after(50, self.animate, canvas, ui, i+1)

    def graph(self, ui):
        
        fig=plt.figure()
        plt.xlim(0,self.xlim)
        plt.ylim(-1,6) 
        
        matplotlib.use("TkAgg")
        canvas = FigureCanvasTkAgg(fig, ui)
        canvas.get_tk_widget().grid(row=0, column=0)
        self.animate(canvas,ui)


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

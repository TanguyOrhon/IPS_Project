import serial
import time
from tkinter import *
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
# import matplotlib.animation as animation
import matplotlib
import random


class Func:
    def __init__(self, ui, stm):
        self.strEstimated = StringVar(value="0")
        self.x = IntVar()
        self.x_values = []
        self.y_values = []
        self.xlimadd = 100
        self.xlim = self.xlimadd
        self.stm = stm
        self.yval = 0
        self.frame_action = LabelFrame(ui, bd=0, text="Estimations",font=("Arial", 14), bg='grey70')
        self.frame_action.place(x = 10, rely = 0.55, relwidth=0.9, relheight=0.4)
        self.weightInt = IntVar()
        self.degreInt = IntVar()
        self.frame_graph = LabelFrame(ui, bd=0, text="Graphique de déformation de la lame",font=("Arial", 14), bg='grey70')
        self.frame_graph.place(x = 10, y = 10, relwidth=0.9, relheight=0.5)

    def animate(self, canvas, ui, i=0):
        self.x_values.append(i)
        if (self.stm.ADC_Value):
            self.yval=float(self.stm.ADC_Value)
            # print(self.yval)
            print((self.stm.ADC_Value-350.98)*100*5)
            self.weightInt.set((self.stm.ADC_Value-350.98)*100*5)
            self.degreInt.set((self.stm.angleServomoteur-1000)/11.11111)
        self.y_values.append(self.yval)
        if (i == self.xlim):
            plt.xlim(self.xlim, self.xlim + self.xlimadd)
            self.xlim = self.xlim + self.xlimadd
        plt.plot(self.y_values, color='black')
        canvas.draw()
        ui.after(50, self.animate, canvas, ui, i + 1)

    def graph(self, ui):
        fig = plt.figure()
        plt.xlim(0, self.xlim)
        plt.ylim(350.98,351.3)
        canvas = FigureCanvasTkAgg(fig, self.frame_graph)
        canvas.get_tk_widget().place(x=20, y=20, relwidth=0.9, relheight=0.9)
        self.animate(canvas,ui)        

    def weight(self):
        # scale : estimation de poids
        weight_scale = Scale(self.frame_action, label="estimation de la masse (en grammes)",from_=0,to=105, variable=self.weightInt, width=50, tickinterval=5, bg='LightSkyBlue1', orient = HORIZONTAL)
        weight_scale.place(x=10, y=10, relwidth=0.9,relheight=0.4)

    def degre(self):
        # scale : degré d'inclinaison du servomoteur
        degre_scale = Scale(self.frame_action, label="inclinaison du servomoteur (en degre)",from_=-90,to=90, variable=self.degreInt, width=50, tickinterval=10, bg='PaleGreen1', orient = HORIZONTAL)
        degre_scale.place(x=10, rely=0.6, relwidth=0.9,relheight=0.4)

    def button(self, ui):
        moteurButton = Checkbutton(ui, text="Moteur en route", height=10, width=10, variable=self.x)
        # moteurButton.grid(row=2, column=2)
        testButton = Button(ui, text="add +1", font=("Arial", 12), background="seagreen", fg="black", bd=2,
                            relief=RAISED,
                            command=self.onPushTest)
        testButton.place(x=100, y=60, width=80,height=40)

    def onPushTest(self):
        print(type(self.weight))
        self.stm.ADC_Value = float(random.randint(35098,35127))/100
        self.stm.angleServomoteur = random.randint(0,2000)
        print(self.stm.ADC_Value)
        self.degreInt.set(45)
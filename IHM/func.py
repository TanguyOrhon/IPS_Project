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
    def __init__(self,stm, ui):
        self.strEstimated = StringVar(value="0")
        self.x = IntVar()
        self.x_values = []
        self.y_values = []
        self.xlimadd = 100
        self.xlim = self.xlimadd
        self.stm = stm
        self.yval = 0
        self.frame_action = LabelFrame(ui, bd=5, text="Actions",font=("Arial", 14))
        self.frame_action.place(x = 10, rely = 0.55, relwidth=0.9, relheight=0.4)
        
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
        frame_graph = LabelFrame(ui, bd=5, text="Graphique de déformation de la lame",font=("Arial", 14))
        frame_graph.place(x = 10, y = 10, relwidth=0.9, relheight=0.5)
        fig=plt.figure()
        plt.xlim(0,self.xlim)
        plt.ylim(-1,6)
        
        canvas = FigureCanvasTkAgg(fig, frame_graph)
        canvas.get_tk_widget().place(x=20, y=20, relwidth=0.9, relheight=0.9)
        self.animate(canvas,ui)


    def weight(self, ui):
        # scale : estimation de poids
        weight = 10
        weight_scale = Scale(self.frame_action, label="estimation du poids",from_=0,to=105, variable=weight, width=50, tickinterval=5, bg='LightSkyBlue1', orient = HORIZONTAL)
        weight_scale.place(x=10, y=10, relwidth=0.9,relheight=0.4)

        # zone de texte avec "poid : *zone de texte modifiable* g"
        # WeightEntry = Entry(self.frame_action, textvariable=self.strEstimated, font=("Arial", 15), fg="black")
        # WeightEntry.place(relx=0.3, y=120, relwidth=0.5,height=40)

    def degre(self, ui):
        # scale : degré d'inclinaison du servomoteur
        degre = 10
        degre_scale = Scale(self.frame_action, label="inclinaison du servomoteur (en degre)",from_=0,to=90, variable=degre, width=50, tickinterval=5, bg='PaleGreen1', orient = HORIZONTAL)
        degre_scale.place(x=10, rely=0.6, relwidth=0.9,relheight=0.4)

    def button(self, ui):
        moteurButton = Checkbutton(self.frame_action, text="Moteur en route", height=10, width=10, variable=self.x)
        # moteurButton.place(x=10, y = 10, width=200,height=40)
        testButton = Button(self.frame_action, text="add +1", font=("Arial", 12), background="seagreen", fg="black", bd=2,
                            relief=RAISED,
                            command=self.onPushTest)
        # testButton.place(x=10, y=60, width=80,height=40)

    def onPushTest(self):
        var = int(self.strEstimated.get())
        self.strEstimated.set(var + 1)
        print("value récupérée du checkbutton du moteur : ")
        print(self.x.get())
        self.x.set(not self.x.get())

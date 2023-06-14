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

class Stm:
    def __init__(self, ui):
        self.port = 'COM7'
        self.baudrate = 115200
        self.serBuffer = ""
        self.ser = 0
        self.ui = ui
        self.ADC = StringVar()
        self.VoltageData = 0
        self.ADC_Value = 0
        self.angleServomoteur=0
        self.config()

    def config(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate, bytesize=8, parity='N', stopbits=1, timeout=None, rtscts=False,
                                dsrdtr=False)
            print("serial port " + self.ser.name + " opened")
        except Exception:
            print("error open serial port: " + self.port)
            exit()

    def receive(self):
        #self.VoltageData = self.ser.readline().decode().strip()
        self.ADC_Value = self.ser.readline().decode().strip()
        self.angleServomoteur = self.ser.readline().decode().strip()
        self.ADC.set(self.ADC_Value)
        self.ui.after(10, self.receive)

    def display(self):
        receivedEntry = Entry(self.ui, textvariable=self.ADC,width=60 )
        #receivedEntry.grid(row=4, column=5)
        #receivedEntry2 = Entry(self.ui, textvariable=self.ADC_Value,width=60 )
        #receivedEntry2.grid(row=5, column=5)
        self.receive()
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
        self.port = 'COM5'
        self.baudrate = 115200
        self.serBuffer = ""
        self.ser = 0
        self.ui = ui
        self.strReceived = StringVar()
        self.strReceived2 = StringVar()
        self.test1 = 0
        self.test2 = 0
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
        reading = []
        reading2 = []
        i = 0
        while self.ser.inWaiting() > 0:
            if self.ser.inWaiting() > 0:
                c = self.ser.read(1).decode()
                if len(c) == 0:
                     break

                if c == 'b':
                    i = 1
                elif c == 'a':
                    i = 2
                elif i == 1 :
                    self.reading(reading, c)
                elif i == 2 :
                    self.reading(reading2, c)
                # check if character is a delimeter

            time.sleep(0.001)
            #self.strReceived.set(reading)
            self.strReceived.set(reading)
            self.test1 = Entry(self.ui, textvariable=self.strReceived, width=60)
            self.strReceived2.set(reading2)
            self.test2 = Entry(self.ui, textvariable=self.strReceived, width=60)
            self.ser.flush()
        self.ui.after(1, self.receive)


    def display(self):
        receivedEntry = Entry(self.ui, textvariable=self.strReceived,width=60 )
        receivedEntry.grid(row=4, column=5)
        receivedEntry2 = Entry(self.ui, textvariable=self.strReceived2,width=60 )
        receivedEntry2.grid(row=5, column=5)
        self.ui.after(1, self.receive)

    def reading(self, r, c):
        if c == '\r':
            r.append()  # don't want returns. chuck it
        elif c == '\n':
            # serBuffer += "\n"  # add the newline to the buffer
            # log.insert('0.0', serBuffer)
            r.append("")  # empty the buffer
        else:
            r.append(c)

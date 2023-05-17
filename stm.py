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
        self.strReceived = [StringVar()]#StringVar()
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
        while (self.ser.inWaiting() > 0):
            if (self.ser.inWaiting() > 0):
                c = self.ser.read(1)
                if len(c) == 0:
                     break

                    # get the buffer from outside of this function
                global serBuffer

                # check if character is a delimeter
                if c == '\r':
                    reading.append()  # don't want returns. chuck it
                elif c == '\n':
                    # serBuffer += "\n"  # add the newline to the buffer
                    # log.insert('0.0', serBuffer)
                    reading.append("")  # empty the buffer
                else:
                    reading.append(c)
            time.sleep(0.001)
            #self.strReceived.set(reading)
            i=0
            val = [] #=(int.from_bytes(reading[0],'big'))
            while (i<len(reading)):
                val[i] = (int.from_bytes(reading[i],'big'))
                self.strReceived[i].set(val[i])
                i+=1
            self.ser.flush()
        self.ui.after(1, self.receive)


    def display(self):
        receivedEntry = Entry(self.ui, textvariable=self.strReceived,width=60 )
        receivedEntry.grid(row=4, column=5)
        self.ui.after(1, self.receive)
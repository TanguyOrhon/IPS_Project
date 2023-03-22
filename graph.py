import serial
import time
from tkinter import *
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib

def graph(ui):
    matplotlib.use("TkAgg")
    figure = Figure(figsize=(5, 5), dpi=100)
    plot = figure.add_subplot(1, 1, 1)
    plot.plot(0.5, 0.3)
    canvas = FigureCanvasTkAgg(figure, ui.graph)
    canvas.get_tk_widget().grid(row=0, column=0)



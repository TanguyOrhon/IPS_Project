# coding: utf-8
import sys
major=sys.version_info.major
minor=sys.version_info.minor
if major==2 and minor==7 :
    import Tkinter as tk
    import tkFileDialog as filedialog
elif major==3 :
    import tkinter as tk
    from tkinter import filedialog
else :
    if __name__ == "__main__" :
        print("Your python version is : ",major,minor)
        print("... I guess it will work !")
    import tkinter as tk
    from tkinter import filedialog 

from math import pi,sin
from observer import Observer
from generator import Generator

class Screen(Observer) :
    def __init__(self,parent,bg="white",width=200,height=100,xy = False):
        self.parent=parent
        self.bg=bg
        self.name="X"
        self.signal=[]
        self.width,self.height=width,height
        self.units=1
        self.gui()
        self.xy = xy
        self.screen.bind("<Configure>",self.resize)
        self.x,self.y,self.radius=0,0,10
        self.canvas=tk.Canvas(parent,bg=bg)
        self.spot=self.canvas.create_oval(
            self.x-self.radius,self.y-self.radius,
            self.x+self.radius,self.y+self.radius,
            fill='yellow',outline='black',tags="spot")
        self.width=int(self.canvas.cget("width"))
        self.height=int(self.canvas.cget("height"))

    def gui(self) :
        print("Screen.gui()")
        self.screen=tk.Canvas(self.parent, bg=self.bg,width=self.width,height=self.height)

    def update(self,subject):
        print("Screen.update()")
        self.signal = subject.signal
        if (self.xy == False):
            self.plot_signal(subject.name,subject.signal)
        else:
            self.plot_signal_XY(subject.name,subject.signal)
    

    def plot_signal(self,name="X",signal=[],color="PaleTurquoise4"):
        print("Screen.plot()")
        width,height=self.width,self.height
        if signal and len(signal)>1:
            #if self.screen.find_withtag(name) :
            self.screen.delete(name)
            plots=[(x*width,(height/self.units)*y+height/2) for (x,y) in signal]
            self.screen.create_line(plots,fill=color,smooth=1,width=3,tags=name)

    def plot_signal_XY(self,name="XY",signal=[],color="PaleTurquoise4"):
        print("Screen.plot()")
        width,height=self.width,self.height
        if signal and len(signal)>1:
            #if self.screen.find_withtag(name) :
            self.screen.delete(name)
            plots = [(x*width+width/2, y*height + height/2) for (x, y) in signal]
            self.screen.create_line(plots,fill=color,smooth=1,width=3,tags=name)

    def create_grid(self, tiles = 8):
        print("Screen.create_grid()")
        if self.screen.find_withtag("grid") :
            self.screen.delete("grid")         
        self.units=tiles
        tile_x=self.width/tiles
        for t in range(1,tiles+1):
            x =t*tile_x
            self.screen.create_line(x,0,x,self.height,tags="grid")
            self.screen.create_line(x,self.height/2-10, x,self.height/2+10,width=3,tags="grid")
        tile_y=self.height/tiles
        for t in range(1,tiles+1):
            y =t*tile_y
            self.screen.create_line(0,y,self.width,y,tags="grid")
            self.screen.create_line(self.width/2-10,y,self.width/2+10,y, width=3,tags="grid")

    def resize(self,event):
        print("Screen.resize()")
        if event:
            self.width,self.height=event.width,event.height
            self.screen.delete("grid")
            self.create_grid(self.units)
            self.plot_signal(signal=self.signal)
        pass

    def get_canvas(self) :
        return self.canvas

    def animate_spot(self,canvas,signal,i=0):
        print("Screen.animate_spot()")
        width,height=canvas.winfo_width(),canvas.winfo_height()
        msec=5
        if i==len(signal) :
            i=0
        x,y=signal[i][0]*width, height/2*(signal[i][1]+1)
        self.canvas.coords(self.spot,x,y,x+self.radius,y+self.radius)
        after_id=self.parent.after(msec, self.animate_spot,canvas,signal,i+1)
        return after_id
    
    def layout(self) :
        print("Screen.layout()")
        self.screen.pack(side = "top", expand=1, fill="both", padx=6)
        #self.canvas.pack()

if   __name__ == "__main__" :
    root=tk.Tk()
    model=Generator()
    view=Screen(root)
    view.create_grid()
    view.layout()
    model.attach(view)
    model.generate()
    view.animate_spot(view.get_canvas(), model.get_signal())
    
    root.mainloop()

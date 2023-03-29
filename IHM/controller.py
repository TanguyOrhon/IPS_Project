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
from screen import Screen
from generator import Generator

class Controller(object) :
    def __init__(self, model, view):
        self.model,self.view=model,view
        self.gui()
        self.actions_binding()

    def gui(self) :
        print("Controller.gui()")
        # premier signal
        self.frame1=tk.LabelFrame(self.view.parent,text= "Contrôleurs")
        self.var_mag=tk.IntVar()
        self.var_mag.set(self.model.m)
        self.scaleA=tk.Scale(self.frame1,variable=self.var_mag,
                             label="Amplitude",
                             orient="horizontal",length=250,
                             from_=0,to=4,tickinterval=1,
                             bg = "PaleTurquoise1")

        self.var_freq=tk.IntVar()
        self.var_freq.set(self.model.f)
        self.scaleB=tk.Scale(self.frame1,variable=self.var_freq,
                             label="Fréquence",
                             orient="horizontal",length=250,
                             from_=0,to=5,tickinterval=1,
                             bg = "PaleTurquoise2")

        self.var_phase=tk.IntVar()
        self.var_phase.set(self.model.p)
        self.scaleC=tk.Scale(self.frame1,variable=self.var_phase,
                             label="Phase",
                             orient="horizontal",length=250,
                             from_=0,to=2*pi,tickinterval=pi/3,
                             bg = "PaleTurquoise3")
        
        self.var_harmo=tk.IntVar()
        self.var_harmo.set(self.model.harmonics)
        self.scaleD=tk.Scale(self.frame1,variable=self.var_harmo,
                             label="Harmonique",
                             orient="horizontal",length=250,
                             from_=0,to=5,tickinterval=1,
                             bg = "PaleTurquoise4")
        
        self.var_samples=tk.IntVar()
        self.var_samples.set(self.model.samples)
        self.scaleE=tk.Scale(self.frame1,variable=self.var_samples,
                             label="Echantillons",
                             orient="horizontal",length=250,
                             from_=0,to=200,tickinterval=50,
                             bg = "teal")
        
        self.frame2=tk.LabelFrame(self.view.parent,text="Harmonics")
        self.radio_var=tk.IntVar()
        btn=tk.Radiobutton(self.frame2,text="All", variable=self.radio_var,value=1,command=self.activate_button)
        btn.select()
        btn.pack(anchor ="w")
        btn=tk.Radiobutton(self.frame2,text="Odd", variable=self.radio_var,value=2,command=self.activate_button)
        btn.pack(anchor ="w")
        self.nb_ech_var=tk.IntVar()

        self.frame3=tk.LabelFrame(self.view.parent,text="Nb echantillons")
        self.nb_ech_var=tk.Entry(self.frame3)
        self.nb_ech_var.bind("<Return>", self.update_echantillon)
        self.nb_ech_var.pack()
        
    def actions_binding(self) :
        print("Controller.actions_binding()")
        #self.frame.bind("<Configure>",self.view.resize)
        self.scaleA.bind("<B1-Motion>",self.action_magnitude)
        self.scaleB.bind("<B1-Motion>",self.action_frequence)
        self.scaleC.bind("<B1-Motion>",self.action_phase)
        self.scaleD.bind("<B1-Motion>",self.action_harmonique)
        self.scaleE.bind("<B1-Motion>",self.action_samples)

    def action_magnitude(self,event):
        print("Controller.action_magnitude()")
        if  self.model.m != self.var_mag.get() :
            self.model.m = self.var_mag.get()
            self.model.generate()

    def action_frequence(self,event):
        print("Controller.action_frequence()")
        if  self.model.f != self.var_freq.get() :
            self.model.f = self.var_freq.get()
            self.model.generate()
    
    def action_phase(self,event):
        print("Controller.action_phase()")
        if  self.model.p != self.var_phase.get() :
            self.model.p = self.var_phase.get()
            self.model.generate()

    def action_harmonique(self,event):
        print("Controller.action_harmonique()")
        if  self.model.harmonics != self.var_harmo.get() :
            self.model.harmonics = self.var_harmo.get()
            self.model.generate()

    def action_samples(self,event):
        print("Controller.action_samples()")
        if  self.model.samples != self.var_samples.get() :
            self.model.samples = self.var_samples.get()
            self.model.generate()

    def activate_button(self):
        print("You selected the option " + str(self.radio_var.get()))
        self.model.harmo_odd_even=self.radio_var.get()

    def update_echantillon(self,event):
        print("cb_update_echantillon(self,event)",self.nb_ech_var.get())
        self.model.set_samples(int(self.nb_ech_var.get()))
        self.model.generate()

    def layout(self) :
        print("Controller.layout()")
        self.frame1.pack(side = "left", padx = 6)
        self.frame2.pack(side = "left", padx = 6)
        self.frame3.pack(side = "left", padx = 6)
        self.scaleA.pack()
        self.scaleB.pack()
        self.scaleC.pack()
        self.scaleD.pack()
        #self.scaleE.pack()

if __name__ == "__main__":
    root=tk.Tk()
    model=Generator()
    view=Screen(root)
    model.attach(view)
    view.create_grid(8)
    view.layout()
    ctrl=Controller(model,view)
    model.generate()
    ctrl.layout()

    root.mainloop()

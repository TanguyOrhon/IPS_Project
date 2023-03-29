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
from observer import Subject

class Generator(Subject) :
    def __init__(self, name="X"):
        Subject.__init__(self)
        self.name=name
        self.signal=[]
        self.m,self.f,self.p=2.0,3.0,0.0
        self.harmonics=1
        self.harmo_odd_even=1
        self.samples=200

    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
    def get_magnitude(self):
        return self.mag
    def set_magnitude(self,mag):
        self.mag=mag
    def get_frequency(self):
        return self.freq
    def set_frequency(self,freq):
        self.freq=freq
    def get_phase(self):
        return self.phase
    def set_phase(self,phase):
        self.phase=phase
    def get_harmonics(self) :
        return self.harmonics    
    def set_harmonics(self,harmonics=1) :
        self.harmonics=harmonics
    def get_samples(self):
        return self.samples
    def set_samples(self,samples):
        self.samples=samples
    def get_signal(self):
        return self.signal

    def vibration(self,t):
        m,f,p=self.m,self.f,self.p
        harmo=self.harmonics
        somme=0
        for h in range(1,harmo+1) :
            somme=somme + (m/h)*sin(2*pi*(f*h)*t-p)
        return somme

    def generate(self,period=1):
        print("Generator.generate()")
        del self.signal[0:]
        samples=int(self.samples)
        p_samples = period/samples
        for t in range(int(self.samples)+1) :
            self.signal.append([t*p_samples,self.vibration(t*p_samples)])
        self.notify()
        return self.signal

if   __name__ == "__main__" :
    model=Generator()
    print(model.generate())


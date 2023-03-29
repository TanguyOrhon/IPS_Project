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

from screen import Screen
from generator import Generator
from controller import Controller
from menubar import Menubar

if __name__ == "__main__":
    root=tk.Tk()
    root.title("Simulateur d'oscilloscope")
    model1=Generator()
    view1 = Screen(root)
    app = Menubar(root)
    model1.attach(view1)
    view1.create_grid(8)
    view1.layout()
    ctrl1 = Controller(model1,view1)
    model1.generate()
    ctrl1.layout()

    root.mainloop()
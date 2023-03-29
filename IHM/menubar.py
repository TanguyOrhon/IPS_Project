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

import json
from tkinter.filedialog import askopenfilename, asksaveasfilename

class Menubar(tk.Frame):
    def __init__(self,parent=None):
        tk.Frame.__init__(self, borderwidth=2)
        if parent :
            self.parent=parent
            menu = tk.Menu(parent)
            parent.config(menu=menu)
            fileMenu = tk.Menu(menu)
            fileMenu.add_command(label="Open",command=self.open)
            fileMenu.add_command(label="Save", command=self.save)
            fileMenu.add_command(label="Save Image (PIL)", command=self.save_image)
            fileMenu.add_command(label="Exit", command=self.close_app)
            menu.add_cascade(label="File", menu=fileMenu)
 
            fileMenu = tk.Menu(menu)
            fileMenu.add_command(label="About Us ...",command=self.about_us)
            fileMenu.add_command(label="About Tk ...",command=self.about_Tk)
            fileMenu.add_command(label="About Python ...",command=self.about_Python)
            menu.add_cascade(label="Help", menu=fileMenu)

    def open(self):
        name = askopenfilename(title="Choose the file to open",
                               filetypes=[("All files", ".*")])
        with open(name,"r") as fichier:
            dictionary = json.loads(fichier.read())
        print(dictionary)

    def save(self):
        name=asksaveasfilename(title="Save your file",defaultextension=".json")
        d = {'amplitude': '1', 'frequence' : '4'}
        with open(name, "w") as fichier:
            fichier.write(json.dumps(d))

    def save_image(self):
        pass

    def close_app(self):
        result = tk.messagebox.askquestion("Exit", "Voulez-vous quitter la fenêtre ?")
        if result == 'yes':
            exit()

    def about_us(self):
        print("menubar.about_us()")
        tk.messagebox.showinfo("About us", "Menez Romain / r9menez@enib.fr")
    
    def about_Tk(self):
        print("menubar.about_Tk()")
        tk.messagebox.showinfo("About Tk", "Bibliothèque graphique utilisée : TkInter")

    def about_Python(self):
        print("menubar.about_Python()")
        tk.messagebox.showinfo("About Python", "Langage de programmation utilisé : Python3")

if __name__ == "__main__" :
    mw = tk.Tk()
    app = Menubar(mw)
    mw.wm_title("Tkinter : Menubar")
    mw.mainloop()
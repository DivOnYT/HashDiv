from HashDiv import *
from tkinter import *

def init_Fr2Gr():
	top = Toplevel()
	top.title("Encode_Grec")
	entree1 = Entry(top, width=25)
	entree1.bind("<Return>", fr2Gr)
	entree1.grid(row=0, column=1)
	entre2 = Entry(top, width=25)
	entre2.grid(row=1, column=1)
	Label(top, text="Encode chars Fr2Gr").grid(row=0, column=0, sticky=E)
	
def init_Gr2Fr():
	top = Toplevel()
	top.title("Decode_Grec2Fr")
	entree = Entry(top, width=25)
	entree.bind("<Return>", gr2Fr)
	entree.grid(row=0, column=1)
	entre = Entry(top, width=25)
	entre.grid(row=1, column=1)
	Label(top, text="Decode chars Grec2Fr").grid(row=0, column=0, sticky=E)
	
def gr2Fr():
	pass
def fr2Gr():
        pass
t = Tk()
t.title("All Commands Encode")
Button(t, text="Encode_Grec", command=init_Fr2Gr).grid(row=0, column=0)
Button(t, text="Decode_Grec2Fr", command=init_Gr2Fr).grid(row=0, column=1)

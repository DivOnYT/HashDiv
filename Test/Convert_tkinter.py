from HashDiv import *
from tkinter import *
def convert(event):
  a = entree.get()
  b = convFr2Gr(a)
  entree1.delete(0, END)
  entree1.insert(0, b)
  print(a)
  print(b)
  
def conve(event):
  a = entree2.get()
  b = convGr2Fr(a)
  entree3.delete(0, END)
  entree3.insert(0, b)
  print(a)
  print(b)
  
t = Tk()
t.title("Conv Chars FR to chars GREC")
entree = Entry(t, width=25)
entree.bind("<Return>", convert)
entree.grid(row=0, column=1)
entree1 = Entry(t, width=25)
entree1.grid(row=1, column=1)
Label(t ,text="To convert : ").grid(row=0, column=0, sticky=E)
Label(t, text="To reconvert : ").grid(row=2, column=0, sticky=E)
Label(t, text="Le code est top secret.Alors CHUT...").grid(row=4, column=0, sticky=E)
entree2 = Entry(t, width=25)
entree2.bind("<Return>", conve)
entree2.grid(row=2, column=1)
entree3 = Entry(t, width=25)
entree3.grid(row=3, column=1)
t.mainloop()

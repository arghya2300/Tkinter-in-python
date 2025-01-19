from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert! Virus detected!!!")

button = Button(root, text="Scan For Virus", command=msg)
button.place(x=40,y=80)


root.mainloop()



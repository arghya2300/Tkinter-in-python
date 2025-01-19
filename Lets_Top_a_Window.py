from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("180x180")
    l2 = Label(top, text = "this is a another window")
    l2.pack()
    top.mainloop()

l = Label(root, text= "this is another window")
btn = Button(root, text= "click here to open another window", command=topwin)

l.pack()
btn.pack()

root.mainloop()






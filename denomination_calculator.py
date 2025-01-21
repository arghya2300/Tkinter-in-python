from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


root = Tk()
root.title("Denomination Calculator")
root.configure('light blue')
root.geometry("650x400")

upload = Image.open("image.png")
upload = upload.resize(('300x300'))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)


label1 = label(root, text="Hello user, welcome to the Denomination Calculator!",bg='light blue')
label1.place(relx=0.5, y=340, ANCHOR=CENTER)


def msg():
    MsgBox = messagebox.showinfo("Alert!", "Do you want to calculate the denomation count?")        
    if MsgBox == 'ok':
        topwin()

button1 = Button(root,text="lets get started!", command=msg, bg='brown',fg='white')
button1.place(x=260,y=360)


def topwin():
    top = Toplevel()    
    top.title('Denomination Calculator')
    top.configure(bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here the number notes for each denomination", bg='light grey')
    
    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="2000", bg='light grey')
    l3 = Label(top, text="2000", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

def calculator():
    try:
        global amount
        amount = int(entry.get())
        note2000 = amount // 2000
        amount %= 2000
        note500 = amount // 500
        amount %= 500
        note100 = amount // 100
        
        t1.delete(t1.END)
        t2.delete(t2.END)
        t3.delete(t3.END)

        t1.insert(END,str(note2000))
        t2.insert(END,str(note500))
        t3.insert(END,str(note100))

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

        btn = Button(top,text="calculate", command=calculator,bg='brown',fg='white')


    label.place(x=230, y=50 )
    entry.place(x=200, y=80 )

    btn.place(x=240, y=120 )

    lbl.place(x=140, y=170 )

    l1.place(x=180, y=200 )

    l2.place(x=180, y=230 )

    l3.place(x=180, y=260 )

    t1.place(x=270, y=200 )

    t2.place(x=270, y=230 )

    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()
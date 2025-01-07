from tkinter import *

window = Tk()
window.title('Tinker sample window')
window.geometry('300x300')

# label

greeting = Label(text="hello user", fg= 'white', bg= 'black')

button = Button(text= "click me", bg= 'white', fg= 'black')

entry = Entry(fg= "yellow", bg= "white", width= 50) 

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text='Super Frame')
label.pack()

textbox = Text(fg='green', bg='yellow')
textbox.pack()
window.mainloop()
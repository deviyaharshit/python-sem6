from tkinter import *
win = Tk(className="students")
win.title("welcome to advance python")
btn = Button(win,text="Click me")
btn.pack()
t = win.title()
lbl = Label(win,text=t)
lbl.pack()
win.mainloop()
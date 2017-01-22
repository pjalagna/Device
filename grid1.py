from Tkinter import *

# callback
def act1():
    global e1
    print("e1=" + e1.get())
#end act1

# paint
master = Tk()
master.geometry('200x210+350+70')

Label(master, text="First").grid(row=0, sticky=W)
Label(master, text="Second").grid(row=1, sticky=W)

global e1
e1 = Entry(master)
e2 = Entry(master)

e3 = Button(master, text="b" , command=act1)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=4, column=3)

master.mainloop()

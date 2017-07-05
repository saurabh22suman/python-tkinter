from tkinter import *
def mcal():
    var2 = var1.get()
    var3 = var2 * 1.8 + 32
    e2.insert(0,var3)
def mclear():
    e1.delete(0,END)
    e2.delete(0,END)
a = Tk()
var1 = IntVar()
n = "arial",14,"bold"
Label(a,text="Celsius",padx=25,font=(n)).grid(row=0,column=0,sticky="w")
e1 = Entry(a,width=25, textvariable=var1)
e1.grid(row=0,column=1)
Label(a,text="Fahrenheit",padx=25,font=(n)).grid(row=1,column=0,sticky="w")
e2 = Entry(a,width=25)
e2.grid(row=1,column=1)
Button(a,text="Convert",font=(n),command=mcal,width=25).grid(row=2,column=1)
Button(a,text="Clear",font=(n),command=mclear,width=25).grid(row=2,column=0)
Button(a,text="Close app",font=(n),command=a.destroy,width=25).grid(row=3,column=0)

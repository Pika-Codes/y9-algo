from tkinter import *
import turtle as t
import time
from tkinter import messagebox
import random as random

def password(event):
    """def turt():
        t.speed(0)
        t.left(90)
        t.forward(90)
        t.right(157)
        t.forward(93)
        t.left(157)
        t.forward(90)
        t.right(90)
        t.penup()
        t.forward(25)
        t.right(90)
        t.forward(45)
        t.pendown()
        t.circle(45)
        time.sleep(1)
        quit()"""
    p = pss.get()
    i = icecream.get()
    if p == 'n':
        print(i)
        clos = messagebox.askyesno("NICE!","Correct! Do you Want to Quit?")
        if clos == True:
            quit()
    else:
        jesus = messagebox.askyesno("R U DUMB!?","NOPE! Is The Password Correct?")
        if jesus == True:
            messagebox.showinfo("LOL","NO")
            time.sleep(1)
            quit()
        else:
            messagebox.showinfo("LOL","YES")
            time.sleep(1)
            quit()
        
ica = Tk()

icecream = StringVar()
choc = Radiobutton(ica, text='Chocolate', variable=icecream, value='chocolate')
vani = Radiobutton(ica, text='Vanilla', variable=icecream, value='vanilla')
straw = Radiobutton(ica, text='Srawberry', variable=icecream, value='strawberry')
#txt = Label(ica, text='')
txt2 = Label(ica ,text='Pick your favorite IceCream')
txt3 = Label(ica ,text='Flavour')
psstxt = Label(ica ,text='Password')
pss = Entry(ica,  show='•')
sub = Label(ica ,text='Press Enter')
jesu = Label(ica ,text='LOL')

#txt.grid(row=0,column=0)
txt2.grid(row=0,column=1)
txt3.grid(row=0,column=2)
choc.grid(row=1,column=0)
vani.grid(row=1,column=1)
straw.grid(row=1,column=2)
psstxt.grid(row=2,column=0)
pss.grid(row=2,column=1)
sub.grid(row=2,column=2)
jesu.grid(row=3,column=1)

ica.bind('<Return>', password)

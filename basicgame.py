from tkinter import*
from random import randint

def redraw():
    c1.delete("all")
    c1.create_oval(herox, heroy, herox + herosize, heroy + sizehero)
    
def moveright(event):
    global herox
    herox = herox + heromove
    c1.after(1, redraw)

win = Tk()
cwidth = 800
cheight = 600
herosize = 30
heromove = 10

herox = randint(0, cwidth)
heroy = randint(cheight, 0)

c1 = Canvas(win, width=cwidth, height=cheight)
c1.pack()
win.bind("<Right>", moveright)
c1.after(1, redraw)

mainloop()

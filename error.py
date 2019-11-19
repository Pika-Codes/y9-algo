from tkinter import *

win = Tk()

def runcode(event):
    if (e1.get() == ""):
        print("Enter A Number")
    else:
        try:
            print(e1.get()+10)
        except TypeError:
            print("You Have Not Entered A Number")
        except:
            print("Something Bad Happened")

e1 = Entry(win,)
e1.pack()
e1.bind("<Enter>", runcode)

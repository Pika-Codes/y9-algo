from tkinter import *

def findit():
    print(whos.get())

poke = open("poke.csv", "r")

pika = Tk()
pika.title("Pokemon Finder")

whos = Entry(pika, )
that = Button(pika, text="Find That Pokemon!", command=findit)
pokemon = Label(pika, text="")
whos.grid(row=0, column=0)
that.grid(row=0, column=1)
pokemon.grid(row=1, column=0)


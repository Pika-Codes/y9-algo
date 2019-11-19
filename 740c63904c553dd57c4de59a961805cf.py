import tkinter as tk

def show_entry_fields():
    print(e1.get())
    print(e2.get())

master = tk.Tk()

master.minsize(100 ,100)

tk.Label(master, text="First Name").grid(row=0)
tk.Label(master, text="Last Name").grid(row=1)
tk.Label(master, text="Comments").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

tk.Button(master, text='Quit', command=quit).grid(row=4, column=0)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=4, column=1)

tk.mainloop()

# -*- coding: utf-8 -*-

from tkinter import *


class App:
    def __init__(self,master):
        frame = Frame(master)
        master.geometry("500x75")
        master.title("Jump Ranking Sender")
        frame.pack()

        self.user_l = Label(master, text="User:")
        self.user_l.pack(side=LEFT, padx=5, pady=20)
        self.user_i = Entry(master)
        self.user_i.pack(side=LEFT, padx=5, pady=20)

        self.spacer = Label(master, text="")
        self.spacer.pack(side=LEFT, padx=10, pady=20)

        self.height_l = Label(master, text="Height:")
        self.height_l.pack(side=LEFT, padx=5, pady=20)
        self.height_i = Entry(master)
        self.height_i.pack(side=LEFT, padx=5, pady=20)

        self.quit_b = Button(master, text="SEND", command=sys.exit)
        self.quit_b.pack(side=RIGHT, padx=20, pady=20)


root = Tk()

app = App(root)

root.mainloop()
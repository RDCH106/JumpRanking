# -*- coding: utf-8 -*-

from tkinter import *


class App:
    def __init__(self,master):
        frame = Frame(master)
        master.geometry("500x75")
        master.title("Jump Ranking Sender")
        frame.pack()

        self.quit_b = Button(master, text="Quit", command=sys.exit)
        self.quit_b.pack()


root = Tk()

app = App(root)

root.mainloop()
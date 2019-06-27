# -*- coding: utf-8 -*-

from tkinter import *

response_ok = "✔️"
response_error = "❌"
response_sending = "⏳"


class App:
    def __init__(self, master):
        frame = Frame(master)
        master.geometry("500x75")
        master.title("Jump Ranking Sender")
        frame.pack()

        self.user_l = Label(master, text="User:")
        self.user_l.pack(side=LEFT, padx=5, pady=20)
        self.user_i = Entry(master)
        self.user_i.pack(side=LEFT, padx=5, pady=20)

        self.spacer = Label(master, text="")
        self.spacer.pack(side=LEFT, padx=5, pady=20)

        self.height_l = Label(master, text="Height:")
        self.height_l.pack(side=LEFT, padx=5, pady=20)
        self.height_i = Entry(master)
        self.height_i.pack(side=LEFT, padx=5, pady=20)

        self.spacer = Label(master, text="")
        self.spacer.pack(side=RIGHT, padx=5, pady=20)

        self.quit_b = Button(master, text="SEND", command=self.send_request)
        self.quit_b.pack(side=RIGHT, padx=5, pady=20)

        self.response_l = Label(master, text=" ")
        self.response_l.pack(side=RIGHT, padx=5, pady=20)



root = Tk()

app = App(root)

root.mainloop()

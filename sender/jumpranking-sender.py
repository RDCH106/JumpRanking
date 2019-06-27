# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from requests import post, exceptions
import time

response_ok = "✔️"
response_error = "❌"
response_sending = "⏳"

api = "https://server1.mascandobits.es:5030/jumpranking/api/v1/registers"


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

    def send_request(self):
        self.response_l["text"] = response_sending
        self.response_l.update()
        if self.user_i.get() != "" and self.height_i.get() != "" and self.height_i.get().isdigit():
            try:
                response = post(api + "/" + self.user_i.get() + "/" + self.height_i.get(), auth=("", ""))
                if response.status_code == 201:
                    self.response_l["text"] = response_ok
                    self.user_i.delete(0, END)
                    self.height_i.delete(0, END)
                else:
                    self.response_l["text"] = response_error
            except exceptions.RequestException as e:
                print(e)
                messagebox.showerror("Error", e)
                self.response_l["text"] = response_error
        else:
            messagebox.showerror("Error", "Invalid input data!!")
            self.response_l["text"] = response_error


root = Tk()

app = App(root)

root.mainloop()

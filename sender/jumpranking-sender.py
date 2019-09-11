# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from requests import post, exceptions
from json import load, JSONDecodeError
from hashlib import sha256

response_ok = "✔️"
response_error = "❌"
response_sending = "⏳"

api = ""


class App:
    def __init__(self, master):
        self.credentials = None
        self.load_json()
        api = self.credentials["api"]
        self.hash = None

        frame = Frame(master)
        master.geometry("500x100")
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

        self.password_l = Label(master, text="Password:")
        self.password_l.place(x=290, y=75)
        self.password_i = Entry(master, show="*")
        self.password_i.place(x=360, y=75)

    def load_json(self):
        with open("config/config.json", 'r') as f:
            try:
                self.credentials = load(f)
            except JSONDecodeError as e:
                messagebox.showerror("Error", "config.json decode error!!")

    def send_request(self):
        self.response_l["text"] = response_sending
        self.response_l.update()
        self.hash = sha256()
        self.hash.update(self.password_i.get().encode("utf8"))
        if self.hash.hexdigest() == self.credentials["password"]:
            if self.user_i.get() != "" and self.height_i.get() != "" and self.height_i.get().isdigit():
                try:
                    response = post(api + "/" + self.user_i.get() + "/" + self.height_i.get(),
                                    auth=(self.credentials["user"], self.password_i.get()))
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
        else:
            messagebox.showerror("Error", "Invalid password!!")
            self.response_l["text"] = response_error


root = Tk()

app = App(root)

root.mainloop()

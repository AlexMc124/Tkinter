import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "BOOTY BOOTY BOOTY\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.booty_btn = tk.Button(self)
        self.booty_btn["text"] = "More Booty??"
        self.booty_btn["command"] = self.more_booty
        self.booty_btn.pack()

        self.kanye = tk.Button(self)
        self.kanye["text"] = "kanye?"
        self.kanye["command"] = self.call_kanye
        self.kanye.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone have some booty!")
        print('(‿ˠ‿) (‿ˠ‿) (‿ˠ‿) (‿ˠ‿) (‿ˠ‿)')

    def more_booty(self):
        print("More Booty!!")

    def call_kanye(self):
        print("Kanye")


def launch():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


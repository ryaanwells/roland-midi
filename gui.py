from Tkinter import *
from patches.integrated_tones import IntegratedTones

class App:

    def __init__(self, master):

        self.current = None
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.listbox = Listbox(frame, exportselection=0)
        self.listbox.pack(side=LEFT)

        it = IntegratedTones()
        for key, value in it.groups.items():
            self.listbox.insert(END, key)

    def say_hi(self):
        print "hi there, everyone!"

    def poll_main_selection(self):
        now = self.listbox.curselection()
        if now != self.current:
            print


root = Tk()

app = App(root)

root.mainloop()

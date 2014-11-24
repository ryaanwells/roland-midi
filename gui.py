from Tkinter import *
from patches.integrated_tones import IntegratedTones


class App:

    def __init__(self, master):

        self.current = None
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.main_bank_select = Listbox(frame, exportselection=0)
        self.main_bank_select.pack(side=LEFT)

        self.voice_select = Listbox(frame, exportselection=0)
        self.voice_select.pack(side=LEFT)

        self.integrated_tones = IntegratedTones()
        self.chosen_bank = None
        self._update_listbox(self.main_bank_select, self.integrated_tones.groups)

        self.main_bank_select.bind("<<ListboxSelect>>", self._update_voice_listbox)
        self.voice_select.bind("<<ListboxSelect>>", self._choose_voice)

    def poll_main_selection(self):
        now = self.main_bank_select.curselection()
        if now != self.current:
            print now

    def _update_voice_listbox(self, event):
        selection = self._get_listbox_selection_from_event(event)
        print selection
        self.chosen_bank = self.integrated_tones.groups[selection]["class"]
        self._update_listbox(self.voice_select, self.chosen_bank.voices)

    def _choose_voice(self, event):
        selection = self._get_listbox_selection_from_event(event)
        print self.chosen_bank.voices[selection]

    @staticmethod
    def _get_listbox_selection_from_event(event):
        return event.widget.curselection()[0]

    @staticmethod
    def _update_listbox(listbox, item_array):
        listbox.delete(0, END)
        for item in item_array:
            listbox.insert(END, item["name"])


root = Tk()

app = App(root)

root.mainloop()

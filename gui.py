from Tkinter import *
from patches.integrated_tones import IntegratedTones
from voice_stack.patch_change import PatchChange
from voice_stack.patch_entry import PatchEntry


class App:

    def __init__(self, master):

        self.current = None
        frame = Frame(master)
        frame.pack()

        # Voice stack info
        self.chosen_bank = None
        self.chosen_voice = None
        self.voice_list = []
        self.current_index = -1

        # Voice Display Info
        self.display_holder = LabelFrame(frame, padx=5, pady=5)
        self.display_holder.pack(side=RIGHT)
        self.display_class_stringvar = StringVar()
        self.display_voice_stringvar = StringVar()
        self.display_class_label = Label(self.display_holder, textvariable=self.display_class_stringvar)
        self.display_voice_label = Label(self.display_holder, textvariable=self.display_voice_stringvar)
        self.display_class_label.pack(side=LEFT)
        self.display_voice_label.pack(side=LEFT)

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.main_bank_select = Listbox(frame, exportselection=0)
        self.main_bank_select.pack(side=LEFT)

        self.voice_select = Listbox(frame, exportselection=0)
        self.voice_select.pack(side=LEFT)

        self.integrated_tones = IntegratedTones()
        self._update_listbox(self.main_bank_select, self.integrated_tones.groups)

        self.main_bank_select.bind("<<ListboxSelect>>", self._update_voice_listbox)
        self.voice_select.bind("<<ListboxSelect>>", self._choose_voice)

        self.chose_button = Button(frame, text="Add", bg="black", fg="blue", command=self._pick_voice)
        self.chose_button.pack(side=LEFT)

    def hello(self, event):
        if len(self.voice_list) == 0:
            return

        if self.current_index == len(self.voice_list) - 1:
            self.current_index = 0
        else:
            self.current_index += 1
        new_display = self.voice_list[self.current_index]
        self.display_class_stringvar.set(new_display.upper_1.patch_class.__name__)
        self.display_voice_stringvar.set(new_display.upper_1.patch_entry["name"])
        print self.integrated_tones.get_change_info_for_patch_entry(new_display)
        print event.type
        print "hello"

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
        self.chosen_voice = self.chosen_bank.voices[selection]

    def _pick_voice(self):
        print self.chosen_voice["voice_number"]
        patch_entry = PatchEntry(self.chosen_bank, self.chosen_voice)
        patch_change = PatchChange(patch_entry)

        self.voice_list.append(patch_change)

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
root.bind("<space>", app.hello)

root.mainloop()

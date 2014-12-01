from Tkinter import *
from patches.integrated_tones import IntegratedTones
from voice_stack.patch_change import PatchChange
from voice_stack.patch_entry import PatchEntry
from tools.load_save import LoadSave


class App:

    def __init__(self, master):
        self.current = None
        frame = Frame(master)
        frame.pack()

        # Voice stack info
        self.chosen_bank = None
        self.chosen_voice = None
        self.voice_list = LoadSave.load()
        self.current_index = -1

        # Voice Display Info
        self.display_holder = LabelFrame(frame, padx=5, pady=5)
        self.display_holder.pack(side=RIGHT)
        self.display_voice_stringvar = StringVar()
        self.display_voice_label = Label(self.display_holder, textvariable=self.display_voice_stringvar)
        self.display_voice_label.pack(side=LEFT)

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.main_bank_select = Listbox(frame, exportselection=0, width=8)
        self.main_bank_select.pack(side=LEFT)

        self.voice_select = Listbox(frame, exportselection=0, width=12, height=10)
        self.voice_select.pack(side=LEFT)

        button_frame = Frame(frame)
        button_frame.pack(side=LEFT)

        chose_append_button = Button(button_frame, text="At End", bg="black", fg="blue",
                                     command=lambda: self._pick_voice(append=True))
        chose_append_button.pack(side=TOP)
        chose_before_button = Button(button_frame, text="Before",
                                     command=lambda: self._pick_voice(after=False))
        chose_before_button.pack(side=TOP)
        chose_before_button = Button(button_frame, text="After",
                                     command=lambda: self._pick_voice(after=True))
        chose_before_button.pack(side=TOP)
        spacer = Frame(button_frame, height=2)
        spacer.pack(side=TOP, pady=5)

        self.order_listbox = Listbox(frame, exportselection=0)
        self.order_listbox.pack(side=LEFT)
        set_cursor_button = Button(button_frame, text="Set At",
                                   command=lambda: self._set_current_index(int(self.order_listbox.curselection()[0])))
        set_cursor_button.pack()

        self.integrated_tones = IntegratedTones()
        self._update_listbox(self.main_bank_select, self.integrated_tones.groups)

        self.main_bank_select.bind("<<ListboxSelect>>", self._update_voice_listbox)
        self.voice_select.bind("<<ListboxSelect>>", self._choose_voice)
        self._update_order_listbox()

    def next_voice(self, event):
        if len(self.voice_list) == 0:
            return

        self.order_listbox.selection_clear(0, END)
        if self.current_index == len(self.voice_list) - 1:
            self.current_index = 0
        else:
            self.current_index += 1
        new_display = self.voice_list[self.current_index]
        self.display_voice_stringvar.set(str(new_display))

        self.order_listbox.selection_set(self.current_index)
        self.order_listbox.see(self.current_index + 3)
        print self.integrated_tones.get_change_info_for_patch_entry(new_display)

    def _update_voice_listbox(self, event):
        selection = self._get_listbox_selection_from_event(event)
        self.chosen_bank = self.integrated_tones.groups[selection]["class"]
        self._update_listbox(self.voice_select, self.chosen_bank.voices)

    def _choose_voice(self, event):
        selection = self._get_listbox_selection_from_event(event)
        self.chosen_voice = self.chosen_bank.voices[selection]

    def _pick_voice(self, append=False, after=False):
        if self.chosen_voice:
            patch_entry = PatchEntry(self.chosen_bank, self.chosen_voice)
            patch_change = PatchChange(patch_entry)
            current_index_selection = map(int, self.order_listbox.curselection())

            if append or len(current_index_selection) == 0:
                self.voice_list.append(patch_change)
            else:
                index = current_index_selection[0]
                if after:
                    index += 1
                self.voice_list.insert(index, patch_change)

            self._update_order_listbox()

            print patch_change.serialise()
            LoadSave.write(self.voice_list)

    def _update_order_listbox(self):
        self.order_listbox.delete(0, END)
        for item in self.voice_list:
            self.order_listbox.insert(END, str(item))

    def _set_current_index(self, index):
        self.current_index = index

    @staticmethod
    def _get_listbox_selection_from_event(event):
        return int(event.widget.curselection()[0])

    @staticmethod
    def _update_listbox(listbox, item_array):
        listbox.delete(0, END)
        for item in item_array:
            listbox.insert(END, item["name"])


root = Tk()

app = App(root)
root.bind("<space>", app.next_voice)

root.mainloop()

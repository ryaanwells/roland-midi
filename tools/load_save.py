import json
from voice_stack.patch_entry import PatchEntry
from voice_stack.patch_change import PatchChange
from patches.integrated_tones import IntegratedTones


class LoadSave:

    @staticmethod
    def load():
        all_changes = []
        try:
            saved_file = open("saved.json", "r")
            loaded = json.load(saved_file)
            saved_file.close()
        except Exception as e:
            print e
            return all_changes

        print loaded

        for change in loaded:
            upper_1 = PatchEntry(patch_class=IntegratedTones.get_class_by_name(change["upper_1"]["patch_class"]),
                                 patch_entry=change["upper_1"]["patch_entry"])
            print upper_1.patch_entry
            print upper_1.patch_class
            patch_change = PatchChange(upper_1)
            all_changes.append(patch_change)

        return all_changes

    @staticmethod
    def write(patch_changes):
        try:
            save_file = open("saved.json", "w")
        except Exception as e:
            print e
            return

        change_list = []
        for patch in patch_changes:
            change_list.append(patch.serialise())

        json.dump(change_list, save_file, sort_keys=True, indent=4,)

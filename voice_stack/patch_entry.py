

class PatchEntry:

    def __init__(self, patch_class=None, patch_entry=None):
        self.patch_class = patch_class
        self.patch_entry = patch_entry

    def serialise(self):
        return {"patch_class": self.patch_class.__name__, "patch_entry": self.patch_entry}

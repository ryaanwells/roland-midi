

class PatchChange:

    def __init__(self, name, upper_1, upper_2=False, lower=False):
        self.name = name
        self.upper_1 = upper_1
        self.upper_2 = upper_2
        self.lower = lower

    def __str__(self):
        base = "["
        if self.name:
            base = base + self.name
        base += ", "
        if self.upper_1:
            base = base + self.upper_1.patch_class.__name__.upper() + ":" + self.upper_1.patch_entry["name"]
        base += ", "

        if self.upper_2:
            base = base + self.upper_2.patch_class.__name__.upper() + ":" + self.upper_2.patch_entry["name"]
        base += ", "

        if self.lower:
            base = base + self.upper_3.patch_class.__name__.upper() + ":" + self.upper_3.patch_entry["name"]
        base += "]"

        return base

    def serialise(self):
        return {"name": self.name if self.name else None,
                "upper_1": self.upper_1.serialise() if self.upper_1 else None,
                "upper_2": self.upper_2.serialise() if self.upper_2 else None,
                "lower": self.lower.serialise() if self.lower else None}

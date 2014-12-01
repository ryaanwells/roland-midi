from tools.iter_mixin import IterMixin

from patches.integrated_tones_patches.piano import Piano
from patches.integrated_tones_patches.ep import EP
from patches.integrated_tones_patches.clav import Clav
from patches.integrated_tones_patches.organ import Organ
from patches.integrated_tones_patches.strings import Strings
from patches.integrated_tones_patches.pad import Pad
from patches.integrated_tones_patches.guitar import Guitar
from patches.integrated_tones_patches.brass import Brass
from patches.integrated_tones_patches.synth import Synth


class IntegratedTones(IterMixin):
    MSB_BANK_CHANGE_UPPER_1 = 0xB0
    MSB_BANK_CHANGE_UPPER_2 = 0xB1
    MSB_BANK_CHANGE_LOWER = 0xB2

    MSB_SET_VOICE_UPPER_1 = 0xC0
    MSB_SET_VOICE_UPPER_2 = 0xC1
    MSB_SET_VOICE_LOWER = 0xC2

    LSB_SET_BANK_SOURCE = 0x00
    LSB_SET_BANK_FAMILY = 0x20

    INTEGRATED_TONES_PROGRAM_CHANGE = 87

    groups = [
        {"name": "PIANO", "class": Piano},
        {"name": "EP", "class": EP},
        {"name": "CLAV", "class": Clav},
        {"name": "ORGAN", "class": Organ},
        {"name": "STRINGS", "class": Strings},
        {"name": "PAD", "class": Pad},
        {"name": "GUITAR", "class": Guitar},
        {"name": "BRASS", "class": Brass},
        {"name": "SYNTH", "class": Synth}
    ]

    @property
    def items(self):
        print self.__dict__
        return self.__dict__

    @staticmethod
    def get_class_by_name(name):
        name = name.upper()
        for group in IntegratedTones.groups:
            if group["name"] == name:
                return group["class"]
        return None

    def get_change_info_for_patch_entry(self, patch_entry):
        change_info = []
        if patch_entry.upper_1:
            signals = self._create_voice_change(patch_entry.upper_1, self.MSB_BANK_CHANGE_UPPER_1, self.MSB_SET_VOICE_UPPER_1)
            change_info.extend(signals)
        if patch_entry.upper_2:
            signals = self._create_voice_change(patch_entry.upper_2, self.MSB_BANK_CHANGE_UPPER_2, self.MSB_SET_VOICE_UPPER_2)
            change_info.extend(signals)
        if patch_entry.lower:
            signals = self._create_voice_change(patch_entry.lower, self.MSB_BANK_CHANGE_LOWER, self.MSB_SET_VOICE_LOWER)
            change_info.extend(signals)

        return change_info

    def _create_voice_change(self, patch_entry, msb_bank_change, msb_set_voice):
        indicate_bank_change = [msb_bank_change, self.LSB_SET_BANK_SOURCE, self.INTEGRATED_TONES_PROGRAM_CHANGE]
        indicate_desired_bank = [msb_bank_change, self.LSB_SET_BANK_FAMILY, patch_entry.patch_class.BANK_NUMBER]
        indicate_desired_patch = [msb_set_voice, patch_entry.patch_entry["voice_number"]]
        return [indicate_bank_change, indicate_desired_bank, indicate_desired_patch]


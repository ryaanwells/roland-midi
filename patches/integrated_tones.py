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
    LSB = 87
    
    groups = {"PIANO": Piano,
              "EP": EP,
              "CLAV": Clav,
              "ORGAN": Organ,
              "STRINGS": Strings,
              "PAD": Pad,
              "GUITAR": Guitar,
              "BRASS": Brass,
              "SYNTH": Synth}

    @property
    def items(self):
        print self.__dict__
        return self.__dict__


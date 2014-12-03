from tools.midi_controller import MidiController
from getch import getch


PIANO = [[0xB0, 0x00, 87], [0xB0, 0x20, 64], [0xC0, 0]]
EP = [[0xB0, 0x00, 87], [0xB0, 0x20, 65], [0xC0, 4]]
JAZZ_ORGAN = [[0xB0, 0x00, 87], [0xB0, 0x20, 67], [0xC0, 5]]
SURFS_UP_ORGAN = [[0xB0, 0x00, 87], [0xB0, 0x20, 67], [0xC0, 15]]
SOFT_PAD = [[0xB0, 0x00, 87], [0xB0, 0x20, 69], [0xC0, 1]]
COMBING_PAD = [[0xB0, 0x00, 87], [0xB0, 0x20, 69], [0xC0, 13]]
BARI_SAX = [[0xB0, 0x00, 87], [0xB0, 0x20, 71], [0xC0, 8]]
FLUTE = [[0xB0, 0x00, 87], [0xB0, 0x20, 71], [0xC0, 9]]
OBOE = [[0xB0, 0x00, 87], [0xB0, 0x20, 71], [0xC0, 10]]
TRUMPETS = [[0xB0, 0x00, 93], [0xB0, 0x20, 8], [0xC0, 244-128]]

voices = {
    " ": PIANO,
    "e": EP,
    "j": JAZZ_ORGAN,
    "u": SURFS_UP_ORGAN,
    "p": SOFT_PAD,
    "m": COMBING_PAD,
    "b": BARI_SAX,
    "f": FLUTE,
    "o": OBOE,
    "t": TRUMPETS
}

if __name__ == "__main__":
    mc = MidiController()
    run = True
    while run:
        ch = getch()
        print ch

        if ch == "/":
            print "exiting"
            run = False
        else:
            voice = voices.get(ch, PIANO)
            print voice
            mc.send_messages(voice)



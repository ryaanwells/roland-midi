from patches.integrated_tones import IntegratedTones

import rtmidi
import time



class SRXBTones:
    LSB = 93
    
    BANK_1 = 7
    BANK_2 = 8
    BANK_3 = 9
    BANK_4 = 10

class SRXATones:
    LSB = 93

    BANK_1 = 11
    BANK_2 = 12
    BANK_3 = 13
    BANK_4 = 14

class Part:

    LSB_SET_BANK_SOURCE = 0x00
    LSB_SET_BANK_FAMILY = 0x20

    class Upper1:
        MSB_BANK_CHANGE = 0xB0
        MSB_SET_VOICE = 0xC0
        MSB_NOTE_ON = 0x90
        MSB_NOTE_OFF = 0x80
        
    class Upper2:
        MSB_BANK_CHANGE = 0xB1
        MSB_SET_VOICE = 0xC1
        MSB_NOTE_ON = 0x91
        MSB_NOTE_OFF = 0x81

    class Lower:
        MSB_BANK_CHANGE = 0xB2
        MSB_SET_VOICE = 0xC2
        MSB_NOTE_ON = 0x92
        MSB_NOTE_OFF = 0x82

MIDDLE_C = 60

U1_indicate_bank_change = [Part.Upper1.MSB_BANK_CHANGE, Part.LSB_SET_BANK_SOURCE, IntegratedTones.LSB]
U1_set_bank_piano = [Part.Upper1.MSB_BANK_CHANGE, Part.LSB_SET_BANK_FAMILY, IntegratedTones.Piano.BANK_NUMBER]
U1_set_bank_ep = [Part.Upper1.MSB_BANK_CHANGE, Part.LSB_SET_BANK_FAMILY, IntegratedTones.EP.BANK_NUMBER]
U1_set_voice = [Part.Upper1.MSB_SET_VOICE, IntegratedTones.Piano.HonkyTonk]

U1_note_on = [Part.Upper1.MSB_NOTE_ON, MIDDLE_C, 112]
U1_note_off = [Part.Upper1.MSB_NOTE_OFF, MIDDLE_C, 0]


U2_indicate_bank_change = [Part.Upper2.MSB_BANK_CHANGE, Part.LSB_SET_BANK_SOURCE, SRXATones.LSB]
U2_set_bank_piano = [Part.Upper2.MSB_BANK_CHANGE, Part.LSB_SET_BANK_FAMILY, SRXATones.BANK_1]
U2_set_bank_ep = [Part.Upper2.MSB_BANK_CHANGE, Part.LSB_SET_BANK_FAMILY, SRXBTones.BANK_2]
U2_set_voice = [Part.Upper2.MSB_SET_VOICE, 00]

U2_note_on = [Part.Upper2.MSB_NOTE_ON, MIDDLE_C, 112]
U2_note_off = [Part.Upper2.MSB_NOTE_OFF, MIDDLE_C, 0]

out = rtmidi.MidiOut()
ports = out.get_ports()

out.open_port(1)

out.send_message(U1_indicate_bank_change)
out.send_message(U1_set_bank_piano)
out.send_message(U1_set_voice)
out.send_message(U2_indicate_bank_change)
out.send_message(U2_set_bank_ep)
out.send_message(U2_set_voice)

time.sleep(0.3)

out.send_message(U1_note_on)
out.send_message(U2_note_on)
time.sleep(1)
out.send_message(U1_note_off)
out.send_message(U2_note_off)

time.sleep(2)

out.send_message(U1_indicate_bank_change)
out.send_message(U1_set_bank_ep)
out.send_message(U1_set_voice)
out.send_message(U2_indicate_bank_change)
out.send_message(U2_set_bank_piano)
out.send_message(U2_set_voice)

time.sleep(0.3)

out.send_message(U1_note_on)
out.send_message(U2_note_on)
time.sleep(2)
out.send_message(U1_note_off)
out.send_message(U2_note_off)

del out


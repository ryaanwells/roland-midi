import rtmidi
import time

class IntegratedTones:
    LSB = 87
    
    class Piano:
        BANK_NUMBER = 64

    EP = 65
    CLAV = 66
    ORGAN = 67
    STRINGS = 68
    PAD = 69
    GUITAR = 70
    BRASS = 71
    SYNTH = 72

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


U1_indicate_bank_change = [0xB0, 0x00, IntegratedTones.LSB]
U1_set_bank_piano = [0xB0, 0x20, IntegratedTones.Piano.BANK_NUMBER]
U1_set_bank_ep = [0xB0, 0x20, IntegratedTones.EP]
U1_set_voice = [0xC0, 00]

U1_note_on = [0x90, 60, 112]
U1_note_off = [0x80, 60, 0]


U2_indicate_bank_change = [0xB1, 0x00, SRXATones.LSB]
U2_set_bank_piano = [0xB1, 0x20, SRXATones.BANK_1]
U2_set_bank_ep = [0xB1, 0x20, SRXBTones.BANK_2]
U2_set_voice = [0xC1, 00]

U2_note_on = [0x91, 60, 112]
U2_note_off = [0x81, 60, 0]

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


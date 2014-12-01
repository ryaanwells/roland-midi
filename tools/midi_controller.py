import rtmidi


class MidiController:

    def __init__(self):
        self.midi_out = rtmidi.MidiOut()
        self.midi_out.get_ports()
        # self.midi_out.open_port(1) # uncomment me

    def send_messages(self, messages):
        for message in messages:
            self.midi_out.send_message(message)

    def close(self):
        del self.midi_out
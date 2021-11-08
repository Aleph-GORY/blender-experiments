import rtmidi
import time
import sys


def linear_interpolation(r1, r2, s1, s2):
    return lambda x: (x - r1) / (r2 - r1) * (s1 - s2) + s1


class MidiInputHandler(object):
    def __init__(self, port, schema, debug=False):
        self.port = port
        self.schema = schema
        self.debug = debug
        self._wallclock = time.time()

    def __call__(self, event, data=None):
        message, deltatime = event
        self._wallclock += deltatime
        if self.debug:
            print("[%s] @%0.4f %r" % (self.port, self._wallclock, message))
        id = message[1]
        transformer = self.schema.get(id)
        if transformer:
            value = message[2]
            transformer(value)


def setup_controller(controller_schema, port=0):
    midi_controller = rtmidi.MidiIn()
    ports = midi_controller.get_ports()
    if ports:
        print("Ports")
        print(ports)
        print("Opening connection with", ports[port], "on port", port)
        midi_controller.open_port(port)
        midi_controller.set_callback(MidiInputHandler(port, controller_schema))
    else:
        print("NO MIDI INPUT PORTS!")
        sys.exit(-1)

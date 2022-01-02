import com
import xbee
from machine import Pin

class barrier:
    moving = 0
    position = 0
    ad0 = Pin("D0", Pin.IN, Pin.PULL_UP)
    ad1 = Pin("D1", Pin.IN, Pin.PULL_UP)
    ad2 = Pin("D2", Pin.IN, Pin.PULL_UP)
    ad4 = Pin("D4", Pin.OUT)

    def status(seq,payload):
        pass
    def command(seq, payload):
        pass

    def watch(self):
        pass
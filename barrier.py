import com
import xbee
from machine import Pin


class Barrier:
    moving = 0
    barrier_position = 0
    ad0 = Pin("D0", Pin.IN, Pin.PULL_UP) #door
    ad1 = Pin("D1", Pin.IN, Pin.PULL_UP) #motor
    ad4 = Pin("D4", Pin.OUT, value=0)
    door = ad0.value()
    motor = ad1.value()
    update = False

    def status(self, seq, payload):
        pass

    def command(self, seq, payload):
        pass

    def watch(self):
        current_door = self.door
        current_motor = self.motor
        self.door = self.ad0.value()
        self.motor = self.ad1.value()
        if (current_door != self.door) or (current_motor != self.motor):
            self.update = True
        else:
            self.update = False
        if self.door == 0:
            if self.motor == 1:
                self.moving = 0
                self.barrier_position = 100
        if self.motor == 0:
            if self.door == 1:
                self.moving = 0
                self.barrier_position = 0
        if self.motor == 0:
            if self.door == 0:
                if self.barrier_position == 100:
                    self.barrier_position = 50
                    self.moving = 1
                if self.barrier_position == 0:
                    self.barrier_position = 50
                    self.moving = 2
        return self.update

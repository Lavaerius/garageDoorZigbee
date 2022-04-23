import time

import com
import xbee
from machine import Pin


class Barrier:
    moving = b'\x00'
    barrier_position = b'\x00'
    ad0 = Pin("D0", Pin.IN, Pin.PULL_UP) #door
    ad1 = Pin("D1", Pin.IN, Pin.PULL_UP) #motor
    ad4 = Pin("D4", Pin.OUT, value=0)
    door = ad0.value().to_bytes(2,"big")
    motor = ad1.value().to_bytes(2, "big")
    update = True

    def status(self,seq, kwargs):
        #moving state is x0001 enum8(0x30)
        #Barrierposition is 0x000A uint8(0x20)
        # 2 octets attribute identifier
        # 1 octet attribute data type
        # 1 octet attribute value
        print("really messed up early in the game eh")
        attributes = kwargs['attributes']
        print(attributes)
        if len(attributes) == 1:
            print("length")
            if attributes[0] == 10:
                print("position request")
                print(self.barrier_position)
                return self.barrier_position
            if attributes[0] == 1:
                print("moving request")
                print(self.moving)
                return self.moving
        #to_return = bytes([1,0,48]) + bytes(self.moving) + bytes([10,0,20]) + bytes(self.barrier_position)
        return -1


    def command(self, seq, payload):
        self.ad4.value(1)
        time.sleep_ms(600)
        self.ad4.value(0)


    def watch(self):
        current_door = self.door
        current_motor = self.motor
        self.door = self.ad0.value().to_bytes(2, "big")
        self.motor = self.ad1.value().to_bytes(2, "big")
        #print("door: "+str(self.door))
        #print("motor:" +str(self.motor))
        if (current_door != self.door) or (current_motor != self.motor):
            self.update = True
        else:
            self.update = False
        if self.door == b'\x00':
            if self.motor == b'\x01':
                self.moving = b'\x00'
                self.barrier_position = b'\x64'
        if self.motor == b'\x00':
            if self.door == b'\x01':
                self.moving = b'\x00'
                self.barrier_position = b'\x00'
        if self.motor == b'\x00':
            if self.door == b'\x00':
                if self.barrier_position == b'\x64':
                    self.barrier_position = b'\x32'
                    self.moving = b'\x01'
                if self.barrier_position == b'\x00':
                    self.barrier_position = b'\x32'
                    self.moving = b'\x02'
        return self.update

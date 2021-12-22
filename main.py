# xbee python docs:  http://cms.digi.com/resources/documentation/digidocs/90002219/#concepts/c_90002219_start.htm?TocPath=Digi%2520MicroPython%2520Programming%2520Guide%257C_____0
# using pycharm w/ xbee: https://www.digi.com/resources/documentation/digidocs/90002445/default.htm
# xbee hardware pdf: https://www.digi.com/resources/documentation/digidocs/pdfs/90001543.pdf
import time
import xbee
import ubinascii
from machine import I2C
from machine import Pin
import struct
# print(" +-------------------------------------+")
# print(" +-------------------------------------+\n")

# print("Waiting for data...\n")
# default to everything off and 0 at power on.
#  in the future, we can try to reclaim previous state.
#  Hopefully this lamp won't turn off very often


# arduino_addr = 0x48
# senddata = 0

x = xbee.XBee()
#xbee.atcmd('NT', 0xFF)
#tp = xbee.atcmd('TP')1A
print(xbee.atcmd('MY'))
print("transmitting")
srcaddr = int(xbee.atcmd('MY'))
print(xbee.atcmd('AI'))
xbee.atcmd('CN')
print(srcaddr)
srcarry = srcaddr.to_bytes(2,"big")
print(srcarry)
initial_payload=bytes([171, srcarry[1], srcarry[0], 141, 194, 209, 65, 0, 162, 19, 0, 142])
leave_load=bytes([171, 141, 194, 209, 65, 0, 162, 19, 0, 2])
print(initial_payload)
#xbee.transmit(xbee.ADDR_COORDINATOR, b'\xAB\xF7\x6A\x8D\xC2\xD1\x41\x00\xA2\x13\x00\x8E', source_ep=0, dest_ep=0, cluster=19, profile=0, tx_options=0)
#xbee.transmit(xbee.ADDR_COORDINATOR, b'\xAB\xF7\x6A\x8D\xC2\xD1\x41\x00\xA2\x13\x00\x8E', source_ep=0, dest_ep=0, cluster=19, profile=0, tx_options=0)
send=0
lame = 0
while lame < 3:
    xbee.receive()
    lame += 1

while send==0:
    try:
        if xbee.transmit(xbee.ADDR_COORDINATOR, leave_load, source_ep=0, dest_ep=0, cluster=52, profile=0, tx_options=0) is None:
            send = 1
        print("leaving")
    except OSError as e:
        print("leaving transmit error")
    send=1
send=0
time.sleep(1)
while send==0:
    try:
        if xbee.transmit(xbee.ADDR_COORDINATOR, initial_payload, source_ep=0, dest_ep=0, cluster=19, profile=0, tx_options=0) is None:
            send = 1
        print("joining")
    except OSError as e:
        print("joining transmit error")
print("receiving")
while 1 != 0:
    blorp = xbee.receive()
    if blorp is not None:
        if blorp['cluster']==5:
            print(bytes(blorp['payload']))
            b = bytearray(blorp['payload'])
            print(b[0])
            payload=bytes([b[0], 00, b[1], b[2], 1, 8])
            xbee.transmit(xbee.ADDR_COORDINATOR,payload,source_ep=0,dest_ep=0,cluster=32773, profile=0, tx_options=0)
        if blorp['cluster']==4:
            print(bytes(blorp['payload']))
            b = bytearray(blorp['payload'])
            print(b[0])
            payload = bytes([b[0], 00, b[1], b[2], 14, 8, 4, 1, 2, 0, 6, 3, 0, 0, 3, 0, 6, 0, 0])
            xbee.transmit(xbee.ADDR_COORDINATOR, payload, source_ep=0,dest_ep=0,cluster=32772, profile=0, tx_options=0)
        if blorp['cluster'] == 0:
            print(bytes(blorp['payload']))
            b = bytearray(blorp['payload'])
            for x in b:
                print(x)
        print(blorp)

#print(xbee.receive())
#print("temperature")
#print(tp)
#if tp > 0x7FFF:
#    tp = tp - 0x10000
#    print("The XBee is %.1F degrees" % (tp * 9.0 / 5.0 + 32.0))
#for i in list(xbee.discover()):
#    print(i)
#while True:
    # Check if the XBee has any message in the queue.
    # received_msg = xbee.receive()
#    ad0 = Pin("D0", Pin.IN, Pin.PULL_UP)
#    ad1 = Pin("D1", Pin.IN, Pin.PULL_UP)
#    ad2 = Pin("D2", Pin.IN, Pin.PULL_UP)
#    if ad0.value() == 0:
#        print("input pin 0")
#    if ad1.value() == 0:
#        print("input pin 1")
#    if ad2.value() == 0:
#        print("input pin 2")
#    #print("just a print, lots and lots")
#    # if received_msg:
    # Get the sender's 64-bit address and payload from the received message.
#     sender = received_msg['sender_eui64']
#    payload = received_msg['payload']
# Check to make sure data is coming from zigbee controller
#   if sender == b'\x00!.\xff\xff\x06\rW':
# is an on/off command
#       if len(payload) == 3:
#           if payload[2] == 0:
# turn lamp off
#               lamp_ha_state['on_off'] = 0
#               lamp_ha_bytes[1] = 0
#               lamp_ha_bytes[0] = 1
#               senddata = 1
#           elif payload[2] == 1:
#               # turn lamp on
#               lamp_ha_state['on_off'] = 1
#               lamp_ha_bytes[1] = 1
#               lamp_ha_bytes[0] = 1
#               senddata = 1
#           else:
# did not receive 1 or 0
# print("did not receive 1 or 0")
#               pass
# brightness, color, or color temp command
#       if len(payload) > 3:
# is brightness command
#          if payload[2] == 4:
# Home Assistant automatically turns the switch 'on' if brightness
#  is edited.  Therefore, also set on_off to 1 to make sure to match
#  Home Assistant
# print("brightness command")
#             lamp_ha_state['on_off'] = 1
#             lamp_ha_state['brightness'] = payload[3]
#             lamp_ha_bytes[1] = 1
#             lamp_ha_bytes[2] = payload[3]
#             lamp_ha_bytes[0] = 2
#             senddata = 1
# is color command
#        elif payload[2] == 7:
# print("color command")
#            lamp_ha_state['color_x_raw'] = (payload[4] << 8) | payload[3]
#            lamp_ha_bytes[4] = payload[4]
#            lamp_ha_bytes[5] = payload[3]
#            lamp_ha_state['color_y_raw'] = (payload[6] << 8) | payload[5]
#            lamp_ha_bytes[6] = payload[6]
#            lamp_ha_bytes[7] = payload[5]
#            lamp_ha_bytes[0] = 2
# turn lamp on
#           lamp_ha_state['on_off'] = 1
#           lamp_ha_bytes[1] = 1
# lamp_ha_bytes[0] = 1 # not necessary
#          senddata = 1
# is color temp command
#     elif payload[2] == 10:
# print("color temp command")
#        pass
# is unknown data
#    else:
# print("unknown data received %s" % ubinascii.hexlify(payload))
#         pass
#            print("good sender found")
# print(lamp_ha_state)
# print(lamp_ha_bytes)
#            print(lamp_ha_state['color_x_raw']/65535)
#            print(lamp_ha_state['color_y_raw'] / 65535)
# print("===================")
# if senddata == 1:
#    i2c.writeto(arduino_addr, bytearray(lamp_ha_bytes), True)
#    lamp_ha_bytes[0] = 0
#    senddata = 0
# print(len(payload))
# print(ubinascii.hexlify(payload))
#        print("Data received from %s >> %s" % (''.join('{:02x}'.format(x).upper() for x in sender),
#                                               payload.decode()))

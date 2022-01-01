# xbee python docs:  http://cms.digi.com/resources/documentation/digidocs/90002219/#concepts/c_90002219_start.htm?TocPath=Digi%2520MicroPython%2520Programming%2520Guide%257C_____0
# using pycharm w/ xbee: https://www.digi.com/resources/documentation/digidocs/90002445/default.htm
# xbee hardware pdf: https://www.digi.com/resources/documentation/digidocs/pdfs/90001543.pdf
import time
import xbee
import spec
import ubinascii
from machine import I2C
from machine import Pin
import gen
import struct

# print(" +-------------------------------------+")
# print(" +-------------------------------------+\n")

# print("Waiting for data...\n")
# default to everything off and 0 at power on.
#  in the future, we can try to reclaim previous state.
#  Hopefully this lamp won't turn off very often
ad0 = Pin("D0", Pin.IN, Pin.PULL_UP)
ad1 = Pin("D1", Pin.IN, Pin.PULL_UP)
ad2 = Pin("D2", Pin.IN, Pin.PULL_UP)
ad4 = Pin("D4", Pin.OUT)
def status_cb(status):
    print("received status: {:02x}".format(status))

xbee.modem_status.callback(status_cb)
# arduino_addr = 0x48
# senddata = 0
time.sleep(3)
x = xbee.XBee()
#xbee.atcmd('NT', 0xFF)
#tp = xbee.atcmd('TP')1A
xbee.atcmd('KY',b'\x5A\x69\x67\x42\x65\x65\x41\x6C\x6C\x69\x61\x6E\x63\x65\x30\x39')
print(xbee.atcmd('MY'))
print("transmitting")
srcaddr = int(xbee.atcmd('MY'))
print(xbee.atcmd('AI'))
xbee.atcmd('CN')
time.sleep(3)
srcarry = srcaddr.to_bytes(2,"big")


initial_payload=bytes([171, srcarry[1], srcarry[0], 141, 194, 209, 65, 0, 162, 19, 0, 142])
leave_load=bytes([171, srcarry[1], srcarry[0], 209, 65, 0, 162, 19, 0, 2])
print(initial_payload)
#xbee.transmit(xbee.ADDR_COORDINATOR, b'\xAB\xF7\x6A\x8D\xC2\xD1\x41\x00\xA2\x13\x00\x8E', source_ep=0, dest_ep=0, cluster=19, profile=0, tx_options=0)
#xbee.transmit(xbee.ADDR_COORDINATOR, b'\xAB\xF7\x6A\x8D\xC2\xD1\x41\x00\xA2\x13\x00\x8E', source_ep=0, dest_ep=0, cluster=19, profile=0, tx_options=0)
send=0
lame = 0
#while lame < 3:
#    xbee.receive()
#    lame += 1

#while send==0:
#    try:
#        if xbee.transmit(xbee.ADDR_COORDINATOR, leave_load, source_ep=0, dest_ep=0, cluster=52, profile=0, tx_options=0) is None:
#            send = 1
#        print("leaving")
#    except OSError as e:
#        print("leaving transmit error")
#    send=1
send=0
time.sleep(1)
def fancy_transmit(payload, source_ep, dest_ep, cluster,profile):
    send = 0
    while send==0:
        try:
            if xbee.transmit(xbee.ADDR_COORDINATOR, payload, source_ep=source_ep, dest_ep=dest_ep, cluster=cluster, profile=profile,
                             tx_options=0) is None:
                send = 1
                #time.sleep(1)
        except OSError as e:
            time.sleep(1)
            print(payload)
            print(e)


fancy_transmit( payload=initial_payload, source_ep=0, dest_ep=0, cluster=19,profile=0 )
print("receiving")
diff = 3600000
first_report = False
timestamp = time.ticks_ms()
while 1 != 0:
    blorp = xbee.receive()
    if blorp is not None:
        print(blorp)
        if blorp['cluster'] == 6: #genOnOffCluster in HA Profile
            if blorp['profile'] == 260: #HA profile
              cluster_name, seq, CommandType, command_name, disable_default_response, kwargs = spec.decode_zcl(blorp['cluster'], blorp['payload'])
              print(CommandType)
              print(command_name)
              print(kwargs)
              if 'command' in kwargs:
                if kwargs['commands'][0] == 0:
                  ad4.value(1)
                  time.sleep(1)
                  ad4.value(0)
                if kwargs['commands'][1] == 0:
                  ad4.value(1)
                  time.sleep(1)
                  ad4.value(0)
                if kwargs['commands'][2] == 0:
                  ad4.value(1)
                  time.sleep(1)
                  ad4.value(0)
        if blorp['cluster']==5: #active endpoint request
            print(bytes(blorp['payload']))
            b = bytearray(blorp['payload'])
            print(b[0])
            payload=bytes([b[0], 00, b[1], b[2], 1, 8])
            fancy_transmit(payload=payload,source_ep=0,dest_ep=0,cluster=32773, profile=0)
            print("sent-endpoint-response")
        if blorp['cluster']==4: #simple descriptor request
            print(bytes(blorp['payload']))
            b = bytearray(blorp['payload'])
            print(b[0])
            payload = bytes([b[0], 00, b[1], b[2], 14, 8, 4, 1, 2, 0, 6, 3, 0, 0, 3, 0, 6, 0, 0])
            fancy_transmit(payload=payload, source_ep=0, dest_ep=0, cluster=32772, profile=0)
            print("simple descriptor response")

        if blorp['cluster'] == 0: #network address request
            if blorp['profile'] == 260:
              #resp = bytearray(blorp['payload'])
              cluster_name, seq, CommandType, command_name, disable_default_response, kwargs = spec.decode_zcl(blorp['cluster'], blorp['payload'])
              print(command_name)
              print(kwargs)
              if 'attributes' in kwargs:
                attr_bytes=gen.attribute_result(kwargs)
                #payload: control byte, code bytes(2), seq copy, command identifier(read_attributes_response,
                #payload = bytes([4, 30, 16, seq, 1, attr_bytes, 0, 8, 0])
                payload = bytes([12, 30, 16, seq, 1])
                payload = payload+attr_bytes
                #payload= attr_bytes
                print(payload)
                fancy_transmit(payload=payload, source_ep=blorp['dest_ep'], dest_ep=blorp['source_ep'], cluster=blorp['cluster'], profile=blorp['profile'])
              print("attribute_read_response")
              #spec.decode_zcl(blorp['cluster'], blorp['payload'])
            print(bytes(blorp['payload']))
            b = bytearray(blorp['payload'])
            for x in b:
                print(x)
        if blorp['cluster'] == 2: #node descriptor request
            print(bytes(blorp['payload']))
            b = bytearray(blorp['payload'])
            print(b[0])
            payload = bytes([b[0], 00, b[1], b[2], 4, 143, 120, 8, 80, 160, 0, 1, 44, 160, 0, 0])
            fancy_transmit(payload=payload, source_ep=0, dest_ep=0, cluster=32772, profile=blorp['profile'])
            print("node descriptor response")
        if blorp['cluster'] == 32770: #node descriptor response
            print(bytes(blorp['payload']))
            b = bytearray(blorp['payload'])
            print("Node descriptor response integer payload discard")
        #for key, value in blorp.items():
        #1  print (key, ' : ', value)
    if (diff < time.ticks_diff(time.ticks_ms(), timestamp)) or ( not first_report )  :
        timestamp = time.ticks_ms()
        first_report = True
        zcl_head = bytes([12, 30, 16, 171, 10])    
        payload = zcl_head + bytes([0,0,10,0]) #for now only return off for state report
        fancy_transmit(payload=payload, source_ep=8, dest_ep=1, cluster=6, profile=260)


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

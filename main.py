# xbee python docs:  http://cms.digi.com/resources/documentation/digidocs/90002219/#concepts/c_90002219_start.htm?TocPath=Digi%2520MicroPython%2520Programming%2520Guide%257C_____0
# using pycharm w/ xbee: https://www.digi.com/resources/documentation/digidocs/90002445/default.htm
# xbee hardware pdf: https://www.digi.com/resources/documentation/digidocs/pdfs/90001543.pdf
import time
import xbee
import spec
import barrier
from machine import Pin
import gen
import com
from micropython import const
import struct

#ad0 = Pin("D0", Pin.IN, Pin.PULL_UP)
#ad1 = Pin("D1", Pin.IN, Pin.PULL_UP)
#ad2 = Pin("D2", Pin.IN, Pin.PULL_UP)help
while xbee.atcmd("AI") != 0:
  time.sleep(0.1)
ad4 = Pin("D4", Pin.OUT, value=0)
def status_cb(status):
    print("m stat: {:02x}".format(status))

xbee.modem_status.callback(status_cb)
# arduino_addr = 0x48
# senddata = 0
key = b'\x5A\x69\x67\x42\x65\x65\x41\x6C\x6C\x69\x61\x6E\x63\x65\x30\x39'
#_key = const(0x5A 0x69 0x67 0x42 0x65 0x65 0x41 0x6C 0x6C 0x69 0x61 0x6E 0x63 0x65 0x30 0x39)
xbee.atcmd('KY', key)


#leave_load=bytes([171, srcarry[1], srcarry[0], 209, 65, 0, 162, 19, 0, 2])
#xbee.transmit(xbee.ADDR_COORDINATOR, b'\xAB\xF7\x6A\x8D\xC2\xD1\x41\x00\xA2\x13\x00\x8E', source_ep=0, dest_ep=0, cluster=19, profile=0, tx_options=0)
#xbee.transmit(xbee.ADDR_COORDINATOR, b'\xAB\xF7\x6A\x8D\xC2\xD1\x41\x00\xA2\x13\x00\x8E', source_ep=0, dest_ep=0, cluster=19, profile=0, tx_options=0)
#send=0
com.announce()
time.sleep(1)

print("receiving")

#war_header=b'\x10'
#payload_header=b'\x0c\x1e\x10'
_rap=const(0x01) #read attribute response
_dap=const(0x0d) #discover attribute response
_war=const(0x05) #write attribute no response
_ra =const(0x0a)  #report attributes
oob=b'\xab' #out of band sequence number
duint8 = b'\x20'
duint16 =b'\x21'
denum8 = b'\x30'
dbool =  b'\x10'
SUCCESS = b'\x00'

def main_loop ():
  diff = 10000
  first_report = False
  timestamp = time.ticks_ms()
  garage = barrier.Barrier()
  payload_header = b'\x18'
  while 1 != 0:
      packet = com.receive()
      if packet is not None:
          print(packet)
          b = bytearray(packet['payload'])
          print(b[0])
          if packet['cluster'] == 259:  #barrier cluster
              cluster_name, seq, CommandType, command_name, disable_default_response, kwargs = spec.decode_zcl(
                  packet['cluster'], packet['payload'])
              print("printing kwargs for incoming packet")
              print(command_name)
              if "attributes" in kwargs:
                  #garage.status(seq,packet['payload'])
                  print("found attribute request")
                  stat=garage.status(seq, kwargs)
                  if stat != 'b\xffff':
                      print("garage status")
                      payload = payload_header+ bytes([seq])+ bytes([_rap]) + stat
                      print(payload)
                      com.fancy_transmit(payload=payload, source_ep=packet['dest_ep'], dest_ep=packet['source_ep'], cluster=packet['cluster'], profile=packet['profile'])
              #if CommandType is not None:
              if command_name == "stop":
                  garage.command(seq, packet['payload'])
                  payload = payload_header + bytes([seq]) + bytes([_def]) + 'b\x01' + 'b\x00'
                  com.fancy_transmit(payload=payload, source_ep=packet['dest_ep'], dest_ep=packet['source_ep'], cluster=packet['cluster'], profile=packet['profile'])
              pass
          if packet['cluster'] == 6: #genOnOffCluster in HA Profile
              if packet['profile'] == 260: #HA profile
                cluster_name, seq, CommandType, command_name, disable_default_response, kwargs = spec.decode_zcl(packet['cluster'], packet['payload'])
                # print(packet['payload'])
                # print(CommandType)
                # print(command_name)
                # print(kwargs)
                if "attributes" in kwargs:
                    if kwargs['attributes'][0] == 0:
                      payload = payload_header + bytes([seq]) + bytes([_rap]) + bytes([0,0])+ SUCCESS + dbool + bytes([ad4.value()])
                      print(payload)
                      com.fancy_transmit(payload=payload, source_ep=packet['dest_ep'], dest_ep=packet['source_ep'],
                                       cluster=packet['cluster'], profile=packet['profile'])
                    if kwargs['attributes'][0] == 10:
                      payload = payload_header + bytes([seq]) + bytes([_rap]) + bytes([0, 0, 16, ad4.value()])
                      print(payload)
                      com.fancy_transmit(payload=payload, source_ep=packet['dest_ep'], dest_ep=packet['source_ep'],
                                   cluster=packet['cluster'], profile=packet['profile'])
                if command_name == "on":
                    ad4.value(1)
                if command_name == "off":
                    ad4.value(0)
                if command_name == "toggle":
                    ad4.value(1)
                    time.sleep(1)
                    ad4.value(0)
          if packet['cluster']==5: #active endpoint request
              print(bytes(packet['payload']))
              b = bytearray(packet['payload'])
              print(b[0])
              payload=bytes([b[0], 00, b[1], b[2], 1, 1])           
              com.fancy_transmit(payload=payload,source_ep=0,dest_ep=0,cluster=32773, profile=0)
              print("sent-endpoint-response")
          if packet['cluster']==4: #simple descriptor request
              print(bytes(packet['payload']))
              b = bytearray(packet['payload'])
              print(b[0])
              payload = bytes([b[0], 00, b[1], b[2], 14, 1, 4, 1, 2, 0, 6, 4, 0, 0, 3, 0, 6,0, 3, 1,0, 0])
              com.fancy_transmit(payload=payload, source_ep=0, dest_ep=0, cluster=32772, profile=0)
              print("simple descriptor response")

          if packet['cluster'] == 0: #network address request
              if packet['profile'] == 260:
                cluster_name, seq, CommandType, command_name, disable_default_response, kwargs = spec.decode_zcl(packet['cluster'], packet['payload'])
                print(command_name)
                print(kwargs)
                if 'attributes' in kwargs:
                  attr_bytes=gen.attribute_result(kwargs)
                  zcl_header = payload_header + bytes([seq]) + _rap
                  payload = zcl_header+attr_bytes
                  print(payload)
                  com.fancy_transmit(payload=payload, source_ep=packet['dest_ep'], dest_ep=packet['source_ep'], cluster=packet['cluster'], profile=packet['profile'])
                print("attribute_read_response")
                #spec.decode_zcl(packet['cluster'], packet['payload'])
              print(bytes(packet['payload']))
              b = bytearray(packet['payload'])
              for x in b:
                  print(x)
          if packet['cluster'] == 2: #node descriptor request
              print(bytes(packet['payload']))
              b = bytearray(packet['payload'])
              print(b[0])
              payload = bytes([b[0], 00, b[1], b[2], 4, 143, 120, 8, 80, 160, 0, 1, 44, 160, 0, 0])
              com.fancy_transmit(payload=payload, source_ep=0, dest_ep=0, cluster=32772, profile=packet['profile'])
              print("node descriptor response")
          if packet['cluster'] == 32770: #node descriptor response
              print(bytes(packet['payload']))
              b = bytearray(packet['payload'])
              print("Node descriptor response integer payload discard")
          #for key, value in packet.items():
          #1  print (key, ' : ', value)
          #print(time.ticks_diff(time.ticks_ms(),timestamp))
      if (diff < time.ticks_diff(time.ticks_ms(), timestamp)) or (not first_report):
          timestamp = time.ticks_ms()
          first_report = True
          #payload = bytes([12, 30, 16, 171, 5,0, 0, 0, 16, ad4.value()])  # zcl_header
          #payload =  bytes([])
          #payload = zcl_head# + payload
          garage.watch()
          zcl_header = payload_header + oob + bytes([_ra])
          payload=zcl_header+garage.position()+garage.movement()
          #dumb = bytes([12, 30, 16, 171, 5])
          #com.fancy_transmit(payload=bytes([12, 30, 16, 171, 10])+florp, source_ep=8, dest_ep=1, cluster=6, profile=260)
          com.fancy_transmit(payload=payload , source_ep=1, dest_ep=1, cluster=259, profile=260)
      if garage.watch():
          #payload_header + oob + bytes([_war])
          payl = payload_header + oob + bytes([_ra]) + garage.position()+ garage.movement()
          print("door: "+ str(garage.door))
          print("motor: "+ str(garage.motor))
          print("moving: "+ str(garage.moving))
          print("barrierPosition: "+ str(garage.barrier_position))
          print(payl)
          com.fancy_transmit(payload=payl, source_ep=1, dest_ep=1, cluster=259, profile=260)
          time.sleep(1)
          garage.update = False


while 1 != 0:
  try:
      main_loop()
  except Exception as e:
      print(str(e))
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

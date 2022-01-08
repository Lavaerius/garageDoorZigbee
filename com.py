import time
import xbee
def receive():
    return xbee.receive()

def announce():
    srcaddr = xbee.atcmd('MY')
    xbee.atcmd('CN')
    srcarry = srcaddr.to_bytes(2, "big")
    initial_payload=bytes([171, srcarry[1], srcarry[0], 141, 194, 209, 65, 0, 162, 19, 0, 142])
    xbee.transmit(xbee.ADDR_COORDINATOR,initial_payload, source_ep=0, dest_ep=0, cluster=19,profile=0, tx_options=0)

def fancy_transmit(payload, source_ep, dest_ep, cluster,profile):
    send = 0
    while send == 0:
        try:
            if xbee.transmit(xbee.ADDR_COORDINATOR, payload, source_ep=source_ep, dest_ep=dest_ep, cluster=cluster, profile=profile,
                             tx_options=0) is None:
                send = 1
        except OSError as e:
            time.sleep(1)
           # print("connection status: {stat}".format(stat=str(xbee.atcmd('AI'))))
            if xbee.atcmd('AI') == 'b\x23':
              print("we burnin")
              xbee.atcmd('NR')
              xbee.atcmd('CN')
              announce()
              i = 0
            while i<4:
              receive()
              i+=1
              #print(payload)
              #print(e)
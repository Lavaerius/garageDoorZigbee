import time
import xbee
def receive():
    return xbee.receive()

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
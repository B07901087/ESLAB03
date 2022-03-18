# ble_scan_connect.py:
from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)
scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
n=0
addr = []
for dev in devices:
    print ("%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr, 
    dev.addrType, dev.rssi))
    addr.append(dev.addr)
    n += 1
    for (adtype, desc, value) in dev.getScanData():
        print (" %s = %s" % (desc, value))
number = input('Enter your device number: ')
print ('Device', number)
num = int(number)
print (addr[num])
#
print ("Connecting...")
dev = Peripheral(addr[num], 'random')
#
print ("Services...")
for svc in dev.services:
    print (str(svc))
#
import struct
from bluepy.btle import *


class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print(data)



try:
    testService = dev.getServiceByUUID(UUID(0xfff0))
    for ch in testService.getCharacteristics():
        print (str(ch))
#
    ch = dev.getCharacteristics(uuid=UUID(0xfff1))[0]
    if (ch.supportsRead()):
        print (ch.read())

    dev.setDelegate(MyDelegate())

    print("Connected")
    '''
    ch = dev.getCharacteristics(uuid=UUID(0xfff4))[0]
    # ch = ch + 2
    handle = ch.getHandle()
    print(f"the handle is: {handle}")
    if (ch.supportsRead()):
        print (ch.read())
    
    notify_setup = b"\x02\x00"
    dev.writeCharacteristic(handle, notify_setup, withResponse=True)
    print("writing done")
    while True:
        if dev.waitForNotifications(1.0):
            print("notifications")
            dev.readCharacteristic(handle)
            break
    '''
    for i in dev.getDescriptors():
        print(f"UUID: {i.uuid}")


finally:
    dev.disconnect() 
#





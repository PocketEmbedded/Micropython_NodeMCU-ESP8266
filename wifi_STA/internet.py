########################################################################
# App   : Wifi_STA
# Author: Pocket Embedded
# Created On: 09/06/2020
# File_name:internet.py
#########################################################################
from machine import Pin
led=Pin(2,Pin.OUT)
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect("Net","123456789")
        led.off()
        while not wlan.isconnected():
            pass
    print('network config',wlan.ifconfig())


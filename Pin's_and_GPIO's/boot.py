########################################################################
# App   : Blinking LED
# Author: Pocket Embedded
# Created On: 08/06/2020
#
#########################################################################
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#uos.dupterm(None, 1) # disable REPL on UART(0)
import uos, machine
from machine import Pin
import time
led = Pin(2, Pin.OUT)
while True:
    led.on()
    time.sleep(2)
    led.off()
    time.sleep(2)

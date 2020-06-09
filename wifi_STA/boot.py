########################################################################
# App   : Wifi_STA
# Author: Pocket Embedded
# Created On: 09/06/2020
# File_name:boot.py
#########################################################################
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#uos.dupterm(None, 1) # disable REPL on UART(0)
import uos, machine
from machine import Pin
import time
import network
import internet
led=Pin(2,Pin.OUT)
led.on()
internet.do_connect()
led.on()


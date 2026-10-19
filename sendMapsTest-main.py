'''
Description: Send map when a request is sent on a given channel
Author: S. Brophy
Date: October 19, 2025
'''

# Imports go at the top
from microbit import *
import radio
map = 'S00000101100010010100100X'
radio.config(channel=xx)              # substitute your team number for the channel
radio.on()
msg = ''                              #
x = 0
cnt = 0
def update_progress(cnt):
    if cnt<50:
        if cnt%10:
            x = cnt//10
            display.set_pixel(x,2,9)
    else:
        cnt = 0
        display.clear()
    return cnt+1      
# Code in a 'while True:' loop repeats forever
while True:
# Wait for request
    msg = radio.receive()
    if msg:
        radio.send(map)
        print(msg)
    else:
        cnt=update_progress(cnt)
    sleep(250)

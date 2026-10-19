# from microbit import *
# import radio
import PathSearchCode as psc


# radio.config(channel=13)
# radio.on()
while True:
    #msg = radio.receive()
    msg = "S01000010001110000101000X"
    if msg:
        map = [msg[0:5], msg[5:10], msg[10:15], msg[15:20], msg[20:25]]
        print(psc.pathSearch(map))
        break
        



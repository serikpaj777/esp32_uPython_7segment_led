import network
import usocket as socket

ap = network.WLAN(network.AP_IF)
#
# values for autmode
#    0 - open
#    1 - WEP
#    2 - WPA-PSK
#    3 - WPA2-PSK
#    4 - WPA/WPA2-PSK
#
# values for hidden
#    0 - visible
#    1 - hidden
#ap.config(essid='uPython', authmode=3, password='135135135', hidden=1)
ap.config(essid='uPython', authmode=3, password='135135135')
ap.active(True)
while ap.active()==False:
    pass
print('connection successful......')
print(ap.ifconfig())

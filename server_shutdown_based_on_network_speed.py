## Outbound Traffic Monitor v0.1 - Jan 2014
## Shutdown the server if the maximum outbound speed is reached.

# Set the interface you wish to monitor, eg: eth0, wlan0, usb0
INTERFACE = "eth0"

# Set the maximum out speed in KB/s, shutdown the server if reached.
MAXIMUM_SPEED = 15

# Set the number of retries to test for the average maximum speed. If the average speed is greater
# than the maximum speed for x number of retries, then shutdown.
RETRIES = 5

# Set the interval (in seconds), between retries to test for the maximum speed.
INTERVAL = 5


import os, time
from commands import getoutput

def worker ():
    RETRIES_COUNT = RETRIES
    while True:
        SPEED = int(float(getoutput("ifstat -i %s 1 1 | awk '{print $1}' | sed -n '3p'" % INTERFACE)))
        if (SPEED < MAXIMUM_SPEED and RETRIES_COUNT <= 0):
            os.system("shutdown -h now")
        elif SPEED < MINIMUM_SPEED:
            RETRIES_COUNT -= 1
            time.sleep(INTERVAL)
        else:
            RETRIES_COUNT = RETRIES
            time.sleep(INTERVAL)

worker()

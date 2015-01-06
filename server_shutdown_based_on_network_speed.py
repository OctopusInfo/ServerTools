## Download Monitor v0.1 - March 2012

# Set the interface you wish to monitor, eg: eth0, wlan0, usb0
INTERFACE = "eth0"

# Set the minimum download speed in KB/s that must be achieved.
MAXIMUM_SPEED = 2500 #2.5 MB/s or 20Mb/s

# Set the number of retries to test for the average minimum speed. If the average speed is less
# than the minimum speed for x number of retries, then shutdown.
RETRIES = 3

# Set the interval (in seconds), between retries to test for the minimum speed.
INTERVAL = 5


import os, time
from commands import getoutput

def worker ():
    RETRIES_COUNT = RETRIES
    while True:
        SPEED = int(float(getoutput("ifstat -i %s 1 1 | awk '{print $1}' | sed -n '3p'" % INTERFACE)))
        if (SPEED > MAXIMUM_SPEED and RETRIES_COUNT <= 0):
            os.system("shutdown -h now")
        elif SPEED > MAXIMUM_SPEED:
            RETRIES_COUNT -= 1
            time.sleep(INTERVAL)
        else:
            RETRIES_COUNT = RETRIES
            time.sleep(INTERVAL)

worker()

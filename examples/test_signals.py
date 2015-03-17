import sys
import time

sys.path.append('../')

from LocationApi import *


def __show_help():
    print "--------------------------"
    print "python test_signal.py show_all: Show all SSIDs found"
    print "python test_signal.py trace --rssi *<ssid>: trace the rssi of the given ssid"
    print "python test_signal.py trace --distance *<ssid>: trace the distance of the given ssid"
    print "python test_signal.py help: show this help guide"

def __cal_distances(signals):
    #dLink_transmit_power = 15
    unit_strength = -63
    freqInMHz  = 2462
    path_loss_exponent = 2
    return calDistance(freqInMHz, unit_strength, path_loss_exponent, signals)

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0 or (len(args) > 0 and "help" == args[0]): 
        __show_help()
    elif "show_all" == args[0]:
        listAllNetwork()
    elif "trace" == args[0] and len(args) > 2:
        while True: 
            time.sleep(3)
            if "--rssi" == args[1]:
                print getSignalfor(args[2:])
            elif "--distance" == args[1]:
                siganls = getSignalfor(args[2:])
                print __cal_distances(siganls)
            else:
                __show_help()
                break
    else:
        __show_help()
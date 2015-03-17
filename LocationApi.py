import math
from WindowsWifi import *

def getSignalfor(ssids):
    ifaces = getWirelessInterfaces()
    for iface in ifaces:
        #scanWlan(iface)
        networks = getWirelessAvailableNetworkList(iface)
        bssList = getWirelessNetworkBssList(iface)

        signals = []
        
        for network in networks:
            if not network.ssid in ssids:
                continue

            best_streanth = -100
            signal_value = {}
            values = {}
            values["network_rssi"] = int(-100+(network.signal_quality/2))
            for bss in bssList:
                if network.ssid == bss.ssid:
                    if bss.rssi > best_streanth:
                        best_streanth = bss.rssi

                    values["bss_rssi"] = best_streanth

            signal_value[network.ssid] = values
            signals.append(signal_value)

        return signals

def calDistance(freqInMHz, unit_strength, path_loss_exponent, signals):
    distances = []
    for signal in signals:
        print signal
        for ssid in signal.keys():
            network_rssi = signal[ssid]["network_rssi"]
            #result = (unit_strength - (20 * math.log10(freqInMHz)) + math.fabs(network_rssi)) / 20.0
            #meters = math.pow(10, result)
            meters = __general_modle(freqInMHz, unit_strength, path_loss_exponent, network_rssi)
            one_distance = {}
            one_distance[ssid] = meters

            distances.append(one_distance)

    return distances


def __general_modle(freqInMHz, unit_strength, path_loss_exponent, rssi):
    return math.pow(10, (rssi - unit_strength)/((-10.0)*path_loss_exponent))

def __itu_modle(freqInMHz, unit_strength, path_loss_exponent, rssi):
    lost = rssi - unit_strength
    print lost
    power = (lost-45.6)/30
    print power
    return math.pow(10, power) 


def listAllNetwork():
    ifaces = getWirelessInterfaces()
    for iface in ifaces:
        print iface
        networks = getWirelessAvailableNetworkList(iface)
        bssList = getWirelessNetworkBssList(iface)
        print ""
        for network in networks:
            if network.ssid == "":
                continue

            print network.ssid
            print network.bss_type
            print ("Signal Quality: " + str(network.signal_quality) + "%")

            best_streanth = -10
            for bss in bssList:
                if network.ssid == bss.ssid and bss.rssi < best_streanth:
                    best_streanth = bss.rssi

                if best_streanth < -100:
                    best_streanth = -100
            print "Signal Streath: " + str(best_streanth)
            print "-" * 20
        print ""
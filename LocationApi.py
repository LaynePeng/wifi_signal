from WindowsWifi import *

def getSignalfor(*ssids):
    ifaces = getWirelessInterfaces()
    for iface in ifaces:
        networks = getWirelessAvailableNetworkList(iface)
        bssList = getWirelessNetworkBssList(iface)

        signals = []
        
        for network in networks:
            if network.ssid not in ssids:
                continue

            best_streanth = -10
            for bss in bssList:
                if network.ssid == bss.ssid and bss.rssi < best_streanth:
                    best_streanth = bss.rssi

                if best_streanth < -100:
                    best_streanth = -100

            signal_value = {}
            signal_value[network.ssid] = best_streanth

            signals.append(signal_value)

        return signals
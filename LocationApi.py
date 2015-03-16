from WindowsWifi import *

def getSignalfor(*ssids):
    ifaces = getWirelessInterfaces()
    for iface in ifaces:
        #scanWlan(iface)
        networks = getWirelessAvailableNetworkList(iface)
        bssList = getWirelessNetworkBssList(iface)

        signals = []
        
        for network in networks:
            if network.ssid not in ssids:
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
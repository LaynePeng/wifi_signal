# -*- coding: utf-8 -*-
# Author: Jing Chen @ EMC Corp. jing.chen2@emc.com
#

import time

from WindowsWifi import getWirelessInterfaces
from WindowsWifi import getWirelessAvailableNetworkList
from WindowsWifi import runWlanScan

import math

def quality2strength(quality):
    """
        The quality2strength function converts the signal quality in percentage into signal strength in dBm.
        dBm is the power ratio in decibels of the measured power referenced to one milliwatt.
    """
    if isinstance(quality, (int, long)):
        if quality >= 0 and quality <= 100:
            strength = 0.6 * quality - 95.6
            return strength
        else:
            print "The signal quality input must be an integer ranging from 0 to 100!"
            raise OverflowError
    else:
        print "The signal quality input must be an integer!"
        raise TypeError

def calculate_distance(quality, offset):
    """
        The get_distance function calculates the distance to the AP by the received signal quality in percentage.
        The return value is the distance in centimeter.
    """
    distance = 10 ** (  (27.55 - (20*math.log10(2412)) - quality2strength(quality)) / 20.0  )
    distance_in_centimeters = 100 * distance + offset
    return distance_in_centimeters

def get_distance(ssid_in, offset):
    ifaces = getWirelessInterfaces()
    iface0 = ifaces[0]
    distance = []
    quality = []
    strength = []
    for i in range(3):
        time.sleep(5)
        print time.ctime(),
        runWlanScan(iface0)
        networks = getWirelessAvailableNetworkList(iface0)
        for network in networks:
            if network.ssid == ssid_in:
                print network.ssid, '\t', network.signal_quality,'%\t', quality2strength(network.signal_quality), 'dB\t', calculate_distance(network.signal_quality, offset), 'cm'
                distance.append(calculate_distance(network.signal_quality, offset))
                quality.append(network.signal_quality)
                strength.append(quality2strength(network.signal_quality))
    
    sum_dis = sum(distance)
    sum_qul = sum(quality)
    sum_str = sum(strength)
    if len(distance):
        averaged_distance = sum_dis / float(len(distance))
        averaged_quality = sum_qul / float(len(quality))
        averaged_strength = sum_str / float(len(strength))
    else:
        averaged_distance = 9999999.99
        averaged_quality = 0
        averaged_strength = -95.6
    print averaged_distance, averaged_quality, averaged_strength
    return {"distance":averaged_distance, "quality":averaged_quality, "strength":averaged_strength}

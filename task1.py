#!/usr/local/bin/python3
# Task number 1
from typing import re

NAT = "ip nat inside source list ACL interface FastEthernet0/1overload"


def change_name(name):
    return str(name).replace("FastEthernet", "GigabitEthernet")


print(change_name(NAT))

# Task number 2

mac = 'AAAA:BBBB:CCCC'


def mac_format_changer(adr):
    return str(adr).replace(':', '.', 2)


print(mac_format_changer(mac))

# Task 3
config = 'switchport trunk allowed vlan 1,3,10,20,30,100'


def number_spliterator(string):
    modified = ''.join(c for c in string if c.isdigit() or c == ',')
    return modified.split(',')


print(number_spliterator(config))

# Task 4
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]


def de_dublicator(lans):
    return list(dict.fromkeys(lans))


print(de_dublicator(vlans))

# Task 5


command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = "switchport trunk allowed vlan 1,3,8,9"


def show_duplicated_trunks(trunk1, trunk2):
    intersection = list(set(number_spliterator(trunk1)).intersection(number_spliterator(trunk2)))
    list.sort(intersection)

    return intersection


print(show_duplicated_trunks(command1, command2))

# Task 6

ospf_route = 'O  10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0 ,→'


def print_route_ospf(route):
    split = str(route).split(" ")
    print("Protocol: OSPF")
    print("Prefix:" + split[2])
    print("AD/Metric: " + split[3])
    print("Next-Hop " + split[5])
    print("Last update : " + split[6])
    print("Outbound Interface: " + split[7])


print_route_ospf(ospf_route)

# Task 7

mac = 'AAAA:BBBB:CCCC'


def mac_to_binary(address):
    return str(bin(int(str(address).replace(':', ''), 16))).replace("0b", "")


print(mac_to_binary(mac))

# Task 8

ip = '10.1.1.1'


def ip_to_binary(ip_address):
    return ' '.join([bin(int(x)+256)[3:] for x in ip_address.split('.')])


print(ip_to_binary(ip))

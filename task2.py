#!/usr/local/bin/python3

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']


def reformat_mac(address: list):
    result = []
    for m in address:
        result.append(str(m).replace(":", ".", 2))
    return result


print(reformat_mac(mac))


def ip_type(ip):
    i = list(str(ip).split("."))
    if ip == "255.255.255.255":
        print("local broadcast")
    elif ip == "0.0.0.0":
        print("unassigned")
    elif int(i[0]) in range(1, 224):
        print("unicast")
    elif int(i[0]) in range(224, 240):
        print("multicast")
    else:
        print("unused")


ip_type(input())


def check_ip(ip):
    ip_as_list = str(ip).split(".")
    for b in ip_as_list:
        if not b.isdigit():
            return False
        if int(b) not in range(0, 256):
            return False
    else:
        return True


def ip_type_checked(ip):
    if check_ip(ip):
        ip_type(ip)
    else:
        print("Wrong Ip")


ip_type_checked(input())


def ip_type_checked_cont(ip):
    if check_ip(ip):
        ip_type(ip)
    else:
        ip_type_checked_cont(input())


ip_type_checked_cont(input())




access_template = [
'switchport mode access', 'switchport access vlan',
'spanning-tree portfast', 'spanning-tree bpduguard enable'
]
trunk_template = [
'switchport trunk encapsulation dot1q', 'switchport mode trunk',
'switchport trunk allowed vlan'
]
access = {
'0/12': '10',
'0/14': '11',
'0/16': '17',
'0/17': '150'
}
trunk = {
'0/1': ['add', '10', '20'],
'0/2': ['only', '11', '30'],
'0/4': ['del', '17']
}

for intf, allowed in trunk.items():
    action = (
        allowed[0].replace("only", "").replace("del", " remove").replace("add", " add")
    )
    vlans = ",".join(allowed[1:])

    print("interface FastEthernet" + intf)
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            print(' {} {} {} '.format(command, action, vlans) )
        else:
            print(' {}'.format(command))

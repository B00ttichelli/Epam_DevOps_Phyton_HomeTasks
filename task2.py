#!/usr/local/bin/python3

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']


def reformat_mac(address: list):
    result = []
    for m in address:
        result.append(str(m).replace(":", ".", 2))
    return result


print(reformat_mac(mac))


# В зависимости от типа адреса, вывести на стандартный поток вывода:
# •  „unicast“ - если первый байт в диапазоне 1-223
# •  „multicast“ - если первый байт в диапазоне 224-239
# •  „local broadcast“ - если IP-адрес равен 255.255.255.255
# •  „unassigned“ - если IP-адрес равен 0.0.0.0
# •  „unused“ - во всех остальных случаях


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
        print("Неправильный IP-адрес")


ip_type_checked(input())


def ip_type_checked_cont(ip):
    if check_ip(ip):
        ip_type(ip)
    else:
        ip_type_checked_cont(input())


ip_type_checked_cont(input())

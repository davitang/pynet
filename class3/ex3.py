import json
from pprint import pprint

with open("interfaces_data.json") as f:
    interfaces = json.load(f)
    #pprint(intf_data)
    ipv4_list = []
    ipv6_list = []

    for interface in interfaces.values():
        ipv4_addrs = interface.get("ipv4")
        ipv6_addrs = interface.get("ipv6")
        if ipv4_addrs:
            for ip_addr, prefix_len in ipv4_addrs.items():
                ipv4_list.append(ip_addr + "/" + str(prefix_len['prefix_length'])) 

        if ipv6_addrs:
            for ipv6_addr, prefix_len in ipv6_addrs.items():
                ipv6_list.append(ipv6_addr + "/" + str(prefix_len['prefix_length']))

    print("IPV4 LIST:")
    pprint(ipv4_list)
    print("IPV6 LIST:")
    pprint(ipv6_list)

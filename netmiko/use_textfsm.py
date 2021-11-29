from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

password = getpass()
device = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**device)

show_version = net_connect.send_command_timing("show version", use_textfsm=True)
show_lldp_nei = net_connect.send_command_timing("show lldp neighbors", use_textfsm=True)
net_connect.disconnect()

print('-' * 80)
pprint(show_version)
print('-' * 80)
pprint(show_lldp_nei)
print('-' * 80)
print(f"Remote device: {show_lldp_nei[0]['neighbor']}, Remote inteface: {show_lldp_nei[0]['neighbor_interface']}")

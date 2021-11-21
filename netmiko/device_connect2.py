from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device1 = {
    'host':'nxos1.lasthop.io',
    'username':'pyclass',
    'password':password,
    'device_type':'cisco_nxos'
}


device2 = {
    'host':'nxos2.lasthop.io',
    'username':'pyclass',
    'password':password,
    'device_type':'cisco_nxos'
}

devices = [device1, device2]

for device in devices:
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    net_connect.disconnect()



from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

nxos1 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': password,
}


nxos2 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': password,
}

for device in [nxos1, nxos2]:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_from_file('vlan_change.txt')
    output += net_connect.save_config()
    print('-' * 80)
    print(output)
    print('-' * 80)
    net_connect.disconnect()



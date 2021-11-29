from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = getpass()

device = {
    "host": "nxos2.lasthop.io",
    "device_type": "cisco_nxos",
    "username": "pyclass",
    "password": password,
    "global_delay_factor": 2,
}

net_connect = ConnectHandler(**device)

start_time = datetime.now()
output = net_connect.send_command("show lldp neighbors detail")
output += net_connect.send_command("show ip interface brief")
output += net_connect.send_command("show ip arp")
end_time = datetime.now()
print("-" * 80)
print(output)
print("-" * 80)
print("\n\nExecution Time: {}".format(end_time - start_time))
print()


start_time = datetime.now()
output = net_connect.send_command("show lldp neighbors detail", delay_factor=8)
output += net_connect.send_command("show ip interface brief")
output += net_connect.send_command("show ip arp")
end_time = datetime.now()
print("-" * 80)
print(output)
print("-" * 80)
print("\n\nExecution Time: {}".format(end_time - start_time))
print()

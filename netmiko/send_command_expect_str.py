from netmiko import ConnectHandler
from getpass import getpass

password = getpass()
device = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**device)

output = net_connect.send_command("ping", expect_string=r"Protocol", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Target IP", strip_prompt=False, strip_command=False)
output += net_connect.send_command("8.8.8.8", expect_string=r"Repeat count", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Datagram size", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Timeout", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Extended", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Sweep", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"#", strip_prompt=False, strip_command=False)
net_connect.disconnect()

print('-'*80)
print(output)
print('-'*80)

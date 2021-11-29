from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = getpass()

device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "fast_cli": True,
}

cmds = [
    "ip name-server 1.1.1.1",
    "ip name-server 1.0.0.1",
    "ip domain-lookup"
]

net_connect = ConnectHandler(**device)

start_time = datetime.now()
output = net_connect.send_config_set(cmds, strip_prompt=False, strip_command=False)
output += net_connect.send_command("ping google.com", expect_string=r'#')
end_time = datetime.now()

print("-" * 80)
print(output)
print("-" * 80)
print(f"\n\nExecution Time: {end_time - start_time}")

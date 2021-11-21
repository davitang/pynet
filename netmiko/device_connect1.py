from netmiko import ConnectHandler
from getpass import getpass

device1 = ConnectHandler(
    host='nxos1.lasthop.io',
    username='pyclass',
    password=getpass(),
    device_type='cisco_nxos',
    #session_log='session_nxos1.txt',
)

print(device1.find_prompt())

device1.disconnect()

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device
from pprint import pprint
from lxml import etree

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

cmds = [
    "show system uptime",
    "show system resources"
]
output = device.show_list(cmds)
print("output of XML response:")
print("-"*20)
for elem in output:
    print(etree.tostring(elem).decode())

cfg_cmds = [
    "interface lo 111",
    "description DUMMY LOOKBACK I",
    "ip addr 192.168.111.111 255.255.255.255",
    "interface lo 122",
    "description DUMMY LOOKBACK II",
    "ip addre 192.168.122.122 255.255.255.255"
]

output = device.config_list(cfg_cmds)
print("output of config XML response:")
print("-"*20)
for elem in output:
    print(etree.tostring(elem).decode())

print("Verification:")
output = device.show("show ip interface brief")
print(etree.tostring(output).decode())
print()

print("clean the config:")
clean_cmds = [
    "no interface lo111",
    "no interface lo122"
]

output = device.config_list(clean_cmds)
print("output of config XML response:")
print("-"*20)
for elem in output:
    print(etree.tostring(elem).decode())

print("Verification:")
output = device.show("show ip interface brief")
print(etree.tostring(output).decode())
print()


import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device
from pprint import pprint

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show interface Ethernet1/1")
intf_name = output['TABLE_interface']['ROW_interface']['interface']
state = output['TABLE_interface']['ROW_interface']['state']
MTU = output['TABLE_interface']['ROW_interface']['eth_mtu']
print(f"interface: {intf_name}; state: {state}; MTU: {MTU}")

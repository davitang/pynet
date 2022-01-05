import pyeapi
import yaml
from getpass import getpass
from pprint import pprint

with open("./arista4_device.yml") as f:
    device = yaml.safe_load(f)

device['password'] = getpass()

connection = pyeapi.client.connect(**device)

device = pyeapi.client.Node(connection)
show_arp_output = device.enable("show ip arp")

for item in show_arp_output[0]["result"]["ipV4Neighbors"]:
    print(f"IP: {item['address']:15} -> MAC: {item['hwAddress']}")

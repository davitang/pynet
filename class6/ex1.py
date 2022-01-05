import pyeapi
from pprint import pprint

connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    port="443",
    username="pyclass",
    password="88newclass",
)

device = pyeapi.client.Node(connection)
show_arp_output = device.enable("show ip arp")

for item in show_arp_output[0]["result"]["ipV4Neighbors"]:
    print(f"IP: {item['address']:15} -> MAC: {item['hwAddress']}")

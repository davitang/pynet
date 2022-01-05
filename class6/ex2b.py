import pyeapi
from my_funcs import get_device, print_table

filename = "arista4_device.yml"
device = get_device(filename)

connection = pyeapi.client.connect(**device)
device = pyeapi.client.Node(connection)
show_arp_output = device.enable("show ip arp")

print_table(show_arp_output)

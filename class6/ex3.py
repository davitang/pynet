import pyeapi
from my_funcs import get_device
from pprint import pprint

filename = "arista4_device.yml"
device = get_device(filename)

connection = pyeapi.client.connect(**device)
device = pyeapi.client.Node(connection)
output = device.enable("show ip route")

for route, params in output[0]['result']['vrfs']['default']['routes'].items():
    if not params['directlyConnected']:
        print(f"Route: {route:20}, Type: Static, Next-hop: {params['vias'][0]['nexthopAddr']:15}")
        continue
    print(f"Route: {route:20}, Type: Connected")
    

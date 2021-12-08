import yaml
from pprint import pprint
from os import path
from netmiko import ConnectHandler

home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")

with open(filename) as f:
    devices = yaml.load(f, yaml.Loader)
    #pprint(devices)
    cisco3 = devices['cisco3']
    net_connect = ConnectHandler(**cisco3)
    print()
    print(net_connect.find_prompt())
    print()

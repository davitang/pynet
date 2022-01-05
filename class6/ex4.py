import pyeapi
from my_funcs import get_devices, config_gen
from pprint import pprint
#import ipdb

#ipdb.set_trace()

filename = "arista_devices.yml"
devices = get_devices(filename)

for hostname, params in devices.items():
    #Connect to device
    connection = pyeapi.client.connect(**params['connection'])   
    device = pyeapi.client.Node(connection)
    #run show ip int br
    output = device.enable(["show ip interface brief"])
    pprint(output)
    print()
    #generate config
    tpl_filename = "arista_conf.j2"
    rendered_config = config_gen(tpl_filename, params['data'])
    #send config cmds to the device
    cmds = rendered_config.split('\n')
    output = device.config(cmds)
    pprint(output)
    print()
    #run the show command again
    output = device.enable(["show ip interface brief"])
    pprint(output)
    print()

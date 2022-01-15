from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from pprint import pprint
from jnpr_devices import srx2
from jnpr_funcs import gather_routes

#connect to device
device = Device(**srx2)
device.open()
device.timeout = 60

#send config via file
cfg = Config(device)
cfg.lock()

#retrieve routes
route_table = gather_routes(device)
print("Current Routes:\n")
pprint(route_table.items())

#add static routes
cfg.load(path="static_routes.conf", format="text", merge=True)
cfg.commit( comment="testing adding static routes!" )
print("routes are added!")

#retrieve routes
route_table = gather_routes(device)
print("Current Routes:\n")
pprint(route_table.items())

#remove static routes
cfg.load("delete routing-options static route 203.0.113.5/32 discard", format="set", merge=True)
cfg.load("delete routing-options static route 203.0.113.200/32 discard", format="set", merge=True)
cfg.commit( comment="testing removing static routes!" )
print("routes are removed!")

#retrieve routes
route_table = gather_routes(device)
print("Current Routes:\n")
pprint(route_table.items())

#unlock config mode
cfg.unlock()

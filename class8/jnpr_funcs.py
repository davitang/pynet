from jnpr.junos import Device
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable
from pprint import pprint

def check_connection(device):
    if device.connected:
        print(f" {device.facts['hostname']} is connected!")
    else:
        print(f"{device.facts['hostname']} is NOT connected!")
    return device.connected

def gather_routes(device):
    routes = RouteTable(device)
    routes.get()
    return routes

def gather_arp_table(device):
    arp_table = ArpTable(device)
    arp_table.get()
    return arp_table

def print_output(device, route_table, arp_table):
    print("device info:\n")
    print(f"hostname: {device.hostname}")
    print(f"port: {device.port}")
    print(f"user: {device.user}")
    print("device route table:\n")
    pprint(route_table.items())
    print("device arp table:\n")
    pprint(arp_table.items())
    
if __name__ == '__main__':
    from jnpr_devices import srx2
    test_device = Device(**srx2)
    test_device.open()
    
    if not  check_connection(test_device):
        exit()
    
    r_table = gather_routes(test_device)
    a_table = gather_arp_table(test_device)
    print_output(test_device, r_table, a_table)
    

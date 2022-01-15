from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

device_info = {
    'host':'srx2.lasthop.io',
    'user':'pyclass',
    'password':getpass(),
}

srx2 = Device(**device_info)
srx2.open()
#pprint(srx2.facts)
print(srx2.facts['hostname'])

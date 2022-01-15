#!/usr/bin/env python
from __future__ import print_function, unicode_literals

from jnpr.junos import Device
from lxml import etree
from getpass import getpass
from jnpr_devices import srx2
from pprint import pprint

device = Device(**srx2)
device.open()

#display show_version
xml_out = device.rpc.get_software_information()
pprint(etree.tostring(xml_out, encoding="unicode", pretty_print=True))
print('-'*80)
print()

#display show interface terse 
xml_out = device.rpc.get_interface_information(terse=True)
pprint(etree.tostring(xml_out, encoding="unicode", pretty_print=True))
print('-'*80)
print()

#display show_version
xml_out = device.rpc.get_interface_information(interface_name='fe-0/0/7', terse=True, normalize=True)
pprint(etree.tostring(xml_out, encoding="unicode", pretty_print=True))


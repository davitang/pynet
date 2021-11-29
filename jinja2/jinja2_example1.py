#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import jinja2

bgp_vars = {
    "local_as": 10,
    "peer1_ip": "10.255.255.2",
    "peer1_as": 20,
    "advertised_route1": "10.10.200.0/24",
    "advertised_route2": "10.10.201.0/24",
    "advertised_route3": "10.10.202.0/24",
}

bgp_template = '''
feature bgp
router bgp {{ local_as }}
  address-family ipv4 unicast
    network {{ advertised_route1 }}
    network {{ advertised_route2 }}
    network {{ advertised_route3 }}
  neighbor {{ peer1_ip }} remote-as {{ peer1_as }}
    update-source loopback1
    ebgp-multihop 2
'''


t = jinja2.Template(bgp_template)
print(t.render(bgp_vars))

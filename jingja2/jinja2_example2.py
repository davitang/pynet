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

template_file = "nxos_bgp.j2"

with open(template_file) as f:
    bgp_template = f.read() 

t = jinja2.Template(bgp_template)
print(t.render(bgp_vars))

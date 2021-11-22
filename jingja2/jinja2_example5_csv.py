#!/usr/bin/env python
from __future__ import print_function, unicode_literals
from pprint import pprint
import jinja2
import csv


csv_file = "bgp_variables.csv"
with open(csv_file) as f:
    read_csv = csv.DictReader(f)
    #Convert advertised routes to a list
    for bgp_vars in read_csv:
        #pprint(bgp_vars)
        advertised_routes = bgp_vars["advertised_routes"]
        advertised_routes = advertised_routes.split()
        bgp_vars["advertised_routes"] = advertised_routes
        
        bgp_vars["peer1_ipv6"] = True if bgp_vars["peer1_ipv6"] == "True" else False
            

        template_file = "nxos_bgp_condition.j2"
        with open(template_file) as f:
            bgp_template = f.read()
        
        template = jinja2.Template(bgp_template)
        print()
        print('-'*80)
        print(template.render(bgp_vars))
        print('-'*80)
        print()

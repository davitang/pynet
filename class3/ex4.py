import json
from pprint import pprint

with open("arp_data.json") as f:
    arp_data = json.load(f)
    ip_to_mac = {}
    for arp_entry in arp_data['ipV4Neighbors']:
        ip_to_mac[arp_entry['address']] = arp_entry['hwAddress']

    pprint(ip_to_mac)

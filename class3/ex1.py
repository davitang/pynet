from pprint import pprint

arp_data = '''
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
'''

arp_entries_list = arp_data.strip().splitlines()

arp_entries_dicts = []

for entry in arp_entries_list:
    if entry.startswith("Protocol"):
        continue
    _, ip_addr, _, mac_addr, _, intf = entry.split()
    arp_entries_dicts.append({"ip_addr": ip_addr, "mac_addr": mac_addr, "intf": intf })

pprint(arp_entries_dicts)

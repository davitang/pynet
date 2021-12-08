from ciscoconfparse import CiscoConfParse

bgp_config_data = '''
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
'''

cisco_cfg = CiscoConfParse(bgp_config_data.splitlines())

bgp_peers = cisco_cfg.find_objects(r"neighbor")

peer_and_as = []

for peer in bgp_peers:
    peer_ip = peer.text.split()[1]
    peer_as = peer.re_search_children(r"remote-as")[0].text.split()[1]
    peer_and_as.append((peer_ip, peer_as))

print()
print("BGP peers:")
print(peer_and_as)
print()

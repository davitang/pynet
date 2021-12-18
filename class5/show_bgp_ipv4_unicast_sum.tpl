Value PEER_IP ([0-9.]+)
Value PEER_AS (\d+)
Value UP_DOWN (\S+)
Value STATE_PFXRCD (\S+)

Start
 ^Neighbor.*PfxRcd\s*$$ -> BGPNeighbor

BGPNeighbor
 ^${PEER_IP}\s+\d\s+${PEER_AS}\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+${UP_DOWN}\s+${STATE_PFXRCD}\s*$$ -> Record



#BGP summary information for VRF default, address family IPv4 Unicast
#BGP router identifier 10.1.100.2, local AS number 22
#BGP table version is 3, IPv4 Unicast config peers 1, capable peers 1
#0 network entries and 0 paths using 0 bytes of memory
#BGP attribute entries [0/0], BGP AS path entries [0/0]
#BGP community entries [0/0], BGP clusterlist entries [0/0]
#
#Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
#10.1.100.1      4    22      34      34        3    0    0 00:28:43 0

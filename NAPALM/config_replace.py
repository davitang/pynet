#!/usr/bin/env python
#import pdb
from pprint import pprint
from napalm import get_network_driver
from my_functions import open_napalm_connection, create_checkpoint
#get device
from my_devices import nxos1

#Supress SSL Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

NXOS_REPLACEMENT_CANDIDATE = "nxos1_replacement_cfg"

if __name__ == '__main__':
    conn = open_napalm_connection(nxos1)
    #pdb.set_trace()
    #Create a checkpoint from the current configuration
    create_checkpoint(conn)
    
    print("\n\n")
    conn.load_replace_candidate(NXOS_REPLACEMENT_CANDIDATE)
    print("Config Staged: pending differences {}".format(conn.hostname))
    print(">"*8)
    print(conn.compare_config())
    print(">"*8)

    print("\n\n")
    print("Discarding candidate config for device {}".format(conn.hostname))
    conn.discard_config()
    print("Diff after discarding canditate config for device{}".format(conn.hostname))
    print(">"*8)
    print(conn.compare_config())
    print(">"*8)
    print("\n\n")
    conn.close()


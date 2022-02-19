#!/usr/bin/env python
from pprint import pprint
from napalm import get_network_driver

#get device
from my_devices import cisco3, eos1

#Supress SSL Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_connection(device_info):
    device_type = device_info.pop("device_type")
    driver = get_network_driver(device_type)
    napalm_conn = driver(**device_info)
    return napalm_conn

connections = [get_connection(device) for device in [cisco3, eos1]]

if __name__ == '__main__':
    for conn in connections:
        print(f"connnection object: {conn}")
        conn.open()
        pprint(conn.get_facts())
        conn.close()


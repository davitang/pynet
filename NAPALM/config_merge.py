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

def hit_enter():
    input("Hit enter to continue: ")

connections = [get_connection(device) for device in [cisco3, eos1]]

partial_config = "loopbacks.txt"

if __name__ == '__main__':
    for conn in connections:
        print(f"connnection object: {conn}")
        conn.open()
        print()
        print(">>>Load config change (merge) - no commit")
        conn.load_merge_candidate(filename=partial_config)
        print("Diff now:")
        print(conn.compare_config())
        hit_enter()
        
        print()
        print(">>>commit config")
        conn.commit_config()
        print("Diff now:")
        print(conn.compare_config())
        hit_enter()

        print()
        print(">>>rollback")
        conn.rollback()
        print("Diff now:")
        print(conn.compare_config())
        conn.commit_config()
        hit_enter()
        conn.close()



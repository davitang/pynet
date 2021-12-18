from os import path
from netmiko import ConnectHandler
from yaml import safe_load as load
from textfsm import TextFSM
from pprint import pprint
from time import sleep

def extract_device(filename):
    with open(filename) as f:
        yaml_out = load(f)
    return yaml_out


def table_converter(header_row, data):
    col_len = len(header_row)
    output = []
    for entry in data:
        new_row = {}
        for i in range(col_len):
            new_row[header_row[i]] = entry[i]
        output.append(new_row)
    return output

if __name__ == "__main__":
    home_dir = path.expanduser("~")
    file_name = path.join(home_dir, ".netmiko.yml")
    
    devices = extract_device(file_name)
    hostnames = ['nxos1', 'nxos2']
    
    #config push
    for hostname in hostnames:
        net_connect = ConnectHandler(**devices[hostname])
        output = net_connect.send_config_from_file( hostname + '.cfg' )
        #output += net_connect.save_config()
        print('-' * 80)
        print(output)
        print('-' * 80)
        net_connect.disconnect()

    sleep(60)
    #Post-check bgp peer status verification:
    for hostname in hostnames:
        print(f"checking on {hostname}...\n ")
        net_connect = ConnectHandler(**devices[hostname])
        raw_data = net_connect.send_command('show bgp ipv4 unicast summary', use_textfsm=True)
        
        tpl_file = "show_bgp_ipv4_unicast_sum.tpl"
        template = open(tpl_file)
        re_table = TextFSM(template)
        bgp_data = re_table.ParseText(raw_data)
        bgp_peer_table = table_converter(re_table.header, bgp_data)
        #pprint(bgp_peer_table)
        if not bgp_peer_table or len(bgp_peer_table) == 0:
            print(f"{hostname} has no bgp peer configured!\n")
            continue

        all_bgp_ok = True
        for peer in bgp_peer_table:
            if peer['STATE_PFXRCD'] in ["Active", "Idle"]:
                print(f"BGP peer {peer['PEER_IP']} is {peer['STATE_PFXRCD']}!\n")
                if all_bgp_ok:
                    all_bgp_ok = False

        if all_bgp_ok:
            print("All Bgp peers are up!\n")
     
        template.close()

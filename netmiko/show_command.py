from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device1 = {
    'host':'nxos1.lasthop.io',
    'username':'pyclass',
    'password':password,
    'device_type':'cisco_nxos'
}


device2 = {
    'host':'nxos2.lasthop.io',
    'username':'pyclass',
    'password':password,
    'device_type':'cisco_nxos'
}

devices = [device1, device2]

for device in devices:
    net_connect = ConnectHandler(**device)
    show_ver_output = net_connect.send_command("show version")
    file_name = device['host'] + "_show_version.txt"
    with open(file_name, "w") as f:
        print("writing output into file....")
        f.write(show_ver_output)
        print("{} is created!".format(file_name))
    net_connect.disconnect()



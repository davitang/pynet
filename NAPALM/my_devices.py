from getpass import getpass

password = getpass()
cisco3 = dict(
    hostname="cisco3.lasthop.io",
    device_type="ios",
    username="pyclass",
    password=password,
    optional_args={},
)

eos1 = dict(
    hostname="arista1.lasthop.io",
    device_type="eos",
    username="pyclass",
    password=password,
)

nxos1 = dict(
    hostname="nxos1.lasthop.io",
    device_type="nxos",
    username="pyclass",
    password=password,
    optional_args={"port":8443}
)

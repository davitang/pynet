from napalm import get_network_driver

def open_napalm_connection(device):
    """function to open napalm conection and return connection object"""
    #Copy dictionary to ensure original object is not modified
    device = device.copy()
    #Pop "platform" as this is invalid kwarg to napalm
    platform = device.pop("device_type")
    driver = get_network_driver(platform)
    conn = driver(**device)
    conn.open()
    return conn

def create_backup(conn):
    """Function to create backup config and write it into a file"""
    backup = conn.get_config()
    filename = f"{conn.hostname}-runnning.txt"
    with open(filename, "w") as f:
        f.write(backup["running"])

def create_checkpoint(conn):
    """Function to create and save nxos checkpoint into a file"""
    if "nxos" in conn.platform:
        filename = f"{conn.hostname}-running.txt"
        backup = conn._get_checkpoint_file()
        with open(filename, "w") as f:
            f.write(backup)
    else:
        raise ValueError("Checkpoint requires NX-OS")


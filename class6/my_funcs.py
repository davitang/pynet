import yaml
from getpass import getpass
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

#retrieve device params from yml file
def get_device(filename):
    with open(filename) as f:
        device = yaml.safe_load(f)
    device['password'] = getpass()
    return device

#retrieve multiple devices pramas
def get_devices(filename):
    with open(filename) as f:
        devices = yaml.safe_load(f)
    password = getpass()
    for hostname in devices.keys():
        devices[hostname]['connection']['password'] = password
    return devices

#print show command output
def print_table(output):
    for item in output[0]["result"]["ipV4Neighbors"]:
        print(f"IP: {item['address']:15} -> MAC: {item['hwAddress']}")


#Simple configGen
def config_gen(tpl_filename, device_data):
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader(['.'])
    template = env.get_template(tpl_filename)
    return template.render(**device_data)

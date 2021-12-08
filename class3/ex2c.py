import yaml
from pprint import pprint

with open("my_devices.yaml") as f:
    pprint(yaml.load(f, yaml.Loader))

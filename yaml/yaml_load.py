import yaml
from pprint import pprint

filename = "simple_device.yaml"
with open(filename) as f:
    output = yaml.load(f, yaml.Loader)

print()
pprint(output)
print(type(output))
print(output['hostname'])
print()


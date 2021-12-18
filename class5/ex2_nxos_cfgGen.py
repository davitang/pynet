from __future__ import unicode_literals, print_function
from os import path
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from yaml import safe_load as load
from pprint import pprint


#env = Environment()
#env.loader = FileSystemLoader('.')
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(['.', './templates'])

work_dir = path.expanduser('~/pynet/class5/device')
file_name = path.join(work_dir, 'nxos_devices.yml')

with open(file_name) as f:
    devices = load(f)
    #pprint(devices)


template_file = "nxos_int_bgp.j2"
template = env.get_template(template_file)

for device, settings in devices.items():
#    print(f"Rendered Config of {device}:\n")
#    print('-' * 80)
#    print(template.render(**settings))
#    print('-' * 80)
#    print()
    rendered_cfg_filename = device + ".cfg"
    with open(rendered_cfg_filename, "w") as f:
        f.write(template.render(**settings)) 

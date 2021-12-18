from jinja2 import Template
from os import path
from yaml import safe_load

with open("vrfs.yml") as f:
    vrfs = safe_load(f)

home_dir = path.expanduser('~/pynet/class5/templates')
file_name = path.join(home_dir, 'vrf.j2')

with open(file_name) as f:
    vrf_template = f.read()

for vrf, vrf_data in vrfs.items():
    template = Template(vrf_template)
    vrf_config = template.render(**vrf_data)
    print(vrf_config)


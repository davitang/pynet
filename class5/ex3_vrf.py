from jinja2 import Template
from os import path

vrf_var = {
    'VRF_NAME': 'blue',
    'VRF_RD': '100:1',
    'AF_IPV4': True,
    'AF_IPV6': True,
}

home_dir = path.expanduser('~/pynet/class5/templates')
file_name = path.join(home_dir, 'vrf.j2')

file = open(file_name)
vrf_template = file.read()

template = Template(vrf_template)
vrf_config = template.render(**vrf_var)
print(vrf_config)

file.close()

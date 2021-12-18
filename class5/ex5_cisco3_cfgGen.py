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
file_name = path.join(work_dir, 'cisco3.yml')

with open(file_name) as f:
    device  = load(f)
    #pprint(devices)


template_file = "cisco3_base.j2"
template = env.get_template(template_file)
rendered_cfg_filename = "cisco3_rendered_cfg.txt"
with open(rendered_cfg_filename, "w") as f:
    f.write(template.render(**device)) 

import xmltodict
from pprint import pprint

xml_filename = "show_security_zones.xml"

with open(xml_filename) as f:
    xml_data = f.read().strip()
    my_xml = xmltodict.parse(xml_data)
    print()
    print("my_xml:\n")
    pprint(my_xml)
    print()
    print("type:{}".format(type(my_xml)))
    idx = 1
    for zone in my_xml['zones-information']['zones-security']:
        print(f"Security Zone#{idx}: {zone['zones-security-zonename']}")
        idx += 1




"""
OrderedDict([('zones-information',
              OrderedDict([('zones-security',
                            [OrderedDict([('zones-security-zonename', 'trust'),
                                          ('zones-security-send-reset', 'Off'),
                                          ('zones-security-policy-configurable',
                                           'Yes'),
                                          ('zones-security-interfaces-bound',
                                           '1'),
                                          ('zones-security-interfaces',
                                           OrderedDict([('zones-security-interface-name',
                                                         'vlan.0')]))]),
                             OrderedDict([('zones-security-zonename',
                                           'untrust'),
                                          ('zones-security-send-reset', 'Off'),
                                          ('zones-security-policy-configurable',
                                           'Yes'),
                                          ('zones-security-screen',
                                           'untrust-screen'),
                                          ('zones-security-interfaces-bound',
                                           '2'),
                                          ('zones-security-interfaces',
                                           OrderedDict([('zones-security-interface-name',
                                                         ['fe-0/0/0.0',
                                                          'pt-1/0/0.0'])]))]),
                             OrderedDict([('zones-security-zonename',
                                           'junos-host'),
                                          ('zones-security-send-reset', 'Off'),
                                          ('zones-security-policy-configurable',
                                           'Yes'),
                                          ('zones-security-interfaces-bound',
                                           '0'),
                                          ('zones-security-interfaces',
                                           None)])])]))])
"""

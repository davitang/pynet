import xmltodict
from pprint import pprint

def xml_file_to_dict(filename):
    f = open(filename)
    xml_data = f.read().strip()
    f.close()
    return xmltodict.parse(xml_data)

def xml_file_to_dict_forcelist(filename):
    f = open(filename)
    xml_data = f.read().strip()
    f.close()
    return xmltodict.parse(xml_data, force_list={'zones-security': True})


if __name__ == "__main__":
    file1 = "show_security_zones.xml"
    file2 = "show_security_zones_single_trust.xml"

    xml_1 = xml_file_to_dict(file1)
    xml_2 = xml_file_to_dict(file2)
    
    trust_zone1 = xml_1['zones-information']['zones-security']
    print("from file1:\n")
    pprint(trust_zone1)

    trust_zone2 = xml_2['zones-information']['zones-security']
    print("from file2:\n")
    pprint(trust_zone2)
    
    xml_1 = xml_file_to_dict_forcelist(file1)
    xml_2 = xml_file_to_dict_forcelist(file2)
    
    trust_zone1 = xml_1['zones-information']['zones-security']
    print("from file1:\n")
    pprint(trust_zone1)

    trust_zone2 = xml_2['zones-information']['zones-security']
    print("from file2:\n")
    pprint(trust_zone2)

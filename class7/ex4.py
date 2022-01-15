from lxml import etree

xml_filename = "show_security_zones.xml"
with open(xml_filename) as f:
    xml_data = f.read().strip()
my_xml = etree.fromstring(xml_data)

first_zone = my_xml.find(".//zones-security")
print("Find tag of the first zones-security element")
print("-"*20)
print(first_zone.tag)
print()
print("Find tag of all child elements of the first zones-security")
for child in first_zone:
    print(child.tag)

first_zonename = my_xml.find(".//zones-security-zonename")
print("Find the first zones-security-zonename and print its text")
print("-"*20)
print(first_zonename.text)
print()

print("Find all zones and print the zone name")
print("-"*20)
all_zones = my_xml.findall(".//zones-security")
for zone in all_zones:
    zone_name = zone.find("zones-security-zonename")
    print(zone_name.text)


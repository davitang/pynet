from lxml import etree

xml_filename = "show_version.xml"
with open(xml_filename, "rb") as f:
    xml_data = f.read().strip()

my_xml = etree.fromstring(xml_data)

print("The context of show_version.xml:")
print("_"*20)
print(etree.tostring(my_xml).decode())
print()

print("Find and print proc_board_id:")
print("-"*20)
proc_board_id = my_xml.find(".//{*}proc_board_id")
print(proc_board_id.text)

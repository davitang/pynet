from lxml import etree

xml_filename = "show_security_zones.xml"

with open(xml_filename) as f:
    xml_data = f.read().strip()
    my_xml_etree = etree.fromstring(xml_data)
    
    #ex1a
    print("ex1a: root element and its type:")
    print(my_xml_etree)
    print(type(my_xml_etree)) 
    print()

    #ex1b
    print("ex1b: covert the etree to string and print it out:")
    print(etree.tostring(my_xml_etree).decode())
    print()

    #ex1c
    print("ex1c: root element tab and num of its children")
    print(my_xml_etree.tag)
    print(len(my_xml_etree.getchildren()))
    print()
    
    #ex1d
    print("ex1d: Using both direct indices and the getchildren() method, obtain the first child element and print its tag name.")
    print(my_xml_etree[0].tag)
    print(my_xml_etree.getchildren()[0].tag)
    print()    

    #ex1e
    trust_zone = my_xml_etree.find(".//zones-security")
    print("ex1e: print trust zone text")
    print(trust_zone.find("zones-security-zonename").text)


    #ex1f
    print("ex1f: print tag of children of trust_zone:")
    for child in trust_zone:
        print(child.tag)

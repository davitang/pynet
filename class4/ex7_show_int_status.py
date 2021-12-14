import textfsm
from pprint import pprint

template_file = "ex2_show_int_status.tpl"
template = open(template_file)

cli_output_file = "show_int_status.txt"
with open(cli_output_file) as f:
    raw_text_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)

template.close()

print("\nPrint the header row which could be used for dictionary construction")
print(re_table.header)
print("\nOutput Data: ")
pprint(data)
print()

#Convert Data to a List of Dict
data_new_format = []
for entry in data:
    data_new_format.append({re_table.header[0]: entry[0],
                            re_table.header[1]: entry[1],
                            re_table.header[2]: entry[2],
                            re_table.header[3]: entry[3],
                            re_table.header[4]: entry[4],
                            re_table.header[5]: entry[5],
                                                        
})

pprint(data_new_format)

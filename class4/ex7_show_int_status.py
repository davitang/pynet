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

#Convert the Data to Table Dict

def table_converter(header_row, data):
    col_len = len(header_row)
    output = []
    for entry in data:
        new_row = {}
        for i in range(col_len):
            new_row[header_row[i]] = entry[i]
        output.append(new_row)
    return output

data_new_format = table_converter(re_table.header, data)
pprint(data_new_format)
    

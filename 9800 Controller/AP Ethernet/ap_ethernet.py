import textfsm
import json
import re
from pprint import pprint

def apEthernet(data):
    results = []
    ap_dict = {}
    for ap, apConfig in data.items():
        ethSpeed = apConfig['Speed']
        speed = re.findall(r'\d+', ethSpeed)
        ethernetSpeed = int(speed[0])
        duplex = apConfig['Duplex']
        ap_list = []
        if ethernetSpeed < 1000:  ### 
            ap_list = [ap,ethSpeed,duplex]
            results.append(ap_list)
      
    return(results)

outfile = "AP Ethernet.json"
# Load the input file to a variable
input_file = open("AP Ethernet Stats.txt")
raw_text_data = input_file.read()
input_file.close()

# Run the text through the FSM. 
# The argument 'template' is a file handle and 'raw_text_data' is a 
# string with the content from the show_inventory.txt file
template = open("ap_ethernet.template")
re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(raw_text_data)

# print(fsm_results)
ap_dict = {}
for line in fsm_results:
    temp_dict = {}
    ap = line[0]
    ap_dict[ap] = {}
    temp_dict['Status'] = line[2]
    temp_dict['Speed'] = line[3]
    temp_dict['Duplex'] = line[4]
    ap_dict[ap].update(temp_dict)

with open(outfile, 'wt') as j:
    json.dump(ap_dict, j, indent=4)

ethernet = 'AP Ethernet.json'
   
with open(ethernet) as e:
    ethData = json.load(e)

results = apEthernet(ethData)


pprint(results)
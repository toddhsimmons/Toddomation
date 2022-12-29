import textfsm
import json
import re
from pprint import pprint
import pandas as pd

# This is the method that will be called to determine what AP's
# have Ethernet connections slower than 1 Gbps
def apEthernet(data):
    results = []
    for ap, apConfig in data.items():
        ethSpeed = apConfig['Speed']
        speed = re.findall(r'\d+', ethSpeed)
        ethernetSpeed = int(speed[0])
        duplex = apConfig['Duplex']
        ap_list = []
        if ethernetSpeed < 1000:   
            ap_list = [ap,ethSpeed,duplex]
            results.append(ap_list) 
    return(results)

outfile = "AP Ethernet.json"
input_file = "AP Ethernet Stats.txt"
ethHeaders = ['AP Name', 'Speed', 'Duplex']
ap_dict = {}

# This opens the output from the "show ap ethernet statistics"
# If you don't have this file you can use the get_ethernet.py file
with open(input_file, 'r') as f:
    raw_text_data = f.read()

# Run the text through TextFSM. 
# The argument 'template' is a file handle and 'raw_text_data' is a 
# string with the content from the show_inventory.txt file
template = open("ap_ethernet.template")
re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(raw_text_data)

# Create a dictionary to send to apEthernet method
for line in fsm_results:
    temp_dict = {}
    ap = line[0]
    ap_dict[ap] = {}
    temp_dict['Status'] = line[2]
    temp_dict['Speed'] = line[3]
    temp_dict['Duplex'] = line[4]
    ap_dict[ap].update(temp_dict)
    
# This will create a JSON file to save the data
# with open(outfile, 'wt') as j:
#     json.dump(ap_dict, j, indent=4)

# If you do not wish to parse the text file you could 
# load the JSON file and send it to the apEthernet method   
# with open(outfile) as e:
#     ethData = json.load(e)

results = apEthernet(ap_dict)
# results = apEthernet(ethData)

# This takes the data and writes it to a CSV
df = pd.DataFrame(results, columns=ethHeaders)
df.to_csv('APs with Ethernet Issue.csv', mode='w', index=False, header=True, sep=',')

pprint(results)
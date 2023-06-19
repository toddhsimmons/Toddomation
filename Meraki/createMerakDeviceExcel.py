### Written by Todd with Toddomation
import json
from icecream import ic 
import pandas as pd 
import numpy as np 

empty = {}
networksDict = {}
sheets = []
fullList = []
headers = []

EXCEL_WB = "Toddomation_Excel.xlsx"

### Opens the JSON files that contains all networks for the entire ORG
with open("AllOrgNetworks.json", "r") as e:
    orgNetworks = json.load(e)

### Opens the JSON file that contains all devices for the entire ORG
with open("AllOrgDevices.json", "r") as f:
    allDevices = json.load(f)

'''
These lines create the list of headers based on the dictionary keys for each of the devices. 
This is a longer process because it will go through the keys for every single device 
in the JSON file, creating a list full of duplicates.  Then it will go through the created
list and everytime a new value is found it adds it to the headers list. 
I did some data massaging when it comes to the IP Addresses of the devices as well.  This
is because I wanted the devices IPs to be together in the Excel document. 
'''
for device in allDevices:
    tempList = list(device.keys())
    fullList.extend(tempList)
[headers.append(x) for x in fullList if x not in headers]

lanIp = headers.index("lanIp")
wan1Ip = headers.index("wan1Ip")
wan2Ip = headers.index("wan2Ip")
wan1 = headers.pop(wan1Ip)
headers.insert(lanIp+1, wan1)
wan2 = headers.pop(wan2Ip)
headers.insert(lanIp+2, wan2)

'''
This next code does a few things to create the necessary structure
1. Updates the "sheets" list with all of the network names in the ORG
2. Adds each network id as a key to a dictionary with the network name as the value
This is neceaary because the API call to get all ORG devices only specifies the network id
and the speadsheet should use network names for the different worksheets.
'''
for network in orgNetworks:
    networkName = network["name"]
    networkId = network["id"]
    sheets.append(networkName)
    networksDict[networkId] = networkName

sheets.sort()  ### Sort the list of network in alphabetical order
createSheets = pd.DataFrame(empty, columns=headers) # This creates all the worksheets based on network names with no data
with pd.ExcelWriter(EXCEL_WB, mode="w") as writer:
    '''
    This is where the Excel workbook is created.  If there is an existing file with the same name
    it will be overwritten
    All of the worksheets will be created based on the network name
    The headers will then be added to each of the workshets
    '''
    for sheet in sheets:
        createSheets.to_excel(writer, sheet_name=sheet, index=False, columns=headers)
        # writeHeaders.to_excel(writer, sheet_name=sheet, index=False, columns=headers)

'''
Because the Tags are stored in a list in Meraki we need to seperate those items
into comma seperated strings that is a single entry. 
This code below does that and creates a new JSON file with the values for the tag
key to the comma seperated strings
'''
for device in allDevices:
    if len(device["tags"]) > 1:
        device["tags"] = ",".join(device["tags"])
    else:
        device["tags"] = ''.join(device["tags"])

# This creates the new JSON file after changing the list entries into a comma seperated string
with open("AllOrgDevicesStrings.json", "w") as f:
    json.dump(allDevices, f, indent=4)

# Just to make sure this loads the just created JSON into a new dictionary
with open("AllOrgDevicesStrings.json", "r") as f:
    cleanDevices = json.load(f)

### Here the Excel workbook opened again so the devices can be written to their respective worksheets
with pd.ExcelWriter(EXCEL_WB, mode="a", if_sheet_exists="overlay", engine="openpyxl") as writer:
    '''
    Here the code will determine what network the current device belongs to so it knows what
    tab in the Excel workbook it needs to activate.  Using the "overlay" option above allows 
    this because all the worksheets have already been created.  
    With the "to_excel" method it appends to the worksheet using the "startrow" option with 
    the syntax after to start of the next available row. 
    Lastly, using the "na_rep" if the key doesn't exist in the data it will write "N/A" on that row.  
    This is important because different devices use different keys.  The best example is for the MX
    Security Appliances, they don't have a lanIp, instead they have wan1Ip and wan2Ip keys.  
    '''
    for device in cleanDevices:
        networkId = device["networkId"]
        networkName = networksDict[networkId]
        entry = pd.DataFrame(device, index=[0], columns=headers)
        entry.to_excel(writer, sheet_name=networkName,index=False, 
                       startrow=writer.sheets[networkName].max_row,header=False,
                       na_rep="N/A", columns=headers)
    
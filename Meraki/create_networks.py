import meraki
import os 
from pprint import pprint
from get_excel_data import get_data

API_KEY = os.environ.get("MERAKI_KEY")
meraki_products = ['appliance', 'camera', 'cellularGateway', 'sensor', 'switch', 'systemsManager', 'wireless']
new_networks = []

org_excel, networks_excel = get_data()

# print(org_excel)
# pprint(networks_excel)


# This sets up the connection to the Meraki Dashboard
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

# This will return a list of Org data with keys and values
orgs = dashboard.organizations.getOrganizations()

organization_name = org_excel[0]['Org_Name']

for org in orgs:
    name = org["name"]
    id = org["id"]
    if name == organization_name:
        organization_id = id
        
for network in networks_excel:
    network_dict = {}
    name = network['Name']
    tag = network['Tags']
    network_dict[name] = {'notes': network['Notes'],
                          'tags': [tag],
                          'timeZone': network['Timezone'],
                          'products': []
                          }
    # if network['appliance'] == True:
    #     network_dict[name]['products'].append('appliance')
    # if network['camera'] == True:
    #     network_dict[name]['products'].append('camera')
    # if network['cellularGateway'] == True:
    #     network_dict[name]['products'].append('cellularGateway')
    # if network['sensor'] == True:
    #     network_dict[name]['products'].append('sensor')
    # if network['switch'] == True:
    #     network_dict[name]['products'].append('switch')
    # if network['systemsManager'] == True:
    #     network_dict[name]['products'].append('systemsManager')
    # if network['wireless'] == True:
    #     network_dict[name]['products'].append('wireless')
        
    for product in meraki_products:
        if network[product]  == True:
            network_dict[name]['products'].append(product)

    new_networks.append(network_dict)

# pprint(new_networks)

for entry in new_networks:
    # 
    for network, values in entry.items():
        name = network
        product_types = values['products']
        timeZone = values['timeZone']
        notes = values['notes']
        tags = values['tags']
        # print(organization_id, name, product_types, timeZone, notes, tags)

        dashboard.organizations.createOrganizationNetwork(organization_id, name, product_types, timeZone=timeZone, notes=notes, tags=tags)


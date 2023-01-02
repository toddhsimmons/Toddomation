import os
from pprint import pprint
import meraki

API_KEY = os.environ.get("MERAKI_API_KEY")
ORG_NAME = ""
NETWORK_NAME = ""


# # Gets the Orgs the API Key has access to
# dashboard = meraki.DashboardAPI(API_KEY)
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)
orgs = dashboard.organizations.getOrganizations()
# pprint(orgs)

# This gets the Organizational ID based on the variable specified above
for entry in orgs:
    if entry['name'] == ORG_NAME:
        organization_id = entry["id"]
# print(organization_id)    

    
# Gets the Networks of an Org and gets the ID based on the variable specified
networks = dashboard.organizations.getOrganizationNetworks(organization_id)
# pprint(networks)

for entry in networks:
    if entry['name'] == NETWORK_NAME:
       network_id = entry["id"]

# print(network_id)

# Create a new Network
# organization_id = ''
name = 'Toddomating Memphis'
product_types = ['appliance', 'switch', 'camera']

response = dashboard.organizations.createOrganizationNetwork(
    organization_id, name, product_types, 
    tags=['memphis','Toddomation'], 
    timeZone='America/Chicago', 
    notes='Memphis Remote Office for Todd'
)

print(response)

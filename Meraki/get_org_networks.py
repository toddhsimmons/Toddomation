import os
from pprint import pprint
import meraki

API_KEY = os.environ.get("MERAKI_KEY")
all_org_networks = []
# # Gets the Orgs the API Key has access to

dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)
orgs = dashboard.organizations.getOrganizations()
# pprint(orgs)

# This gets the Organizational ID based on the variable specified above
for entry in orgs:
    organization_id = entry["id"]
    network = dashboard.organizations.getOrganizationNetworks(organization_id)
    if len(network) < 1:
        print(organization_id)
    all_org_networks.append(network)

pprint(all_org_networks)    

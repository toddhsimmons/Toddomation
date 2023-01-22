import os
from pprint import pprint
import meraki

API_KEY = os.environ.get("MERAKI_KEY")
ORG_ID = "YOUR ORG ID HERE"

# This sets up the connection to the Meraki Dashboard
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

# This will return a list of Org data with keys and values
orgs = dashboard.organizations.getOrganizations()

# pprint(orgs)

# If you accidentaly have multiple Orgs with the same name this will delete the extras
for org in orgs:
    name = org["name"]
    id = org["id"]
    print(f"{name} has this ID: {id}")
    if org['id'] != ORG_ID:
        print("Not Valid")
        dashboard.organizations.deleteOrganization(id)
        
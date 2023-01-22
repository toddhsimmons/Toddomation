import os
import meraki
from pprint import pprint

API_KEY = os.environ.get("MERAKI_KEY")
ORG_NAME = "YOUR ORG NAME HERE"

# This sets up the connection to the Meraki Dashboard
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

# This creates a new Organization 
response = dashboard.organizations.createOrganization(ORG_NAME)

### Written by Todd with Toddomation
import json
from decouple import config
import meraki

API_KEY = config("API_KEY")
ORG_ID = config("ORG_ID")

### If you are not using Python-Decouple you can uncomment these lines
### and add the key and ID so the code will work.
# API_KEY = "1234567890asdgfhjklQWERTYUIOPzxcvbnm1234"
# ORG_ID = "12345"

# This sets up the connection to the Meraki Dashboard
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

### This is the API call to get all the Networks configured in the ORG
orgNetworks = dashboard.organizations.getOrganizationNetworks(
    ORG_ID, total_pages="all")
# ic(orgNetworks)

### Create JSON to be able to use offline
with open("AllOrgNetworks.json", "w") as e:
    json.dump(orgNetworks, e, indent=4)

### This is the API call to get all the devices that exist in the ORG
allDevices = dashboard.organizations.getOrganizationDevices(
    ORG_ID, total_pages="all")
# ic(allDevices)

### Create JSON to be able to use offline
with open("AllOrgDevices.json", "w") as f:
    json.dump(allDevices, f, indent=4)


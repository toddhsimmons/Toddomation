### Written by Todd with Toddomation
import json
from decouple import config
import meraki
from icecream import ic

API_KEY = config("API_KEY")
ORG_ID = config("ORG_ID")

### If you are not using Python-Decouple you can uncomment these lines
### and add the key and ID so the code will work.
# API_KEY = "1234567890asdgfhjklQWERTYUIOPzxcvbnm1234"
# ORG_ID = "12345"

# This sets up the connection to the Meraki Dashboard
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

### This is the API call to get all the Networks configured in the ORG
orgNetworks = dashboard.organizations.getOrganizationNetworks(ORG_ID, total_pages="all")
# ic(orgNetworks)

### Create JSON to be able to use offline
with open("AllOrgNetworks.json", "w") as e:
    json.dump(orgNetworks, e, indent=4)


network_id = "L_634444597505861201"

# response = dashboard.switch.getNetworkSwitchAccessControlLists(network_id)

rules = []

response = dashboard.switch.updateNetworkSwitchAccessControlLists(network_id, rules)


ic(response)

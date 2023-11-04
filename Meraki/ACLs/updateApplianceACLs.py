### Written by Todd with Toddomation
import json
from decouple import config
import meraki
from icecream import ic
import meraki
import merakiApplianceACLs as acl

API_KEY = config("API_KEY")
ORG_ID = config("ORG_ID")

network_id = "L_634444597505861201"

### If you are not using Python-Decouple you can uncomment these lines
### and add the key and ID so the code will work.
# API_KEY = "1234567890asdgfhjklQWERTYUIOPzxcvbnm1234"
# ORG_ID = "12345"

# This sets up the connection to the Meraki Dashboard
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

# This gets the data from the Excel Spreadsheet
firewallInACLs, firewallOutACLs = acl.getRules(network_id)

# Update the Firewall Appliance Inbound Rules
response = dashboard.appliance.updateNetworkApplianceFirewallInboundFirewallRules(
    network_id, rules=firewallInACLs
)

# Update the Firewall Appliance Outbound Rules
response = dashboard.appliance.updateNetworkApplianceFirewallL3FirewallRules(
    network_id, rules=firewallOutACLs
)

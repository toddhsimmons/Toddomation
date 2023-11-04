### Written by Todd with Toddomation
import json
from decouple import config
import meraki
from icecream import ic
import getACLs as acl

API_KEY = config("API_KEY")
ORG_ID = config("ORG_ID")

network_id = "L_634444597505861201"

### If you are not using Python-Decouple you can uncomment these lines
### and add the key and ID so the code will work.
# API_KEY = "1234567890asdgfhjklQWERTYUIOPzxcvbnm1234"
# ORG_ID = "12345"

# This sets up the connection to the Meraki Dashboard
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

### This is the API call to get all the Networks configured in the ORG
# orgNetworks = dashboard.organizations.getOrganizationNetworks(ORG_ID, total_pages="all")
# ic(orgNetworks)

### Create JSON to be able to use offline
# with open("AllOrgNetworks.json", "w") as e:
#     json.dump(orgNetworks, e, indent=4)

switchACLs, firewallInACLs, firewallOutACLs, wirelessACLs = acl.get_data(network_id)

# ic(firewallInACLs)
# exit()
response = dashboard.appliance.updateNetworkApplianceFirewallInboundFirewallRules(
    network_id, rules=firewallInACLs
)

# Get Inbound firewall rules

# response = dashboard.appliance.getNetworkApplianceFirewallInboundFirewallRules(
#     network_id
# )
# ic(response)


# Outbound Rules
response = dashboard.appliance.updateNetworkApplianceFirewallL3FirewallRules(
    network_id, rules=firewallOutACLs
)

# ic(switchACLs)


# response = dashboard.switch.getNetworkSwitchAccessControlLists(network_id)


# rules = [
#     {
#         "comment": "Deny SSH",
#         "policy": "deny",
#         "ipVersion": "ipv4",
#         "protocol": "tcp",
#         "srcCidr": "10.1.10.0/24",
#         "srcPort": "any",
#         "dstCidr": "10.0.0.0/24",
#         "dstPort": "22",
#         "vlan": "10",
#     }
# ]


# ic(switchACLs)
# response = dashboard.switch.updateNetworkSwitchAccessControlLists(
#     network_id, switchACLs
# )

# number = "1"

# response = dashboard.wireless.getNetworkWirelessSsidFirewallL3FirewallRules(
#     network_id, number
# )

# ic(response)
# ic(wirelessACLs)
# ssidCount = []
# for line in wirelessACLs:
#     ssidNumber = int(line["ssid"])
#     ssidCount.append(ssidNumber)

# ssids = list(set(ssidCount))

# for ssid in ssids:
#     rules = []
#     for line in wirelessACLs:
#         if line["ssid"] == str(ssid):
#             rules.append(line)
#             lanAccess = bool(line["allowLanAccess"])

#     response = dashboard.wireless.updateNetworkWirelessSsidFirewallL3FirewallRules(
#         network_id,
#         number=ssid,
#         rules=rules,
#         allowLanAccess=lanAccess,
#     )

# ic(response)

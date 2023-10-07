from decouple import config 
from icecream import ic 
from ruckusVSM import vSmartZone_APIs

ruckus = vSmartZone_APIs()

HOST = config("HOST")
LOGIN = config("LOGIN")
PASSWORD = config("PASSWORD")

# This is the name of a zone I'm going to look for
myZone = "Video Lab"

# Login and get the needed token for API calls
token = ruckus.vszAuth(HOST,LOGIN,PASSWORD)
# ic(token)

zones = ruckus.getAllZones(HOST,token)
# ic(zones)

zoneId = ruckus.filterZone(zones,myZone)
# ic(zoneId)

zoneData = ruckus.getZone(HOST, zoneId, token)
# ic(zoneData)

allSessions = ruckus.getSessions(HOST,token)
# ic(allSessions)

deleteToken = ruckus.deleteToken(HOST,token) # ruckus.deleteToken(HOST,token)
ic(deleteToken)

import requests
import warnings

# Let's ignore the warnings if the vSZ instance has a SSC
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

#This class is used to hold the created methods
class vSmartZone_APIs:
    
    # This method will login to the vSZ and return login Token
    def vszAuth(self, host, username, password):
        url = f"{host}/wsg/api/public/v11_0/serviceTicket"
        body = {'username': username, 'password': password}
        r = requests.post(url, json=body, verify=False).json()
        token = r['serviceTicket']
        return token
    
    # Method to delete the login token
    def deleteToken(self, host, token):
        url = f"{host}/wsg/api/public/v11_0/serviceTicket?serviceTicket={token}"
        r = requests.delete(url, verify=False)
        return r

    # Method to get get a list of all Wireless AP Zones
    def getAllZones(self, host, token):
        url = f"{host}/wsg/api/public/v11_0/rkszones?serviceTicket={token}"
        request = requests.get(url, verify=False).json()
        zones = request['list']
        return zones     

    # Method to return all AP Zone data for a specified zone
    def filterZone(self, zoneList, value):
        for zone in zoneList:
            if zone['name'] == value:
                zoneId = zone['id']
                break
        return zoneId

    # Method to return all AP Zone data for a specified zone
    def getZone(self, host, zoneId, token):
        url = f"{host}/wsg/api/public/v11_0/rkszones/{zoneId}?serviceTicket={token}"
        zone = requests.get(url, verify=False).json()
        return zone
    
        # Method to return all AP Zone data for a specified zone
    def getSessions(self, host, token):
        url = f"{host}/wsg/api/public/v11_0/sessionManagement?serviceTicket={token}"
        request = requests.get(url, verify=False).json()
        sessions = request['list']
        return sessions
